from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from TG.loader import dp,bot


@dp.message_handler(CommandStart())
async def start(message):
    await message.ansewer(f'привет! {message.from_user.full_name}')





