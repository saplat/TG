import asyncpg
from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp,bot,db
from keyboard.gomenu import menu


@dp.callback_query_handler()
async def set_group(call):

   if call.data == "week":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer(text='Неделя ебать',reply_markup = menu)

   elif call.data == "today":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer("сегодня", reply_markup=menu)

   elif call.data == "tomorrow":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer("завтра", reply_markup=menu)

   elif call.data == "setting":
      await call.message.edit_reply_markup()
      await call.message.delete()
      await call.message.answer("настройки", reply_markup=menu)

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
      await call.message.answer("Меню", reply_markup = menu)


   # await call.message.answer("Перейти в меню",reply_markup = stepmenu)
   # await Menu.swapmenu.set()



