from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

season_buttons_kb_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌸 Весна"),
            KeyboardButton(text="☀️ Лето")
        ],
        [
            KeyboardButton(text="🍂 Осень"),
            KeyboardButton(text="❄️ Зима")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
