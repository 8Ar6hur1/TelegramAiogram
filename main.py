# logging
import logging

# aiogram
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router

# asyncio
import asyncio

# os
import os

# dotenv
from dotenv import load_dotenv

# project: admin, user
import admin, user
from admin import admin_route, send_help
from user import user_route, send_help


logging.basicConfig(level=logging.INFO)

load_dotenv()

# API токен телеграм боту
API_TOKEN = os.getenv('API_TOKEN')

# Перевіряємо чи є у нас файл .env 
if API_TOKEN is None:
    raise ValueError('API_TOKEN is not set in the environment or .env file')

admin_ids_str = os.getenv('ADMIN_IDS', '')

# Переконуємось, що ADMIN_IDS коректно завантажено
if admin_ids_str:
    # завантажуємо ADMIN_IDS з файлу .env і перетворюємо його на список цілих чисел.
    ADMIN_IDS = list(map(int, os.getenv('ADMIN_IDS').split(',')))
else:
    ADMIN_IDS = []

# Перевірка чи правильно завантажується ADMIN_IDS з .env
print(f'Loaded ADMIN_IDS: {ADMIN_IDS}')


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(admin_route)
dp.include_router(user_route)


# перевіряємо, чи є user_id в списку адміністраторів, який зберігається в ADMIN_IDS
def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


# перевіряємо яке повідомлення кидати користувачу на команду 'start'
@dp.message(CommandStart())
async def start_bot(message: Message):
    user_id = message.from_user.id
    print(f'Your telegram_id: {user_id}')
    if is_admin(user_id):
        await admin.send_start(message)
    else:
        await user.send_start(message)


# перевіряємо яке повідомлення кидати користувачу на команду 'help'
@dp.message(Command('help'))
async def send_help(message: Message):
    user_id = message.from_user.id
    if is_admin(user_id):
        await admin.send_help(message)
    else:
        await user.send_help(message)




async def main():
    print('Starting bot...')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
