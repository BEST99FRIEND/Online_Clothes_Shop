from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from buttons.buttons_uz import menu_buttons_kb_uz_2

menu_router_uz = Router()

@menu_router_uz.message(F.text == "🛍️ Menyu")
async def menu_f_uz(m: Message):
    text = (
        "🛍️ **Asosiy menyu**\n\n"
        "Bu yerda siz turli kiyim-kechak toifalarini tanlashingiz mumkin 👕🧢🧥\n"
        "O‘zingizga yoqqan bo‘limni tanlang va buyurtma bering 🛍️\n"
        "Har bir mahsulot – sifat va uslub kafolati ✨"
    )
    photoo = FSInputFile("image/menu_shop.jpg")
    await m.answer_photo(photo=photoo, caption=text, reply_markup=menu_buttons_kb_uz_2)
