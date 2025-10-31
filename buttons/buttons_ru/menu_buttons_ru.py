from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons_kb_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍽️ Меню"), KeyboardButton(text="📦 Мои заказы"), KeyboardButton(text="☎️ Связаться с нами")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
