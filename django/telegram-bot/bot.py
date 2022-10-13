import os

import requests
import string

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    TypeHandler
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



def is_chat_id_confirmed(chat_id):
    api_url = (
        os.getenv("DJANGO_APP_API_ROOT_URL") +
        f"user/{chat_id}/"
    )
    try:
        response = requests.get(api_url, timeout=10, verify=False)
        if response.status_code == 200:
            return True
    except Exception as error:
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
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


async def chat(update, context):
    text = (
        "Контакт-центр Банка “Ренессанс Кредит”\n" +
        "8-800-200-0-981(круглосуточно, бесплатно по России)"
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


async def apply(update, context):
    if not is_chat_id_confirmed(update.effective_chat.id):
        print(update.effective_chat)
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
        WEB_APP_URL = "https://loan-application-bot.baraba.sh/"
        button = InlineKeyboardButton(
            text="Создать заявку",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
        keyboard = InlineKeyboardMarkup.from_button(button)
        text = (
                "Номер успешно подтверждён!\n" +
                "Перейдите на форму создания заявки"
        )
        print(update.effective_chat)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=keyboard,
        )
    
    # text = (
    #     "Оформите заявку чтобы получить потребительский кредит " +
    #     "наличными на выгодных условиях с низкой ставкой."
    # )
    # await context.bot.send_message(
    #     chat_id=update.effective_chat.id,
    #     text=text,
    #     reply_markup=keyboard,
    # )

def save_user_chat_id(chat_id, phone_number):
    api_url = (
        os.getenv("DJANGO_APP_API_ROOT_URL") +
        f"user/{chat_id}/"
    )
    print(phone_number)
    try:
        stripped_phone_number = "".join(
            char for char in phone_number if char in string.digits
        )
        formatted_phone_number = f"+{stripped_phone_number}"
        response = requests.post(
            api_url,
            {"phone_number": formatted_phone_number},
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
            print(update.message.contact.phone_number)
            WEB_APP_URL = "https://loan-application-bot.baraba.sh/?phone={}".format(update.message.contact.phone_number)
            print(WEB_APP_URL)
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
        "http://django:8000/"+
        "loan-application/{}".format(chat_id)
    )
    user_applications = []
    try:   
        response = requests.get(api_url, timeout=10)
        print("Отправили респонс")
        print(response)
        if response.json():
            user_applications = response.json()
            print(user_applications)
    except:
        print("ошибка подключения")
        pass
    return user_applications


async def status(update, context):
    chat_id = update.effective_chat.id
    print(chat_id)
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
        parse_mode='Markdown',
    )


def run_bot():
    api_token = os.getenv('TELEGRAM_BOT_API_TOKEN')
    application = ApplicationBuilder().token(api_token).build()

    start_handler = CommandHandler('start', start)
    apply_handler = CommandHandler('apply', apply)
    status_handler = CommandHandler('status', status)
    chat_handler = CommandHandler('chat', chat)
    phone_number_handler = TypeHandler(Update, handle_phone_number)
    application.add_handler(start_handler)
    application.add_handler(apply_handler)
    application.add_handler(status_handler)
    application.add_handler(chat_handler)
    application.add_handler(phone_number_handler)

    application.run_polling()


if __name__ == '__main__':
    run_bot()
