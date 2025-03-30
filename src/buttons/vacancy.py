import json

from config_reader import *
from aiogram import F
from aiogram.types import CallbackQuery

from text import barista_vacancy, respond_answer
from keyboards import main_menu_keyboard, vacancy, in_vacancy


@dp.callback_query(F.data == 'vacancy')
async def vacancy_func(callback: CallbackQuery):
    await callback.message.answer('На данный момент доступны следующие вакансии:', reply_markup=vacancy)


@dp.callback_query(F.data == 'back_from_vacancy')
async def vacancy_func(callback: CallbackQuery):
    await callback.message.answer('На данный момент доступны следующие вакансии:', reply_markup=vacancy)


@dp.callback_query(F.data == 'barista')
async def vacancy_func(callback: CallbackQuery):
    await callback.message.answer(barista_vacancy, reply_markup=in_vacancy)


@dp.callback_query(F.data == 'respond_barista')
async def vacancy_func(callback: CallbackQuery):
    await callback.message.answer(respond_answer, reply_markup=main_menu_keyboard)
    with open('users_data.json', 'r') as file:
        data = json.load(file)
        respond_to_chat = f"<b>ОТКЛИК</b>\n<b>ВАКАНСИЯ:</b> Бариста\n\n" \
                          f"<b>Username</b>: {data[str(callback.from_user.id)]['username']}\n" \
                          f"<b>Номер телефона</b>: {data[str(callback.from_user.id)]['phone_number']}\n\n"
        await bot.send_message(-1002340321528, text=respond_to_chat, message_thread_id=45)
