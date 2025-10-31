from aiogram import Router, F
from aiogram.types import Message

my_orders_router_ru = Router()

@my_orders_router_ru.message(F.text == "📦 Мои заказы")
async def my_orders_f_ru(m:Message):
    text = ""
    await m.answer(text=text)