import asyncio

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = ('6879795290:AAFYEVliuXQ37OBqrU6c9gscF4EZIS4HYaA')

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_hadler(message: Message):
    await message.answer(f'Hello {message}')

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
