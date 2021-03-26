from loader import dp
from aiogram.dispatcher.filters import Text
from aiogram import types

@dp.message_handler(Text('Преподаватель'))
async def student(message):
    a = types.ReplyKeyboardRemove()
    await message.answer('Привет джедай', reply_markup=a)
    await message.answer('Укажи своё ФИ')