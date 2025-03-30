import json

from config_reader import dp
from aiogram import F
from aiogram import types
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, Message

from text import greeting, success_get_contact, repeat_get_contact, menu_text
from keyboards import start_keyboard, main_menu_keyboard


@dp.message(Command("start"))
async def contacts(msg: types.Message):
    await msg.answer(greeting,
                     reply_markup=ReplyKeyboardMarkup(keyboard=start_keyboard, resize_keyboard=True))


@dp.message(F.contact)
async def contacts(msg: types.Message):
    with open('users_data.json', 'r') as file:
        data = json.load(file)

    user_id = str(msg.contact.user_id)
    if user_id not in data:
        data[user_id] = {
            'username': msg.chat.username,
            'phone_number': msg.contact.phone_number,
            'first_name': msg.contact.first_name,
            'last_name': msg.contact.last_name
        }

        with open('users_data.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        await msg.answer(success_get_contact, reply_markup=ReplyKeyboardRemove())
    else:
        await msg.answer(repeat_get_contact, reply_markup=ReplyKeyboardRemove())
    await msg.answer(menu_text, reply_markup=main_menu_keyboard)
