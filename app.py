from aiogram import types
from aiogram import executor
from loader import dp
from handlers.users.start import start

async def starti(dp):
    await start(dp)

executor.start_polling(dp, skip_updates=True)