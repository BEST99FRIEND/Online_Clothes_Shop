from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_button_kb_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="↩️ Back")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
