from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Отправить номер телефона", request_contact=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

location_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍 Отправить локацию", request_location=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

gender_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚹 Мужчина"),
            KeyboardButton(text="🚺 Женщина"),
            KeyboardButton(text="🧒 Ребёнок")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
