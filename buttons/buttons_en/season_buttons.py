from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

season_buttons_kb_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌸 Spring"),
            KeyboardButton(text="☀️ Summer")
        ],
        [
            KeyboardButton(text="🍂 Autumn"),
            KeyboardButton(text="❄️ Winter")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
