from aiogram import Router, F
from aiogram.types import Message, FSInputFile

menu_2_router_en = Router()

@menu_2_router_en.message(F.text == "🧢 Cap")
async def menu_cap_f_en(m: Message):
    text = (
        "🧢 **Cap Section**\n\n"
        "Here you can find modern and high-quality caps! 😎\n"
        "Available in various colors, brands, and sizes.\n"
        "Choose one and complete your stylish look! 👌"
    )
    photoo = FSInputFile("image/cap.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_en.message(F.text == "👕 Shirt")
async def menu_shirt_f_en(m: Message):
    text = (
        "👕 **Shirt Section**\n\n"
        "Discover comfortable and breathable summer shirts ☀️\n"
        "Made from 100% cotton with trendy designs and bright colors!\n"
        "Pick the one that fits your mood! 🛍️"
    )
    photoo = FSInputFile("image/T-shirt.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_en.message(F.text == "🧥 Jacket")
async def menu_jacket_f_en(m: Message):
    text = (
        "🧥 **Jacket Section**\n\n"
        "Warm, durable, and stylish jackets are waiting for you! ❄️\n"
        "Perfect for rain, wind, or cold weather.\n"
        "Check out our latest collection 👇"
    )
    photoo = FSInputFile("image/jacket.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_en.message(F.text == "🤵 Suit")
async def menu_suit_f_en(m: Message):
    text = (
        "🤵 **Suit Section**\n\n"
        "A perfect choice for business meetings, weddings, or events! 👔\n"
        "Premium fabrics, classic and modern designs.\n"
        "Look sharp and confident ✨"
    )
    photoo = FSInputFile("image/suit.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_en.message(F.text == "👖 Trousers")
async def menu_trousers_f_en(m: Message):
    text = (
        "👖 **Trousers Section**\n\n"
        "From casual to formal — find the perfect pair for any occasion 👌\n"
        "Available in multiple styles, colors, and sizes.\n"
        "Comfort and style combined!"
    )
    photoo = FSInputFile("image/trousers.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_en.message(F.text == "👟 Shoes")
async def menu_shoes_f_en(m: Message):
    text = (
        "👟 **Shoes Section**\n\n"
        "High-quality, comfortable, and fashionable shoes 👣\n"
        "Sport, casual, or classic — everything you need is here!\n"
        "Step forward with confidence 🚶‍♂️"
    )
    photoo = FSInputFile("image/shoes.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_en.message(F.text == "👜 Bags")
async def menu_bags_f_en(m: Message):
    text = (
        "👜 **Bags Section**\n\n"
        "Durable, practical, and trendy bags for everyday use 🎒\n"
        "Options for men, women, and kids.\n"
        "Combine fashion with functionality 💼"
    )
    photoo = FSInputFile("image/bags.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_en.message(F.text == "👓 Accessories")
async def menu_accessories_f_en(m: Message):
    text = (
        "👓 **Accessories Section**\n\n"
        "Stylish accessories to complete your look ✨\n"
        "Watches, belts, glasses, and more!\n"
        "Small details make a big difference 💎"
    )
    photoo = FSInputFile("image/accessories.jpg")
    await m.answer_photo(photo=photoo ,caption=text)
