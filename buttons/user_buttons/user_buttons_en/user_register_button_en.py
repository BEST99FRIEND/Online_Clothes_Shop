from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_button_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Send phone number", request_contact=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

location_button_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Send location", request_location=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

gender_button_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚹 Male"),
            KeyboardButton(text="🚺 Female"),
            KeyboardButton(text="🧒 Child")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
