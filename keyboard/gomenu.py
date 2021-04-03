from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuset = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Сегодня'), KeyboardButton(text='Завтра'),KeyboardButton(text='Неделя')
        ],
        [
            KeyboardButton(text='Настройки')
        ]
    ],
    resize_keyboard=True, one_time_keyboard = True
)

stepmenu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="меню")]], resize_keyboard=True, one_time_keyboard=True
)