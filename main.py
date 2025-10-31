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
from handlers import ( menu_router_uz, menu_router_ru, menu_router_en )
from handlers import ( menu_2_router_uz, menu_2_router_ru, menu_2_router_en )
import os

dp = Dispatcher()
bot_token = os.getenv("TOKEN")

async def main():
    bot = Bot(token=bot_token)
    dp.include_router(start_router)
    dp.include_router(start_router_uz)
    dp.include_router(start_router_ru)
    dp.include_router(start_router_en)
    dp.include_router(menu_router_uz)
    dp.include_router(menu_router_ru)
    dp.include_router(menu_router_en)
    dp.include_router(menu_2_router_uz)
    dp.include_router(menu_2_router_ru)
    dp.include_router(menu_2_router_en)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

