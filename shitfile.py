from pyriodic import DatetimesJob
from pyriodic import Scheduler
import datetime
from loader import dp,db,bot
day = datetime.datetime.today().weekday()
async def sending_7am():
    print("Sent")
    f = await db.select_pas()
    for i in range(len(f)):
        newstr = str(f[i]).replace("<Record id_tg=", "").replace(">", "")
        us = await (db.select_shedules('1MDA7', day))
        await bot.send_message(newstr, us)
schedul = Scheduler()

schedul.add_job(DatetimesJob(sending_7am, interval="daily", when="11:42:00 pm"))

schedul.start()