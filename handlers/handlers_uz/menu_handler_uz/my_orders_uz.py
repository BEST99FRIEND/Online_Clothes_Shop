from aiogram import Router, F
from aiogram.types import Message

my_orders_router_uz = Router()

@my_orders_router_uz.message(F.text == "📦 Buyurtmalarim")
async def my_orders_f_uz(m:Message):
    text = ""
    await m.answer(text=text)