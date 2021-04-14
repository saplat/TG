import asyncio
import asyncpg
from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboard import pasget, helpback
from loader import dp,bot,db
from keyboard.gomenu import menu, sett
import datetime

loop = asyncio.get_event_loop()
day = datetime.datetime.today().weekday()


@dp.callback_query_handler()
async def set_group(call):

   if call.data == "week":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(text='Неделя ебать',reply_markup = menu)

   elif call.data == "today":
      await call.message.edit_reply_markup()
      await call.message.delete()
      gr = await db.select_group(call.from_user.id)
      us = await (db.select_shedules(gr,day))
      await call.message.answer(us, reply_markup=menu)

   elif call.data == "tomorrow":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer("завтра", reply_markup=menu)

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
      delay = 10
      async def overpas():
         await call.message.answer('сегодня', reply_markup = menu)
         when_to_call = loop.time() + delay
         loop.call_at(when_to_call, my_callback)

      def my_callback():
         asyncio.ensure_future(overpas())

      my_callback()

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




