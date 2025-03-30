from config_reader import dp
from aiogram import F
from aiogram.types import CallbackQuery, FSInputFile

from keyboards import back_to_menu
from text import events_text


@dp.callback_query(F.data == 'events')
async def events(callback: CallbackQuery):
    #await callback.message.answer_photo(FSInputFile('pictures/nov_events.jpg'),
    #                                    caption= reply_markup=back_to_menu)
    await callback.message.answer(text=events_text, reply_markup=back_to_menu)
