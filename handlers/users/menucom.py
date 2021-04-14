from keyboard import menu
from loader import dp
from aiogram.dispatcher.filters.builtin import Command
from aiogram import types


@dp.message_handler(Command('menu'))
async def menuhand(message):
    a = types.ReplyKeyboardRemove()
    await message.answer('Привет падаван', reply_markup=a)
    await message.answer(
        f"{message.from_user.full_name}, здесь ты можешь получить расписание на сегодня, завтра и неделю\n"
        f"Для подписки на рассылку рассписания и сброса группы перейди в настройки\n"
        f"Там еще помощь есть\n", reply_markup=menu)