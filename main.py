from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import ( Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup,
                            InlineKeyboardButton, CallbackQuery)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext 
from environs import Env
import asyncio
import logging
from handlers import ( start_router, start_router_uz,
                       start_router_ru, start_router_en )
from routers import setup_routers

import os

dp = Dispatcher()
bot_token = os.getenv("TOKEN")

async def main():
    bot = Bot(token=bot_token)
    dp.include_router(setup_routers())
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

