from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import Message
from buttons import menu_buttons_kb_ru

start_router_ru = Router()

@start_router_ru.message(F.text == "🇷🇺 Русский язык")
async def start_ru(m:Message):
    text = '''
👋 Здравствуйте!
👗 Добро пожаловать в официальный бот магазина одежды “StyleZone”!

Здесь вы найдете:
🛍️ Модные наряды,
👕 Удобную повседневную одежду,
👠 Стильные аксессуары и многое другое!

📦 Сделать заказ очень просто — выберите понравившийся товар, укажите размер и цвет, и бот быстро оформит ваш заказ!

💬 Чтобы начать, выберите нужный раздел из меню ниже 👇'''
    await m.answer(text=text,reply_markup=menu_buttons_kb_ru)