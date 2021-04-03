from loader import dp
from aiogram import types
from states import Menu
from keyboard.gomenu import menuset


@dp.message_handler(state= Menu.swapmenu)
async def setp_menu(message, state):
    answer = message.text
    await state.update_data(answe = answer)
    await message.answer('Ты в меню',reply_markup =menuset)
    await state.finish()