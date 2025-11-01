from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

counter_router_en = Router()

# User-specific counters
user_counters = {}


def counter_inline_keyboard(value: int):
    """Create inline buttons"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="➖", callback_data="decrease"),
            InlineKeyboardButton(text=f"{value}", callback_data="none"),
            InlineKeyboardButton(text="➕", callback_data="increase")
        ],
        [
            InlineKeyboardButton(text="🛒 Add to cart", callback_data="add_to_cart"),
        ],
        [
            InlineKeyboardButton(text="❌ Cancel", callback_data="cancel")
        ]
    ])
    return keyboard


@counter_router_en.message(F.text == "🧮 Counter")
async def send_counter(m: Message):
    """Start counter"""
    user_counters[m.from_user.id] = 0
    await m.answer(
        text="🧮 Counter started:",
        reply_markup=counter_inline_keyboard(0)
    )


@counter_router_en.callback_query(F.data.in_(["increase", "decrease"]))
async def handle_counter(callback: CallbackQuery):
    """Handle ➕ and ➖ buttons"""
    user_id = callback.from_user.id
    value = user_counters.get(user_id, 0)

    if callback.data == "increase":
        value += 1
    elif callback.data == "decrease" and value > 0:
        value -= 1

    user_counters[user_id] = value

    await callback.message.edit_reply_markup(reply_markup=counter_inline_keyboard(value))
    await callback.answer()


@counter_router_en.callback_query(F.data == "add_to_cart")
async def add_to_cart(callback: CallbackQuery):
    """🛒 Add to cart"""
    value = user_counters.get(callback.from_user.id, 0)
    await callback.answer(f"{value} items added to cart ✅", show_alert=True)


@counter_router_en.callback_query(F.data == "cancel")
async def cancel_counter(callback: CallbackQuery):
    """❌ Cancel"""
    user_counters.pop(callback.from_user.id, None)
    await callback.message.delete()
    await callback.answer("Counter closed ❌")
