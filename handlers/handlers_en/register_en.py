from aiogram import Router, F
from aiogram.types import Message

register_router_uz = Router()

@register_router_uz.message(F.text == "📝 Register")
async def register_en(m:Message):
    text = ""
    await m.answer(text=text)