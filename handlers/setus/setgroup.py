import asyncpg
from aiogram import types

from keyboard import menuset
from keyboard.gomenu import stepmenu
from loader import dp,bot,db
from states import Menu

@dp.callback_query_handler()
async def set_group(call):
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
   await call.message.answer("Перейти в меню",reply_markup = stepmenu)
   await Menu.swapmenu.set()



