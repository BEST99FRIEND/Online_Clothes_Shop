from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from buttons import menu_buttons_kb_uz

start_router_uz = Router()

@start_router_uz.message(F.text == "🇺🇿 O‘zbek tili")
async def start_uz(m:Message):
    text = '''
👋 Assalomu alaykum!
👗 “StyleZone” kiyim-kechak do‘konining rasmiy botiga xush kelibsiz!

Bu yerda siz:
🛍️ Moda uslubidagi kiyimlar,
👕 Har kungi qulay liboslar,
👠 Ajoyib aksessuarlar va boshqalarni topasiz!

📦 Buyurtma berish juda oson — sizga yoqqan mahsulotni tanlang, o‘lcham va rangni belgilang, va bot sizga tezda yordam beradi!

💬 Boshlash uchun quyidagi menyudan kerakli bo‘limni tanlang 👇'''
    photoo = FSInputFile("image/logo.jpg")
    await m.answer_photo(photo=photoo, caption=text, reply_markup=menu_buttons_kb_uz)
