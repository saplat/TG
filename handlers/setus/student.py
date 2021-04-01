from aiogram.dispatcher.filters import Text
from keyboard.inlinegroup import group
from loader import dp, db
from aiogram import types


@dp.message_handler(Text('Студент'))
async def student(message):
    a = types.ReplyKeyboardRemove()
    await message.answer('Привет падаван', reply_markup=a)
    await message.answer('Какая у тебя группа?', reply_markup= group)
