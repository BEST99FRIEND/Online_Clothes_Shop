from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Telefon raqamni yuborish", request_contact=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

location_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Joylashuvni yuborish", request_location=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

gender_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚹 Erkak"),
            KeyboardButton(text="🚺 Ayol"),
            KeyboardButton(text="🧒 Yosh bola")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
