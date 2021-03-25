from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_go = InlineKeyboardMarkup()
step = InlineKeyboardButton("Перейти к меню", callback_data="step")
menu_go.add(step)