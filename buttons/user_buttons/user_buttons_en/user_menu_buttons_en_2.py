from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_buttons_kb_en_2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧢 Cap"), KeyboardButton(text="👕 T-Shirt")],
        [KeyboardButton(text="🧥 Jacket"), KeyboardButton(text="🤵 Suit")],
        [KeyboardButton(text="👖 Trousers"), KeyboardButton(text="👟 Shoes")],
        [KeyboardButton(text="👜 Bags"), KeyboardButton(text="👓 Accessories")],
        [KeyboardButton(text="🏠 Main Menu")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
