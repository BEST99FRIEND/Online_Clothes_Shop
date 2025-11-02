from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from buttons import menu_buttons_kb_en

start_router_en = Router()

@start_router_en.message(F.text == "🇬🇧 English language")
async def start_en(m:Message):
    text = '''
👋 Hello!
👗 Welcome to the official “StyleZone” clothing store bot!

Here you can find:
🛍️ Trendy outfits,
👕 Comfortable everyday wear,
👠 Stylish accessories and much more!

📦 Placing an order is super easy — just choose the product you like, select the size and color, and the bot will guide you through the process!

💬 To get started, select the desired section from the menu below 👇'''
    photoo = FSInputFile("image/logo.jpg")
    await m.answer_photo(photo=photoo, caption=text, reply_markup=menu_buttons_kb_en)