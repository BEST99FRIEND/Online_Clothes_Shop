from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

season_buttons_kb_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌸 Bahor"),
            KeyboardButton(text="☀️ Yoz")
        ],
        [
            KeyboardButton(text="🍂 Kuz"),
            KeyboardButton(text="❄️ Qish")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
