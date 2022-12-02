import os
import asyncio
import time

from celery import shared_task
from celery.utils.log import get_task_logger
from telegram.ext import ApplicationBuilder
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)

logger = get_task_logger(__name__)

async def _send_plain_message(chat_id, text):
    api_token = os.getenv('TELEGRAM_BOT_API_TOKEN')
    application = ApplicationBuilder().token(api_token).build()
    await application.bot.send_message(
        chat_id=chat_id,
        text=text,
    )


async def _send_markup_message(chat_id, text, button_url, button_text, delay):
    api_token = os.getenv('TELEGRAM_BOT_API_TOKEN')
    application = ApplicationBuilder().token(api_token).build()
    button = InlineKeyboardButton(
        text=button_text,
        url=button_url,
    )
    keyboard = InlineKeyboardMarkup.from_button(button)
    time.sleep(delay)
    await application.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=keyboard,
    )


@shared_task
def send_telegram_bot_message(chat_id, text, button_url=None,
                              button_text=None, delay=0):
    if not chat_id:
        return
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    if (button_url and button_text):
        coroutine = _send_markup_message(
            chat_id, text, button_url, button_text, delay
        )
    else:
        coroutine = _send_plain_message(chat_id, text)
    loop.run_until_complete(coroutine)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")
    print("hello celery")

