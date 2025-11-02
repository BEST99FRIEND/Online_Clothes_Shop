from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, FSInputFile

start_admin_router = Router()

@start_admin_router.message(Command("admin"))
async def start_admin(m:Message)