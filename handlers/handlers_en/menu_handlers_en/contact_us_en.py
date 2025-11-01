from aiogram import Router, F
from aiogram.types import Message

contact_us_router_en = Router()

@contact_us_router_en.message(F.text == "☎️ Contact Us")
async def contact_f_en(m:Message):
    text = ""
    await m.answer(text=text)