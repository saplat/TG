from loader import dp, db, bot
import asyncpg
from aiogram.dispatcher.filters import Text
from aiogram import types
from states import Teacher_data
from keyboard import menuth
from keyboard import select


@dp.message_handler(Text('Преподаватель'))
async def teacher(message):
    a = types.ReplyKeyboardRemove()
    await message.answer('Джедай.', reply_markup=a)
    await message.answer('Укажи свою Фамилию и Имя.')

    await Teacher_data.naming.set()

list = []
@dp.message_handler(state=Teacher_data.naming)
async def get_teacher(message, state):
    answer = message.text
    answer.lower()
    global list
    list.append(answer)
    await state.update_data(answe = answer)
    user = await db.check_teacher(str(answer))

    if answer == '/start':
        await message.answer(f'Привет {message.from_user.full_name}.\n'
                             f'Укажи свой статус.', reply_markup=select)
        await state.finish()

    elif user != 'SELECT 0':
        await message.answer(f"Привет {answer}")
        await state.finish()
        await message.answer("Меню", reply_markup=menuth)
    else:
        await message.answer('Данный преподавтель не найден в базе данных')




    # try:
    #     user = await db.check_teacher(fname='g')
    #     await message.answer('А ты хорош')
    # except:
    #     await message.answer('Ты не джедай. лох!')
