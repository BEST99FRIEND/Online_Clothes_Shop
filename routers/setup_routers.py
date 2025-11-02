from aiogram import Router

# 🇺🇿 O'zbekcha routerlar
from handlers.handlers_uz.start_uz import start_router_uz
from handlers.handlers_uz.register_uz import register_router_uz
from handlers.handlers_uz.menu_handlers_uz.menu_uz import menu_router_uz
from handlers.handlers_uz.menu_handlers_uz.menu_2_uz import menu_2_router_uz
from handlers.handlers_uz.menu_handlers_uz.contact_us_uz import contact_us_router_uz
from handlers.handlers_uz.menu_handlers_uz.my_orders_uz import my_orders_router_uz

# 🇷🇺 Ruscha routerlar
from handlers.handlers_ru.start_ru import start_router_ru
from handlers.handlers_ru.register_ru import register_router_ru
from handlers.handlers_ru.menu_handlers_ru.menu_ru import menu_router_ru
from handlers.handlers_ru.menu_handlers_ru.menu_2_ru import menu_2_router_ru
from handlers.handlers_ru.menu_handlers_ru.contact_us_ru import contact_us_router_ru
from handlers.handlers_ru.menu_handlers_ru.my_orders_ru import my_orders_router_ru

# 🇬🇧 Inglizcha routerlar
from handlers.handlers_en.start_en import start_router_en
from handlers.handlers_en.register_en import register_router_en
from handlers.handlers_en.menu_handlers_en.menu_en import menu_router_en
from handlers.handlers_en.menu_handlers_en.menu_2_en import menu_2_router_en
from handlers.handlers_en.menu_handlers_en.contact_us_en import contact_us_router_en
from handlers.handlers_en.menu_handlers_en.my_orders_en import my_orders_router_en


def setup_routers() -> Router:
    """
    Barcha tilga mos routerlarni birlashtiruvchi asosiy funksiya
    """
    main_router = Router()

    # 🇺🇿 Uzbekcha
    for router in [
        start_router_uz, register_router_uz, menu_router_uz,
        menu_2_router_uz, contact_us_router_uz, my_orders_router_uz
    ]:
        main_router.include_router(router)

    # 🇷🇺 Ruscha
    for router in [
        start_router_ru, register_router_ru, menu_router_ru,
        menu_2_router_ru, contact_us_router_ru, my_orders_router_ru
    ]:
        main_router.include_router(router)

    # 🇬🇧 Inglizcha
    for router in [
        start_router_en, register_router_en, menu_router_en,
        menu_2_router_en, contact_us_router_en, my_orders_router_en
    ]:
        main_router.include_router(router)

    return main_router
