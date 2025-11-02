from aiogram import Router, F
from aiogram.types import Message
from buttons.user_buttons.user_buttons_ru.user_register_button_ru import phone_button_ru, location_button_ru, gender_button_ru

register_router_ru = Router()


@register_router_ru.message(F.text == "📝 Регистрация")
async def register_ru(m: Message):
    text = (
        "📝 Начнем процесс регистрации!\n\n"
        "Пожалуйста, введите данные по шагам:\n"
        "1️⃣ Отправьте своё полное имя (Ф.И.О.).\n"
        "2️⃣ Поделитесь номером телефона, используя кнопку ниже.\n"
        "3️⃣ Отправьте свою локацию.\n"
        "4️⃣ Затем выберите свой пол.\n\n"
        "Начнём! Напишите своё Ф.И.О. 👇"
    )
    await m.answer(text=text)


# 1️⃣ Имя
@register_router_ru.message(F.text.regexp(r"^[A-Za-zА-Яа-яЁё\s']+$"))
async def get_full_name_ru(m: Message):
    await m.answer(
        "📱 Отлично! Теперь отправьте свой номер телефона 👇",
        reply_markup=phone_button_ru
    )


# 2️⃣ Телефон
@register_router_ru.message(F.contact)
async def get_phone_number_ru(m: Message):
    await m.answer(
        "📍 Спасибо! Теперь отправьте свою локацию 👇",
        reply_markup=location_button_ru
    )


# 3️⃣ Локация
@register_router_ru.message(F.location)
async def get_location_ru(m: Message):
    await m.answer(
        "🧍‍♂️ Последний шаг! Выберите свой пол 👇",
        reply_markup=gender_button_ru
    )


# 4️⃣ Пол
@register_router_ru.message(F.text.in_(["🚹 Мужчина", "🚺 Женщина", "🧒 Ребёнок"]))
async def get_gender_ru(m: Message):
    await m.answer(
        "✅ Регистрация успешно завершена!\n\n"
        "Теперь вы можете пользоваться всеми возможностями нашего магазина 🎉",
    )
