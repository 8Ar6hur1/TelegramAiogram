from aiogram import Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

user_route = Router()

@user_route.message(Command('start'))
async def send_start(message: Message):
    await message.answer(f'Привіт звичайний {message.from_user.first_name}')