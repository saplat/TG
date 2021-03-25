from loader import dp,bot
from aiogram import types
import random

stup = ["Шизоид?", "Читать умеешь?", "Чел ты...", "Ща в мут полетишь", "Клоун?!",
        "В дурку его ребята","УУУ сука", "Ясно беды с башкой"]
@dp.message_handler(content_types= types.ContentTypes.ANY)
async def pix(message):
    stik =  open('sticker1.webp', 'rb')
    await bot.send_sticker(message.chat.id, stik)
    await message.answer(stup[random.randint(0,len(stup)-1)])