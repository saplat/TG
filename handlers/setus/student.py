from aiogram.dispatcher.filters import Text
from keyboard.inlinegroup import group
from loader import dp, db
from aiogram import types
from keyboard.gomenu import menu


@dp.message_handler(Text('Студент'))
async def student(message):
    a = types.ReplyKeyboardRemove()
    await message.answer('Приветствую, Падаван', reply_markup=a)
    check = await db.check_student(message.from_user.id)
    if check != 'SELECT 1':
        await message.answer('Какая у тебя группа?', reply_markup= group)
    else:
        await message.answer(
            f"{message.from_user.full_name}, здесь ты можешь получить расписание на сегодня, завтра и неделю\n"
            f"Для подписки на рассылку рассписания и сброса группы перейди в настройки\n"
            f"Там еще помощь есть\n", reply_markup=menu)
