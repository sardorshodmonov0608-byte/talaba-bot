from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Assalomu alaykum!\n\nTalabalar uchun bot ishga tushdi."
    )

@dp.message()
async def echo_handler(message: Message):
    await message.answer("Bot ishlayapti ✅")

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
