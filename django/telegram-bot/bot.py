from datetime import datetime, date
import os
import random

import requests
import string

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    TypeHandler,
    filters,
    MessageHandler,
)

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.constants import ParseMode


def debug_print(*args):
    if os.getenv("DEBUG"):
        print(*args)


def is_chat_id_confirmed(chat_id):
    debug_print("is_chat_id_confirmed", chat_id, "start")
    api_url = (
        os.getenv("DJANGO_APP_API_ROOT_URL") +
        f"api/user/{chat_id}/"
    )
    debug_print("api_url", api_url)
    try:
        response = requests.get(api_url, timeout=10, verify=False)
        debug_print("response text", response.text)
        if response.status_code == 200:
            debug_print("return is_chat_id_confirmed", "true")
            return True
    except Exception as error:
        debug_print("return is_chat_id_confirmed", "false")
        return False


async def start(update, context):
    text = (
        "Официальный бот Банка «Ренессанс Кредит» для открытия расчетного счета" +
        "\n\n" +
        "/start начать работу с ботом\n" +
        "/apply подать заявку на РКО\n" +
        "/status узнать статус заявок\n" +
        "/chat связаться с поддержкой банка"
    )
    button_start = KeyboardButton(
        text="/start",
    )
    button_apply = KeyboardButton(
        text="/apply",
    )
    button_status = KeyboardButton(
        text="/status",
    )
    button_chat = KeyboardButton(
        text="/chat",
    )
    reply_markup = ReplyKeyboardMarkup(
        [[button_start, button_apply], [button_status, button_chat]],
        one_time_keyboard=True,
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=reply_markup,
    )


async def chat(update, context):
    debug_print("chat", "start")
    text = (
        "Контакт-центр Банка “Ренессанс Кредит”\n" +
        "8-800-200-0-981(круглосуточно, бесплатно по России)"
    )
    debug_print("chat", "message", "text")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


async def apply(update, context):
    debug_print("apply", "start")
    debug_print("apply", "is_chat_id_confirmed(update.effective_chat.id)",
                is_chat_id_confirmed(update.effective_chat.id))
    if not is_chat_id_confirmed(update.effective_chat.id):
        keyboard = KeyboardButton(
            text="Подтвердить",
            request_contact=True,
        )
        reply_markup = ReplyKeyboardMarkup(
            [[keyboard]],
            one_time_keyboard=True,
        )
        text = (
            "Пройдите авторизацию. Для этого необходимо разрешить использование вашего номера телефона."
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=reply_markup,
        )
    else:

        res_phone = requests.get(
            os.getenv("DJANGO_APP_API_ROOT_URL") +
            f"api/get_phone/{update.effective_chat.id}/"
        )
        debug_print("res_phone text", res_phone.text)
        phone = (res_phone.json()['phone'].replace('+', ''))
        debug_print("phone", phone)
        WEB_APP_URL = os.getenv("DOMAIN_APP_URL") + f"?phone={phone}"
        debug_print("WEB_APP_URL", WEB_APP_URL)
        button = InlineKeyboardButton(
            text="Создать заявку",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
        keyboard = InlineKeyboardMarkup.from_button(button)
        text = (
            "Номер успешно подтверждён!\n" +
            "Перейдите на форму создания заявки"
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=keyboard,
        )


def save_user_chat_id(chat_id, phone_number):
    debug_print("save_user_chat_id", "start")
    api_url = (
        os.getenv("DJANGO_APP_API_ROOT_URL") +
        f"api/user/{chat_id}/"
    )
    debug_print("api_url", api_url)
    try:
        stripped_phone_number = "".join(
            char for char in phone_number if char in string.digits
        )
        debug_print("stripped_phone_number", stripped_phone_number)
        response = requests.post(
            api_url,
            {"phone_number": stripped_phone_number},
            timeout=10,
        )
        if not response.status_code == 200:
            raise Exception()
    except Exception:
        raise Exception()


async def handle_phone_number(update, context):
    if update.message.contact:
        try:
            save_user_chat_id(
                update.effective_chat.id,
                update.message.contact.phone_number,
            )
            WEB_APP_URL = os.getenv(
                "DOMAIN_APP_URL") + "/?phone={}".format(update.message.contact.phone_number)

            button = InlineKeyboardButton(
                text="Создать заявку",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
            keyboard = InlineKeyboardMarkup.from_button(button)
            text = (
                "Номер успешно подтверждён!\n" +
                "Перейдите на форму создания заявки"
            )
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=text,
                reply_markup=keyboard,
            )
        except Exception:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Не удалось подтвердить номер.",
            )


def get_user_applications(chat_id):
    api_url = (
        os.getenv("DJANGO_APP_API_ROOT_URL") +
        "api/loan-application?telegram_chat_id={}".format(chat_id)
    )
    debug_print("api_url", api_url)
    user_applications = []
    try:
        response = requests.get(api_url, timeout=10)
        if response.json():
            user_applications = response.json()
            debug_print("user_applications", user_applications)
    except:
        pass
    return user_applications


async def status(update, context):
    chat_id = update.effective_chat.id
    user_applications = get_user_applications(chat_id)
    status_list = []
    print(user_applications)
    if user_applications:
        status_list = []
        for i, status in enumerate(user_applications, start=1):
            mess = ""
            mess += f"Номер заявки: {random.randint(100000, 999999)}\n"
            mess += f"Дата заявки {status['createdAt'].split('T')[0]}\n"
            mess += f"Тип - открытие счета\n"
            mess += f"Компания:\n"
            mess += f"    - Имя: {status['companyName']}\n"
            mess += f"    - ИНН: {status['inn']}\n"
            mess += f"    - ОГРН: {random.randint(100000, 999999)}\n"
            if status['status'] == 'under_review':
                mess += f"Cтатус заявки - На рассмотрении\n"
            elif status['status'] == 'declined':
                mess += f"Cтатус заявки - Отклонена\n"
            elif status['status'] == 'approved':
                mess += f"Cтатус заявки - Одобрена\n"
            elif status['status'] == 'update':
                mess += f"Cтатус заявки - Доработка заявки\n"
            mess += (f"Номер счета: {random.randint(100000, 999999)} \n" if 'На рассмотрении' ==
                     status["status"] or "Доработка заявки" else '\n')
            mess += (f"Валюта счета: RUB\n " if 'На рассмотрении' ==
                     status["status"] or "Доработка заявки" else '\n')
            mess += (f"Дата открытия {date.today().strftime('%Y-%m-%d')}\n" if 'На рассмотрении' ==
                     status["status"] or "Доработка заявки" else '\n')
            mess += (f"Статус: Зарезервирован\n" if 'На рассмотрении' ==
                     status["status"] or "Доработка заявки" else '\n')
            status_list.append(mess)

        text = "\n\n".join(status_list)
    else:
        text = "Заявок не найдено."
    await context.bot.send_message(
        chat_id=chat_id,
        text=text,
    )


async def handle_custom_start(update, context):
    print(update.message.text)
    print("Отлавливаем кастом старт")
    print(update.effective_chat.id)
    if (update.message.text).lower() == 'старт' or (update.message.text).lower() == 'start':
        text = (
            "Официальный бот Банка «Ренессанс Кредит» для открытия расчетного счета" +
            "\n\n" +
            "/start начать работу с ботом\n" +
            "/apply подать заявку на РКО\n" +
            "/status узнать статус заявок\n" +
            "/chat связаться с поддержкой банка"
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
        )
    print(update.message.text)
    print("Отлавливаем кастом старт")
    if (update.message.text).lower() == 'статус' or (update.message.text).lower() == 'status':
        chat_id = update.effective_chat.id
        user_applications = get_user_applications(chat_id)
        status_list = []
        if user_applications:
            status_list = [
                (
                    f"Номер заявки: {status['id']}\n" +
                    f"Дата заявки {status['createdAt']}\n" +
                    f"Тип - открытие счета\n" +
                    f"Компания:\n" +
                    f"    - Имя: {status['companyName']}\n" +
                    f"    - ИНН: {status['inn']}\n" +
                    f"    - ОГРН: {random.randint(100000, 999999)}\n" +
                    f"Cтатус заявки - {status['status']}\n" +
                    (f"Номер счета: {random.randint(100000, 999999)} \n" if 'На рассмотрении' == status["status"] or "Доработка заявки" else '\n') +
                    (f"Валюта счета: RUB\n " if 'На рассмотрении' == status["status"] or "Доработка заявки" else '\n') +
                    (f"Дата открытия {datetime.now()}\n" if 'На рассмотрении' == status["status"] or "Доработка заявки" else '\n') +
                    (f"Статус: Зарезервирован\n" if 'На рассмотрении' ==
                     status["status"] or "Доработка заявки" else '\n')
                )
                for i, status in enumerate(user_applications, start=1)
            ]
            text = "\n\n".join(status_list)
        else:
            text = "Заявок не найдено."
        await context.bot.send_message(
            chat_id=chat_id,
            text=text,
        )


def run_bot():
    api_token = os.getenv('TELEGRAM_BOT_API_TOKEN')
    application = ApplicationBuilder().token(api_token).build()

    custom_start_handler = MessageHandler(
        filters.TEXT & (~filters.COMMAND), handle_custom_start)

    start_handler = CommandHandler('start', start)
    apply_handler = CommandHandler('apply', apply)
    status_handler = CommandHandler('status', status)
    chat_handler = CommandHandler('chat', chat)
    phone_number_handler = TypeHandler(Update, handle_phone_number)

    application.add_handler(custom_start_handler)

    application.add_handler(start_handler)
    application.add_handler(apply_handler)
    application.add_handler(status_handler)
    application.add_handler(chat_handler)
    application.add_handler(phone_number_handler)

    application.run_polling()


if __name__ == '__main__':
    run_bot()
