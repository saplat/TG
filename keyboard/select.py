from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

select = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Студент')
        ],
        [
            KeyboardButton(text='Преподаватель')
        ]
    ],
    resize_keyboard=True
)