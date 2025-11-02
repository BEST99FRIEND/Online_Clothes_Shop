from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons_kb_ru_2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧢 Кепка"), KeyboardButton(text="👕 Футболка")],
        [KeyboardButton(text="🧥 Куртка"), KeyboardButton(text="🤵 Костюм")],
        [KeyboardButton(text="👖 Брюки"), KeyboardButton(text="👟 Обувь")],
        [KeyboardButton(text="👜 Сумки"), KeyboardButton(text="👓 Аксессуары")],
        [KeyboardButton(text="🏠 Главное меню")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
