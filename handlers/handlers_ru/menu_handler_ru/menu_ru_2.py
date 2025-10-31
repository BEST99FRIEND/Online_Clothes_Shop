from aiogram import Router, F
from aiogram.types import Message

menu_2_router_ru = Router()

@menu_2_router_ru.message(F.text == "🧢 Кепка")
async def menu_cap_f_ru(m: Message):
    text = (
        "🧢 **Раздел кепок**\n\n"
        "Здесь вы найдете стильные и качественные кепки! 😎\n"
        "Доступны разные цвета, бренды и размеры.\n"
        "Выберите и подчеркните свой стиль! 👌"
    )
    await m.answer(text=text, parse_mode="Markdown")

@menu_2_router_ru.message(F.text == "👕 Футболка")
async def menu_shirt_f_ru(m: Message):
    text = (
        "👕 **Раздел футболок**\n\n"
        "В этом разделе вы найдете удобные летние футболки ☀️\n"
        "Сделаны из 100% хлопка, в разных цветах и модных дизайнах!\n"
        "Выберите ту, которая вам по душе! 🛍️"
    )
    await m.answer(text=text, parse_mode="Markdown")

@menu_2_router_ru.message(F.text == "🧥 Куртка")
async def menu_jacket_f_ru(m: Message):
    text = (
        "🧥 **Раздел курток**\n\n"
        "Теплые, прочные и стильные куртки ждут вас! ❄️\n"
        "Они защитят вас от дождя, холода и ветра.\n"
        "Ознакомьтесь с нашей последней коллекцией 👇"
    )
    await m.answer(text=text, parse_mode="Markdown")

@menu_2_router_ru.message(F.text == "🤵 Костюм")
async def menu_suit_f_ru(m: Message):
    text = (
        "🤵 **Раздел костюмов**\n\n"
        "Идеальный выбор для деловых встреч, свадеб и мероприятий! 👔\n"
        "Высококачественные ткани, классические и современные модели.\n"
        "Подчеркните свою элегантность и уверенность ✨"
    )
    await m.answer(text=text, parse_mode="Markdown")

@menu_2_router_ru.message(F.text == "👖 Штаны")
async def menu_trousers_f_ru(m: Message):
    text = (
        "👖 **Раздел штанов**\n\n"
        "От повседневных моделей до удобных офисных брюк 👌\n"
        "Доступны разные стили, размеры и цвета.\n"
        "Комфорт и стиль в одном месте!"
    )
    await m.answer(text=text, parse_mode="Markdown")

@menu_2_router_ru.message(F.text == "👟 Обувь")
async def menu_shoes_f_ru(m: Message):
    text = (
        "👟 **Раздел обуви**\n\n"
        "Качественная, удобная и модная обувь 👣\n"
        "Спортивная, повседневная или классическая — всё здесь!\n"
        "Сделайте каждый шаг уверенным 🚶‍♂️"
    )
    await m.answer(text=text, parse_mode="Markdown")

@menu_2_router_ru.message(F.text == "👜 Сумки")
async def menu_bags_f_ru(m: Message):
    text = (
        "👜 **Раздел сумок**\n\n"
        "Удобные, стильные и прочные сумки на каждый день 🎒\n"
        "Есть варианты для мужчин, женщин и детей.\n"
        "Совместите функциональность и моду 💼"
    )
    await m.answer(text=text, parse_mode="Markdown")

@menu_2_router_ru.message(F.text == "👓 Аксессуары")
async def menu_accessories_f_ru(m: Message):
    text = (
        "👓 **Раздел аксессуаров**\n\n"
        "Самые стильные аксессуары, которые дополнят ваш образ ✨\n"
        "Часы, ремни, очки и многое другое!\n"
        "Маленькие детали создают большое впечатление 💎"
    )
    await m.answer(text=text, parse_mode="Markdown")
