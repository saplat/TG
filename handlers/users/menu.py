from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text

#
# @dp.callback_query_handler(callback_data.filter("week"))
# async def weeks(call):
#     await call.message.answer("неделя")