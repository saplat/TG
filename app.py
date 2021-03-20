from aiogram import types
from aiogram import executor
from loader import dp
from handlers.users.start import start



executor.start_polling(dp, skip_updates=True)