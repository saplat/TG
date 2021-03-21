from loader import dp,bot

@dp.callback_query_handler()
async def set_group(call):
   await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ты в группе")
