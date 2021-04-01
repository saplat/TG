import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, db
from keyboard import select
from loader import dp, db
from utils.misc import rate_limit


@rate_limit(limit = 30)
@dp.message_handler(CommandStart())
async def start(message):
    try:
        await db.create()
        await message.answer(f'Привет {message.from_user.full_name}\n'
                                 f'Укажи свой статус', reply_markup=select)

    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(id_tg=message.from_user.id)
        await message.answer(f'{message.from_user.full_name} ты уже зарегистрирован')
