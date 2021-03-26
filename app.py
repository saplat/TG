from aiogram import types
from aiogram import executor
from loader import dp,db
from handlers.users.start import start
from handlers.setus.student import student
from handlers.more import trash
#from handlers.users.menu import setp_menu

executor.start_polling(dp, skip_updates=True)
