from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

counter_router_ru = Router()

# Значения счётчиков для каждого пользователя
user_counters = {}


def counter_inline_keyboard(value: int):
    """Создание inline-клавиатуры"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="➖", callback_data="decrease"),
            InlineKeyboardButton(text=f"{value}", callback_data="none"),
            InlineKeyboardButton(text="➕", callback_data="increase")
        ],
        [
            InlineKeyboardButton(text="🛒 Добавить в корзину", callback_data="add_to_cart"),
        ],
        [
            InlineKeyboardButton(text="❌ Отменить", callback_data="cancel")
        ]
    ])
    return keyboard


@counter_router_ru.message(F.text == "🧮 Счётчик")
async def send_counter(m: Message):
    """Начать счётчик"""
    user_counters[m.from_user.id] = 0
    await m.answer(
        text="🧮 Счётчик запущен:",
        reply_markup=counter_inline_keyboard(0)
    )


@counter_router_ru.callback_query(F.data.in_(["increase", "decrease"]))
async def handle_counter(callback: CallbackQuery):
    """Обработка кнопок ➕ и ➖"""
    user_id = callback.from_user.id
    value = user_counters.get(user_id, 0)

    if callback.data == "increase":
        value += 1
    elif callback.data == "decrease" and value > 0:
        value -= 1

    user_counters[user_id] = value

    await callback.message.edit_reply_markup(reply_markup=counter_inline_keyboard(value))
    await callback.answer()


@counter_router_ru.callback_query(F.data == "add_to_cart")
async def add_to_cart(callback: CallbackQuery):
    """🛒 Добавить в корзину"""
    value = user_counters.get(callback.from_user.id, 0)
    await callback.answer(f"{value} товаров добавлено в корзину ✅", show_alert=True)


@counter_router_ru.callback_query(F.data == "cancel")
async def cancel_counter(callback: CallbackQuery):
    """❌ Отменить"""
    user_counters.pop(callback.from_user.id, None)
    await callback.message.delete()
    await callback.answer("Счётчик закрыт ❌")
