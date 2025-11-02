from aiogram import Router, F
from aiogram.types import Message,FSInputFile
from buttons.user_buttons.user_buttons_en import menu_buttons_kb_en_2

menu_router_en = Router()

@menu_router_en.message(F.text == "🛍️ Menu")
async def menu_f_en(m: Message):
    text = (
        "🛍️ **Main Menu**\n\n"
        "Here you can explore different clothing categories 👕🧢🧥\n"
        "Choose your favorite section and place your order 🛍️\n"
        "Every product represents quality and style ✨"
    )
    photoo = FSInputFile("image/menu_shop.jpg")
    await m.answer_photo(photo=photoo, caption=text, reply_markup=menu_buttons_kb_en_2)
