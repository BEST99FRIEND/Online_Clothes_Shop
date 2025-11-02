from aiogram import Router, F
from aiogram.types import Message

my_orders_router_en = Router()

@my_orders_router_en.message(F.text == "📦 My Orders")
async def my_orders_f_en(m:Message):
    text = ""
    await m.answer(text=text)