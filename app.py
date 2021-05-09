from aiogram import types
from aiogram import executor
from loader import dp,db,bot
from handlers.users.start import start
from handlers.setus.student import student
from handlers.more import trash
#from handlers.users.menu import setp_menu
import asyncio
import datetime

day = datetime.datetime.today().weekday()


    # f = await db.select_pas()
    # for i in range(len(f)):
    #     newstr = str(f[i]).replace("<Record id_tg=", "").replace(">", "")
    #     us = await (db.select_shedules('1MDA7', day))
    #     await bot.send_message(newstr, us)



executor.start_polling(dp, skip_updates=False)
