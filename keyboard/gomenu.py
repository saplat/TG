from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

#set_callbackk = CallbackData("item_name")
menu = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Неделя", callback_data= "week"),
            InlineKeyboardButton(text="Сегодня", callback_data= "today"),
            InlineKeyboardButton(text="Завтра", callback_data= "tomorrow")
        ],
        [
            InlineKeyboardButton(text="Настройка", callback_data= "setting")
        ]
    ])
# today = InlineKeyboardButton(text="Сегодня", callback_data=set_callbackk.new(item_name = "week"))
# tomorrow = InlineKeyboardButton(text="Завтра", callback_data=set_callbackk.new(item_name = "week"))
# setting = InlineKeyboardButton(text="Настройик", callback_data=set_callbackk.new(item_name = "week"))
# menu.add(week,today,tomorrow,setting)