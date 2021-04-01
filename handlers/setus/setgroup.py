import asyncpg
from aiogram import types
from keyboard.gomenu import menu_go
from loader import dp,bot,db

@dp.callback_query_handler()
async def set_group(call):
   user = await db.add_user(
      fname = call.message.from_user.full_name,
      id_tg =  call.message.from_user.id,
      groupus = call.data
   )
   await call.answer(f"Ты в группе {call.data}", show_alert=True)
   await call.message.edit_reply_markup()
