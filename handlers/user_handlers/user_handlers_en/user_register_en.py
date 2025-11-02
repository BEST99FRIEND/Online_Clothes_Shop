from aiogram import Router, F
from aiogram.types import Message
from buttons.user_buttons.user_buttons_en.user_register_button_en import phone_button_en, location_button_en, gender_button_en

register_router_en = Router()


@register_router_en.message(F.text == "📝 Register")
async def register_en(m: Message):
    text = (
        "📝 Let's start the registration process!\n\n"
        "Please follow these steps:\n"
        "1️⃣ Send your full name.\n"
        "2️⃣ Share your phone number using the button below.\n"
        "3️⃣ Send your location.\n"
        "4️⃣ Then choose your gender.\n\n"
        "Let's begin! Please type your full name 👇"
    )
    await m.answer(text=text)


# 1️⃣ Full name
@register_router_en.message(F.text.regexp(r"^[A-Za-z\s']+$"))
async def get_full_name_en(m: Message):
    await m.answer(
        "📱 Great! Now please send your phone number 👇",
        reply_markup=phone_button_en
    )


# 2️⃣ Phone number
@register_router_en.message(F.contact)
async def get_phone_number_en(m: Message):
    await m.answer(
        "📍 Thank you! Now please share your location 👇",
        reply_markup=location_button_en
    )


# 3️⃣ Location
@register_router_en.message(F.location)
async def get_location_en(m: Message):
    await m.answer(
        "🧍‍♂️ Final step! Please select your gender 👇",
        reply_markup=gender_button_en
    )


# 4️⃣ Gender
@register_router_en.message(F.text.in_(["🚹 Male", "🚺 Female", "🧒 Child"]))
async def get_gender_en(m: Message):
    await m.answer(
        "✅ Registration completed successfully!\n\n"
        "Now you can enjoy all the features of our shop 🎉",
    )
