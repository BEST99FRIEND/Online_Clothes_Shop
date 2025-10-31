from aiogram import Router, F
from aiogram.types import Message

register_router_uz = Router()

@register_router_uz.message(F.text == "📝 Регистрация")
async def register_ru(m:Message):
    text = ""
    await m.answer(text=text)