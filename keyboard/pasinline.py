from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

pasget = InlineKeyboardMarkup()
time1 = InlineKeyboardButton("🕘8:00", callback_data="8")
time2 = InlineKeyboardButton("🕞10:00", callback_data="10")
time3 = InlineKeyboardButton("🕔12:00", callback_data="8")
back2 = InlineKeyboardButton("⬅назад", callback_data="back2")
pasget.add(time1,time2,time3,back2)

helpback =InlineKeyboardMarkup()
back3 = InlineKeyboardButton("⬅назад", callback_data="back2")
helpback.add(back3)