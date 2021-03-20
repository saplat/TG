from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot


# @dp.message_handler(CommandStart())
# async def start(message):
# await message.ansewer(f'привет {message.from_user.full_name}')
@dp.message_handler(text="/start")
async def start(message: types.Message):
    chat_id = message.chat.id
    text = "Хай ма бой"
    await bot.send_message(chat_id=chat_id, text=text)
