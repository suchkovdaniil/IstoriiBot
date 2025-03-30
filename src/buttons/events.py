from config_reader import dp
from aiogram import F
from aiogram.types import CallbackQuery, FSInputFile

from keyboards import back_to_menu


@dp.callback_query(F.data == 'events')
async def events(callback: CallbackQuery):
    await callback.message.answer_photo(FSInputFile('pictures/nov_events.jpg'),
                                        caption='Подробнее о мероприятиях вы можете узнать в нашем телеграм-канале:\n'
                                                '<a href="https://t.me/istorii_coffee"><b>ИСТОРИИ</b></a>', reply_markup=back_to_menu)
