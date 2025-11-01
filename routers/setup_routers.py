from aiogram import Router

# 🇺🇿 O'zbekcha routerlar
from handlers.handlers_uz import (
    start_router_uz, register_router_uz, menu_router_uz,
    menu_2_router_uz, contact_us_router_uz, my_orders_router_uz,
)



# 🇷🇺 Ruscha routerlar
from handlers.handlers_ru import (
    start_router_ru, register_router_ru, menu_router_ru,
    menu_2_router_ru, contact_us_router_ru, my_orders_router_ru
)

# 🇬🇧 Inglizcha routerlar
from handlers.handlers_en import (
    start_router_en, register_router_en, menu_router_en,
    menu_2_router_en, contact_us_router_en, my_orders_router_en
)


def setup_routers() -> Router:
    """
    Barcha tilga mos routerlarni birlashtiruvchi asosiy funksiya
    """
    main_router = Router()

    # 🇺🇿 Uzbekcha
    main_router.include_router(start_router_uz)
    main_router.include_router(register_router_uz)
    main_router.include_router(menu_router_uz)
    main_router.include_router(menu_2_router_uz)
    main_router.include_router(contact_us_router_uz)
    main_router.include_router(my_orders_router_uz)

    # 🇷🇺 Ruscha
    main_router.include_router(start_router_ru)
    main_router.include_router(register_router_ru)
    main_router.include_router(menu_router_ru)
    main_router.include_router(menu_2_router_ru)
    main_router.include_router(contact_us_router_ru)
    main_router.include_router(my_orders_router_ru)

    # 🇬🇧 Inglizcha
    main_router.include_router(start_router_en)
    main_router.include_router(register_router_en)
    main_router.include_router(menu_router_en)
    main_router.include_router(menu_2_router_en)
    main_router.include_router(contact_us_router_en)
    main_router.include_router(my_orders_router_en)

    return main_router
