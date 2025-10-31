from aiogram import Router, F
from aiogram.types import Message,FSInputFile

menu_2_router_uz = Router()

@menu_2_router_uz.message(F.text == "🧢 Kepka")
async def menu_cap_f_uz(m: Message):
    text = (
        "🧢 **Kepkalar bo‘limi**\n\n"
        "Bu yerda siz zamonaviy va sifatli kepkalarni topasiz! 😎\n"
        "Turli ranglar, brendlar va o‘lchamlar mavjud.\n"
        "Tanlang va uslubingizni to‘liq qiling! 👌"
    )
    photoo = FSInputFile("image/cap.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_uz.message(F.text == "👕 Futbolka")
async def menu_shirt_f_uz(m: Message):
    text = (
        "👕 **Futbolkalar bo‘limi**\n\n"
        "Bu bo‘limda siz yozgi qulay futbolkalarni topasiz ☀️\n"
        "100% paxtadan tikilgan, rang-barang va zamonaviy dizaynlar bilan!\n"
        "O‘zingizga yoqqanini tanlang! 🛍️"
    )
    photoo = FSInputFile("image/T-shirt.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_uz.message(F.text == "🧥 Kurtka")
async def menu_jacket_f_uz(m: Message):
    text = (
        "🧥 **Kurtkalar bo‘limi**\n\n"
        "Issiq, bardoshli va uslubli kurtkalar sizni kutmoqda! ❄️\n"
        "Yomg‘ir, sovuq va shamolda sizni himoya qiladi.\n"
        "Eng so‘nggi kolleksiyamizni ko‘rib chiqing 👇"
    )
    photoo = FSInputFile("image/jacket.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_uz.message(F.text == "🤵 Kostyum")
async def menu_suit_f_uz(m: Message):
    text = (
        "🤵 **Kostyumlar bo‘limi**\n\n"
        "Rasmiy uchrashuvlar, to‘ylar va tadbirlar uchun mukammal tanlov! 👔\n"
        "Yuqori sifatli matolar, klassik va zamonaviy dizaynlar.\n"
        "Sizni haqiqiy gentlemanga aylantiradi ✨"
    )
    photoo = FSInputFile("image/suit.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_uz.message(F.text == "👖 Shim")
async def menu_trousers_f_uz(m: Message):
    text = (
        "👖 **Shimlar bo‘limi**\n\n"
        "Kundalik kiyimdan tortib, ofis uchun qulay shimlargacha 👌\n"
        "Turli uslublar, o‘lchamlar va ranglarda mavjud.\n"
        "Qulaylik va stil bir joyda!"
    )
    photoo = FSInputFile("image/trousers.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_uz.message(F.text == "👟 Oyoq kiyim")
async def menu_shoes_f_uz(m: Message):
    text = (
        "👟 **Oyoq kiyimlar bo‘limi**\n\n"
        "Sifatli, qulay va modaga mos oyoq kiyimlar 👣\n"
        "Sport, kundalik yoki klassik uslub — barchasi shu yerda!\n"
        "Yangi juftlik bilan yurishingizga ishonch qo‘shing 🚶‍♂️"
    )
    photoo = FSInputFile("image/shoes.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_uz.message(F.text == "👜 Sumkalar")
async def menu_bags_f_uz(m: Message):
    text = (
        "👜 **Sumkalar bo‘limi**\n\n"
        "Har kuni uchun qulay, zamonaviy va mustahkam sumkalar 🎒\n"
        "Ayollar, erkaklar va bolalar uchun turli variantlar mavjud.\n"
        "Stil va funksionallikni birlashtiring 💼"
    )
    photoo = FSInputFile("image/bags.jpg")
    await m.answer_photo(photo=photoo ,caption=text)

@menu_2_router_uz.message(F.text == "👓 Aksessuarlar")
async def menu_accessories_f_uz(m: Message):
    text = (
        "👓 **Aksessuarlar bo‘limi**\n\n"
        "Sizning obrazingizni to‘ldiradigan eng zamonaviy aksessuarlar ✨\n"
        "Soatlar, kamarlar, ko‘zoynaklar va boshqalar mavjud!\n"
        "Kichik detallar — katta ta’sir yaratadi 💎"
    )
    photoo = FSInputFile("image/accessories.jpg")
    await m.answer_photo(photo=photoo ,caption=text)
