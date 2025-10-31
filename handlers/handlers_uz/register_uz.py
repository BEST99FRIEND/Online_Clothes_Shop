from aiogram import Router, F
from aiogram.types import Message
from buttons.buttons_uz.register_button_uz import phone_button_uz, location_button_uz, gender_button_uz

register_router_uz = Router()


@register_router_uz.message(F.text == "📝 Ro‘yxatdan o‘tish")
async def register_uz(m: Message):
    text = (
        "📝 Ro‘yxatdan o‘tish jarayonini boshlaymiz!\n\n"
        "Iltimos, quyidagi ma’lumotlarni ketma-ket kiriting:\n"
        "1️⃣ To‘liq ism-sharfingizni (F.I.Sh) yuboring.\n"
        "2️⃣ Telefon raqamingizni ulashish uchun tugmadan foydalaning.\n"
        "3️⃣ Joylashuvingizni yuboring.\n"
        "4️⃣ So‘ngra jinsingizni tanlang.\n\n"
        "Keling, boshlaymiz! Quyidagi maydonga F.I.Sh ni yozing 👇"
    )
    await m.answer(text=text)


# 1️⃣ Foydalanuvchi ism-sharfini yuborganda
@register_router_uz.message(F.text.regexp(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s']+$"))
async def get_full_name(m: Message):
    await m.answer(
        "📱 Ajoyib! Endi telefon raqamingizni yuboring 👇",
        reply_markup=phone_button_uz
    )


# 2️⃣ Foydalanuvchi telefon raqamini yuborganda
@register_router_uz.message(F.contact)
async def get_phone_number(m: Message):
    await m.answer(
        "📍 Rahmat! Endi lokatsiyangizni yuboring 👇",
        reply_markup=location_button_uz
    )


# 3️⃣ Foydalanuvchi lokatsiyasini yuborganda
@register_router_uz.message(F.location)
async def get_location(m: Message):
    await m.answer(
        "🧍‍♂️ So‘nggi qadam! Jinsingizni tanlang 👇",
        reply_markup=gender_button_uz
    )


# 4️⃣ Foydalanuvchi jinsni tanlaganda
@register_router_uz.message(F.text.in_(["🚹 Erkak", "🚺 Ayol", "🧒 Yosh bola"]))
async def get_gender(m: Message):
    await m.answer(
        "✅ Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi!\n\n"
        "Endi siz do‘konimizdagi barcha xizmatlardan foydalanishingiz mumkin 🎉",
    )
