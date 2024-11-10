import asyncio
import logging
import json

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, CallbackQuery, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from config_reader import config
from text import greeting
from keyboards import start_keyboard, main_menu_keyboard, back_to_menu, vacancy, back_from_vacancy

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


class Feedback(StatesGroup):
    feedback = State()


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

        await msg.answer(f"Ваш номер успешно получен!", reply_markup=ReplyKeyboardRemove())
    else:
        await msg.answer("Вы уже отправили свой номер!", reply_markup=ReplyKeyboardRemove())
    await msg.answer(f"Выберите, что вас интересует:", reply_markup=main_menu_keyboard)


# Menu buttons implementation
@dp.callback_query(F.data == 'menu')
async def menu_func(callback: CallbackQuery):
    # await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await callback.message.answer_photo(FSInputFile('pictures/меню_истории.jpeg'), reply_markup=back_to_menu)


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
    await message.answer('Спасибо за обратную связь!', reply_markup=main_menu_keyboard)
    with open('users_data.json', 'r') as file:
        data = json.load(file)
        feedback_to_chat = f"{data[str(message.from_user.id)]['username']}\n" \
                           f"{data[str(message.from_user.id)]['phone_number']}\n\n" \
                           f"{message.text}"
        await bot.send_message(-1002340321528, feedback_to_chat, message_thread_id=2)
    await state.clear()


@dp.callback_query(F.data == 'events')
async def events(callback: CallbackQuery):
    await callback.message.answer_photo(FSInputFile('pictures/nov_events.jpg'),
                                        caption='Подробнее о мероприятиях вы можете узнать в нашем телеграм-канале:\n'
                                                'https://t.me/istorii_coffee', reply_markup=back_to_menu)


@dp.callback_query(F.data == 'vacancy')
async def vacancy_func(callback: CallbackQuery):
    await callback.message.answer('На данный момент доступны следующие вакансии:', reply_markup=vacancy)


@dp.callback_query(F.data == 'back_from_vacancy')
async def vacancy_func(callback: CallbackQuery):
    await callback.message.answer('На данный момент доступны следующие вакансии:', reply_markup=vacancy)


@dp.callback_query(F.data == 'barista')
async def vacancy_func(callback: CallbackQuery):
    await callback.message.answer('*Описание вакансии бариста*', reply_markup=back_from_vacancy)


@dp.callback_query(F.data == 'back')
async def bck(callback: CallbackQuery):
    await callback.message.answer(f"Выбери, что тебя интересует:", reply_markup=main_menu_keyboard)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
