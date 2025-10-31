from aiogram import Router, F
from aiogram.types import Message

register_router_uz = Router()

@register_router_uz.message(F.text == "📝 Ro‘yxatdan o‘tish")
async def register_uz(m:Message):
    text = ""
    await m.answer(text=text)