from handlers.setus.teacher import list
import asyncio
import asyncpg
from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboard import pasget, helpback
from loader import dp,bot,db
from keyboard.gomenu import menu, sett
from keyboard import menuth, settth, helpbackth
import states
import datetime

loop = asyncio.get_event_loop()





@dp.callback_query_handler()
async def set_group(call):
   daydown = [i for i in range(1, 30, 2)]
   dayup = [i for i in range(2, 30, 2)]
   global dayend
   if datetime.datetime.now().isocalendar()[1] in daydown:
      dayend = 0
   elif datetime.datetime.now().isocalendar()[1] in dayup:
      dayend = 1
   global day
   day = datetime.datetime.today().weekday()
   global list
   gr = await db.select_group(call.from_user.id)

   if call.data == "week":
      await call.message.edit_reply_markup()
      await call.message.delete()

      for i in range(0,6):
         us = await (db.select_shedules(gr, i,dayend))
         await call.message.answer(us)

      us1 = await (db.select_shedules(gr, 6,dayend))
      await call.message.answer(us1,reply_markup = menu)

   elif call.data == "today":
      await call.message.edit_reply_markup()
      await call.message.delete()
      us = await (db.select_shedules(gr,day, dayend))
      await call.message.answer(us, reply_markup=menu)


   elif call.data == "tomorrow":
      await call.message.edit_reply_markup()
      await call.message.delete()
      if day != 6:
         us = await (db.select_shedules(gr, day+1,dayend))
      else:
         us = await (db.select_shedules(gr, 0,dayend))

      await call.message.answer(us, reply_markup=menu)

   elif call.data == "setting":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer("настройки", reply_markup=sett)

   elif call.data == "back":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(f"{call.from_user.full_name}, здесь ты можешь получить расписание на сегодня, завтра и неделю.\n"
                                f"Для подписки на рассылку рассписания и сброса группы перейди в настройки\n"
                                f"Там еще помощь есть\n", reply_markup = menu)

   elif call.data == 'pass':
        await call.message.edit_reply_markup()
        await call.message.delete()
        await call.message.answer("Выбери время для подписки", reply_markup=pasget)

   elif call.data == "back2":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(f"настройки", reply_markup=sett)

   elif call.data == "drop":
      try:
         await db.delete_users(call.from_user.id)
         await call.message.edit_reply_markup()
         await call.message.delete()
         await call.message.answer("Мем смешной, а пацанчик-то реально умер...", reply_markup=sett)
      except:
         await call.message.answer("дурак")

   elif call.data == 'help':
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(f"{call.from_user.full_name}, ну ты серьезно???\nТут всего 4 кнопки", reply_markup =helpback)

   elif call.data == "8":

      await call.message.edit_reply_markup()
      await call.message.delete()
      try:
         user = await db.add_pas(call.from_user.id)
         await call.message.answer("Ты подписался.", reply_markup=menu)
      except:
         await call.message.answer("Ты уже подписался.", reply_markup=menu)

   elif call.data == 'todayth':
      await call.message.answer('сегодня')
      await call.message.edit_reply_markup()
      await call.message.delete()
      fname = list[0]
      us = await (db.select_shedules_th(fname, day, dayend))
      await call.message.answer(us, reply_markup=menuth)

   elif call.data == 'tomorrowth':
      await call.message.answer('завтра')
      await call.message.edit_reply_markup()
      await call.message.delete()
      fname = list[0]
      try:
         us = await (db.select_shedules_th(fname, day+1, dayend))
         await call.message.answer(us, reply_markup=menuth)
      except:
         us = await (db.select_shedules_th(fname, 0, dayend))
         await call.message.answer(us, reply_markup=menuth)

   elif call.data == 'weekth':
      await call.message.answer('неделя')
      await call.message.edit_reply_markup()
      await call.message.delete()
      fname = list[0]
      for i in range(5):
         us = await (db.select_shedules_th(fname,i,dayend))
         await call.message.answer(us)
      us = await (db.select_shedules_th(fname, 5, dayend))
      await call.message.answer(us, reply_markup=menuth)

   elif call.data == 'settingth':
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer("настройки", reply_markup=settth)

   elif call.data == "backth":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(f"{call.from_user.full_name}, Здесь ты можешь получить расписание на сегодня, завтра и неделю.\n"
                                f"Для подписки на рассылку рассписания и сброса группы перейди в настройки\n"
                                f"Там еще помощь есть\n", reply_markup = menuth)
   elif call.data == "helpth":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(f"{call.from_user.full_name}, Ну ты серьезно???\nТут всего 4 кнопки",
                                reply_markup=helpbackth)
   elif call.data == "back2th":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(f"настройки", reply_markup=settth)

   elif call.data == "passth":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(f"скоро здесь что-то будет", reply_markup=menuth)

   else:
      try:
         user = await db.add_user(
            fname= call.from_user.full_name,
            id_tg =  call.from_user.id,
            groupus = call.data
         )
      except asyncpg.exceptions.UniqueViolationError:
         await call.answer(f'{call.from_user.full_name} ты уже зарегистрирован')

      await call.answer(f"Ты в группе {call.data}", show_alert=True)
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(f"{call.from_user.full_name}, здесь ты можешь получить расписание на сегодня, завтра и неделю\n"
                                f"Для подписки на рассылку рассписания и сброса группы перейди в настройки\n"
                                f"Там еще помощь есть\n", reply_markup = menu)