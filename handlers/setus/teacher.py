from loader import dp, db, bot
import asyncpg
from aiogram.dispatcher.filters import Text
from aiogram import types
from states import Teacher_data
from keyboard.gomenu import menu


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
    try:
        user = await db.check_teacher(str(answer))
        if user == 'SELECT 1':
            await message.answer(f"Привет {answer}")
            await state.finish()
            await message.answer("Меню", reply_markup=menu)
        else:
            await message.answer('лох')
    except:
        await message.answer(f"ЛОХ")






    # try:
    #     user = await db.check_teacher(fname='g')
    #     await message.answer('А ты хорош')
    # except:
    #     await message.answer('Ты не джедай. лох!')