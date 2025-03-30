import asyncio
import logging

from config_reader import *
from aiogram.fsm.state import StatesGroup, State

from buttons.menu import *
from buttons.start import *
from buttons.feedback import *
from buttons.events import *
from buttons.vacancy import *
from buttons.cooperation import *


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
