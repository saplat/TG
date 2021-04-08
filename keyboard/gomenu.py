from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📌Неделя", callback_data= "week"),
            InlineKeyboardButton(text="📌Сегодня", callback_data= "today"),
            InlineKeyboardButton(text="📌Завтра", callback_data= "tomorrow")
        ],
        [
            InlineKeyboardButton(text="⚙Настройка", callback_data= "setting")
        ]
    ])
sett = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text="✉Подписка", callback_data="pass"),
        InlineKeyboardButton(text="🗿Помощь", callback_data="help"),
        InlineKeyboardButton(text="🔴Сброс", callback_data="drop")
    ],
    [
        InlineKeyboardButton(text="⬅Назад", callback_data="back")
    ]
])