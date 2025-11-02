from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons_kb_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍️ Menyu"), KeyboardButton(text="📦 Buyurtmalarim"), KeyboardButton(text="☎️ Biz bilan bog‘lanish")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
