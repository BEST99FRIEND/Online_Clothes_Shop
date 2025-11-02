from aiogram import Router, F
from aiogram.types import Message

contact_us_router_ru = Router()

@contact_us_router_ru.message(F.text == "☎️ Связаться с нами")
async def contact_f_ru(m:Message):
    text = ""
    await m.answer(text=text)