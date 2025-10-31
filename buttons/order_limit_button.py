from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

order_limit_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="+"),
            InlineKeyboardButton(text="0"),
            InlineKeyboardButton(text="-")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
