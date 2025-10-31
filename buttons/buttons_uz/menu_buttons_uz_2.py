from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons_kb_uz_2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧢 Kepka"), KeyboardButton(text="👕 Futbolka")],
        [KeyboardButton(text="🧥 Kurtka"), KeyboardButton(text="🤵 Kostyum")],
        [KeyboardButton(text="👖 Shim"), KeyboardButton(text="👟 Oyoq kiyim")],
        [KeyboardButton(text="👜 Sumkalar"), KeyboardButton(text="👓 Aksessuarlar")],
        [KeyboardButton(text="🏠 Asosiy menyu")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
