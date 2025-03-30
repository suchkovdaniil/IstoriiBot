# 66

import json

from config_reader import dp, bot
from aiogram import F
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import main_menu_keyboard, back_to_menu
from text import cooperation_text


class Cooperation(StatesGroup):
    cooperation = State()


@dp.callback_query(F.data == 'cooperation')
async def feedback_func(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Cooperation.cooperation)
    await callback.message.answer(
        cooperation_text,
        reply_markup=back_to_menu)


@dp.message(Cooperation.cooperation)
async def feedback_text_func(message: types.Message, state: FSMContext):
    await state.update_data(cooperation=message.text)
    await state.set_state(Cooperation.cooperation)
    await message.answer('<b>Мы обязательно свяжемся с вами в ближайшее время!</b>', reply_markup=main_menu_keyboard)
    with open('users_data.json', 'r') as file:
        data = json.load(file)
        cooperation_to_chat = f"<b>Username</b>: {data[str(message.from_user.id)]['username']}\n" \
                           f"<b>Номер телефона</b>: {data[str(message.from_user.id)]['phone_number']}\n\n" \
                           f"{message.text}"
        await bot.send_message(-1002340321528, cooperation_to_chat, message_thread_id=66)
    await state.clear()