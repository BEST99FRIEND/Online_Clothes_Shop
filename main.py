from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import ( Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup,
                            InlineKeyboardButton, CallbackQuery)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext 
from environs import Env
import asyncio
import logging
from routers import setup_routers

import os

dp = Dispatcher()
bot_token = os.getenv("TOKEN")

async def main():
    bot = Bot(token=bot_token)
    main_router = setup_routers()
    dp.include_router(main_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

