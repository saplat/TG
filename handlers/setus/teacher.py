from loader import dp, db, bot
from aiogram.dispatcher.filters import Text
from aiogram import types

@dp.message_handler(Text('Преподаватель'))
async def student(message):
    a = types.ReplyKeyboardRemove()
    await message.answer('Привет джедай', reply_markup=a)
    send = await message.answer('Укажи своё ФИ')


    # @dp.message_handler()
    # def set_teacher(message):
    #     try:
    #         #user = await db.check_teacher(fname = message.text)
    #         #await message.answer('Hi')
    #     except:
    #         await message.answer('Ты не джедай. лох!')