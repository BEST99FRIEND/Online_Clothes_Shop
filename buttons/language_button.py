from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lan_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O‘zbek tili"),
            KeyboardButton(text="🇷🇺 Русский язык"),
            KeyboardButton(text="🇬🇧 English language")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
