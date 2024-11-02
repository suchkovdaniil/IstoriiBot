import asyncio
import logging
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from text import greeting
from aiogram.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, FSInputFile
from aiogram import F

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()


@dp.message(Command("start"))
async def contacts(msg: types.Message):
    keyboard_kb = [[KeyboardButton(text='Share Contact', request_contact=True)]]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_kb, resize_keyboard=True)
    await msg.answer(greeting, reply_markup=keyboard)


@dp.message(F.contact)
async def contacts(msg: types.Message):
    #запись данных о пользователе
    with open('users_data.json', 'r') as file:
        data = json.load(file)
        if msg.contact.user_id not in data:
            data[msg.contact.user_id] = {'username': msg.chat.username,
                                         'phone_number': msg.contact.phone_number,
                                         'first_name': msg.contact.first_name,
                                         'last_name': msg.contact.last_name}

    with open('users_data.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    await msg.answer(f"Твой номер успешно получен!", reply_markup=ReplyKeyboardRemove())


# Запуск процесса поллинга новых апдейтов
async def main():
    #прототип отправки файла с данными пользователей в наш чат в телеграме
    # fl = FSInputFile(path='/Users/essmloy/PycharmProjects/IstoriiBot/users_data.json')
    # await bot.send_document(-1002345827747, fl)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())