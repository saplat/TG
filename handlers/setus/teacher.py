from loader import dp
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text('Преподаватель'))
async def student(message):
    await message.answer('Привет джедай')
