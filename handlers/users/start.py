import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboard import select
from loader import dp, db
from utils.misc import rate_limit

@rate_limit(limit = 30)
@dp.message_handler(CommandStart())
async def start(message):
    await db.create()
    await message.answer(f'Привет {message.from_user.full_name}\n'
                         f'Укажи свой статус', reply_markup=select)
