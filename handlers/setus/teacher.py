from loader import dp, db, bot
import asyncpg
from aiogram.dispatcher.filters import Text
from aiogram import types
from states import Teacher_data

@dp.message_handler(Text('Преподаватель'))
async def teacher(message):
    a = types.ReplyKeyboardRemove()
    await message.answer('Привет джедай', reply_markup=a)
    await message.answer('Укажи своё ФИ')

    await Teacher_data.naming.set()


@dp.message_handler(state=Teacher_data.naming)
async def get_teacher(message, state):
    answer = message.text
    await state.update_data(answe = answer)
    await message.answer(f"Привет {answer}")
    user = await db.check_teacher(answer)
    await state.finish()




    # try:
    #     user = await db.check_teacher(fname='g')
    #     await message.answer('А ты хорош')
    # except:
    #     await message.answer('Ты не джедай. лох!')