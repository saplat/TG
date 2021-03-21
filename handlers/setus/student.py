from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(Text('Студент'))
async def student(message):
    await message.answer('Привет падаван')
