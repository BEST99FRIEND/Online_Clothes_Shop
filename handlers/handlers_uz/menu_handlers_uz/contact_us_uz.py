from aiogram import Router, F
from aiogram.types import Message

contact_us_router_uz = Router()

@contact_us_router_uz.message(F.text == "☎️ Biz bilan bog‘lanish")
async def contact_f_uz(m:Message):
    text = ""
    await m.answer(text=text)