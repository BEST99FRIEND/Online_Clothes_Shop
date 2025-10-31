from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message
from buttons import lan_buttons

start_router = Router()

@start_router.message(CommandStart())
async def start(m:Message):
    text = '''🇺🇿 O‘zbekcha:

🌐 Iltimos, quyidagi tillardan birini tanlang:
🇺🇿 O‘zbek tili
🇷🇺 Rus tili
🇬🇧 Ingliz tili

🇷🇺 Русский:

🌐 Пожалуйста, выберите один из следующих языков:
🇷🇺 Русский язык
🇺🇿 Узбекский язык
🇬🇧 Английский язык

🇬🇧 English:

🌐 Please select one of the following languages:
🇬🇧 English
🇺🇿 Uzbek
🇷🇺 Russian'''
    await m.answer(text=text,reply_markup=lan_buttons)