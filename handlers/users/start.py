from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from keyboard import select


@dp.message_handler(CommandStart())
async def start(message):
    await message.answer(f'Привет {message.from_user.full_name}\n'
                         f'Укажи свой статус', reply_markup=select)

