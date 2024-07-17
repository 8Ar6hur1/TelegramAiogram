# aiogram
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# asyncio
import asyncio

# os
import os

# dotenv
from dotenv import load_dotenv


load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

if API_TOKEN is None:
    raise ValueError('API_TOKEN is not set in the environment or .env file')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_hadler(message: Message):
    await message.answer(f'Hello {message.from_user.first_name}')


@dp.message()
async def send_help(message: Message):
    await message.reply('Hi! I\'m a bot!')




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
