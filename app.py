from aiogram import types
from aiogram import executor
from loader import dp,db,bot
from handlers.users.start import start
from handlers.setus.student import student
from handlers.more import trash
#from handlers.users.menu import setp_menu
import asyncio
import aioschedule
import datetime

day = datetime.datetime.today().weekday()


async def noon_print():
    s = await db.count_userspas()
    f = await db.select_pas()
    for i in range(s):
        newstr = str(f[i]).replace("<Record id_tg=", "")
        newstr1 = newstr.replace(">", "")
        us = await (db.select_shedules('1MDA7', day))
        await bot.send_message(newstr1, us)

async def scheduler():
    aioschedule.every().day.at("00:07").do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):
    asyncio.create_task(scheduler())

executor.start_polling(dp, skip_updates=False,on_startup=on_startup)
