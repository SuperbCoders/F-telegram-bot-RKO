import os

import requests

from telegram.ext import (ApplicationBuilder, CommandHandler)
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)
from telegram.constants import ParseMode


async def start(update, context):
    text = (
        "Официальный бот Банка ЗЕНИТ для частных лиц, малого бизнеса " +
        "и компаний." +
        "\n\n" +
        "/start начать работу с ботом\n" +
        "/loan подать заявку на кредит\n" +
        "/status узнать статус заявок\n" +
        "/chat связаться с поддержкой банка"
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


async def chat(update, context):
    CHAT_URL = "https://www.zenit.ru/bank/general/contacts/"
    button = InlineKeyboardButton(
        text="Чат с сотрудником банка",
        url=CHAT_URL,
    )
    keyboard = InlineKeyboardMarkup.from_button(button)
    text = (
        "Связаться с поддержкой банка можно нажав на кнопку и " +
        "перейдя на сайт банка."
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=keyboard,
    )


async def loan(update, context):
    WEB_APP_URL = "https://loan-application-bot.baraba.sh/"
    button = InlineKeyboardButton(
        text="Подать заявку",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    keyboard = InlineKeyboardMarkup.from_button(button)
    text = (
        "Оформите заявку чтобы получить потребительский кредит " +
        "наличными на выгодных условиях с низкой ставкой."
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=keyboard,
    )


def get_user_applications(chat_id):
    api_url = (
        "https://api.loan-application-bot.baraba.sh/" +
        f"loan-application/{chat_id}/"
    )
    user_applications = []
    try:
        response = requests.get(api_url, timeout=10)
        if response.json():
            user_applications = response.json()
    except Exception:
        pass
    return user_applications


async def status(update, context):
    chat_id = update.effective_chat.id
    user_applications = get_user_applications(chat_id)
    if user_applications:
        status_list = [
            (
                f"Заявка #{i} от {application['createdAt'][:10]} " +
                f"на {application['loanAmount']} рублей\n" +
                f'Статус заявки: \"{application["status"]}\"'
            )
            for i, application in enumerate(user_applications, start=1)
        ]
        text = "\n\n".join(status_list)
    else:
        text = "Заявок не найдено."
    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
    )


def run_bot():
    api_token = os.getenv('TELEGRAM_BOT_API_TOKEN')
    application = ApplicationBuilder().token(api_token).build()

    start_handler = CommandHandler('start', start)
    loan_handler = CommandHandler('loan', loan)
    status_handler = CommandHandler('status', status)
    chat_handler = CommandHandler('chat', chat)
    application.add_handler(start_handler)
    application.add_handler(loan_handler)
    application.add_handler(status_handler)
    application.add_handler(chat_handler)

    application.run_polling()


if __name__ == '__main__':
    run_bot()
