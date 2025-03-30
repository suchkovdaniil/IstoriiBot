from aiogram import types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.types import CallbackQuery, FSInputFile

from text import menu_text
from keyboards import main_menu_keyboard, back_to_menu
from config_reader import bot, dp


@dp.message(Command("menu"))
async def contacts(msg: types.Message):
    await msg.answer(menu_text, reply_markup=main_menu_keyboard)


@dp.callback_query(F.data == 'menu')
async def menu_func(callback: CallbackQuery):
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer_photo(FSInputFile('pictures/меню_истории.jpeg'), reply_markup=back_to_menu)


@dp.callback_query(F.data == 'back')
async def bck(callback: CallbackQuery):
    await callback.message.answer(f"Выбери, что тебя интересует:", reply_markup=main_menu_keyboard)
