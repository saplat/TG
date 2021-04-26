from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menuth = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📌Неделя", callback_data= "weekth"),
            InlineKeyboardButton(text="📌Сегодня", callback_data= "todayth"),
            InlineKeyboardButton(text="📌Завтра", callback_data= "tomorrowth")
        ],
        [
            InlineKeyboardButton(text="⚙Настройка", callback_data= "settingth")
        ]
    ])
settth = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text="✉Подписка", callback_data="passth"),
        InlineKeyboardButton(text="🗿Помощь", callback_data="helpth"),
    ],
    [
        InlineKeyboardButton(text="⬅Назад", callback_data="backth")
    ]
])

helpbackth =InlineKeyboardMarkup()
back3 = InlineKeyboardButton("⬅назад", callback_data="back2th")
helpbackth.add(back3)