from aiogram.dispatcher.filters import Text
from keyboard.inlinegroup import group
from loader import dp


@dp.message_handler(Text('Студент'))
async def student(message):
    await message.answer('Привет падаван \n какая у тебя группа?', reply_markup= group)
