import json

from config_reader import dp, bot
from aiogram import F
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import main_menu_keyboard, back_to_menu


class Feedback(StatesGroup):
    feedback = State()


@dp.callback_query(F.data == 'feedback')
async def feedback_func(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Feedback.feedback)
    await callback.message.answer(
        'Вы можете оставить обратную связь и мы обязательно исправим то, что вам не понравилось!',
        reply_markup=back_to_menu)


@dp.message(Feedback.feedback)
async def feedback_text_func(message: types.Message, state: FSMContext):
    await state.update_data(feedback=message.text)
    await state.set_state(Feedback.feedback)
    await message.answer('<b>Спасибо за обратную связь!</b>', reply_markup=main_menu_keyboard)
    with open('users_data.json', 'r') as file:
        data = json.load(file)
        feedback_to_chat = f"<b>Username</b>: {data[str(message.from_user.id)]['username']}\n" \
                           f"<b>Номер телефона</b>: {data[str(message.from_user.id)]['phone_number']}\n\n" \
                           f"{message.text}"
        await bot.send_message(-1002340321528, feedback_to_chat, message_thread_id=2)
    await state.clear()