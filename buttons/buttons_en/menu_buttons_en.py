from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons_kb_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍️ Menu"), KeyboardButton(text="📦 My Orders"), KeyboardButton(text="☎️ Contact Us")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
