from aiogram import Router, F
from aiogram.types import Message
from buttons.buttons_ru import menu_buttons_kb_ru_2

menu_router_ru = Router()

@menu_router_ru.message(F.text == "🍽️ Меню")
async def menu_f_ru(m: Message):
    text = (
        "🍽️ **Главное меню**\n\n"
        "Здесь вы можете выбрать различные категории одежды 👕🧢🧥\n"
        "Выберите понравившийся раздел и оформите заказ 🛍️\n"
        "Каждый товар — это гарантия качества и стиля ✨"
    )
    await m.answer(text=text, reply_markup=menu_buttons_kb_ru_2)
