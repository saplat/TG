import telebot
import config
import datetime
import sqlite3
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

callmas = ['1MDA7', '1MDA9', '1MD16', '1MDA14', '1MDP12', '1MD14']
th = ['чернышевстаниславандреевич', ]

plan = {0 : "🎓🎓🎓🎓математика, ТМП, БД",
        1 : "🎓🎓🎓🎓Логика",
        2 : "🎓🎓🎓🎓Физра",
        3 : "🎓🎓🎓🎓История",
        4 : "🎓🎓🎓🎓Философия",
        5 :"🎓🎓🎓🎓Инфа",
        6 : "🎓🎓🎓🎓Физика,математика, ТМП, БД"}



def get_day():#Получаем номер деня недели(0-пн...6-вс) return int
    return datetime.datetime.today().weekday()



def get_group(message):#Создание inline кнопок и получение группы пользователя

    markup  = types.InlineKeyboardMarkup()

    group1 = types.InlineKeyboardButton("1МДА7", callback_data='1MDA7')
    group2 = types.InlineKeyboardButton("1МДА9", callback_data='1MDA9')
    group3 = types.InlineKeyboardButton("1МД16", callback_data='1MD16')
    group4 = types.InlineKeyboardButton("1МДА14", callback_data='1MDA14')
    group5 = types.InlineKeyboardButton("1МДП12", callback_data='1MDP12')
    group6 = types.InlineKeyboardButton("1МД14", callback_data='1MD14')
    group7 = types.InlineKeyboardButton("1МДП1", callback_data='1MDP1')
    group8 = types.InlineKeyboardButton("1МДП10", callback_data='1MDP10')
    group9 = types.InlineKeyboardButton("1МДА29с", callback_data='1MDA29')
    group10 = types.InlineKeyboardButton("1МД4", callback_data='1MD4')
    group11 = types.InlineKeyboardButton("1МД8", callback_data='1MD8')
    group12 = types.InlineKeyboardButton("1МД5", callback_data='1MD5')
    group13 = types.InlineKeyboardButton("1МД15", callback_data='1MD15')
    group14 = types.InlineKeyboardButton("1МД17", callback_data='1MD17')
    group15 = types.InlineKeyboardButton("1МД2", callback_data='1MD2')
    group16 = types.InlineKeyboardButton("1МД19", callback_data='1MD19')
    group17 = types.InlineKeyboardButton("1МД20", callback_data='1MD20')
    group18 = types.InlineKeyboardButton("2МДП1", callback_data='2MDP1')
    group19 = types.InlineKeyboardButton("2МД8", callback_data='2MDP8')

    markup.add(group1,group2,group3,group4,group5,group6,group7,group8,group9,group10,group11,group12,group13,group14,group15,group16,group17,group18,group19)

    bot.send_message(message.chat.id,"Какая у тебя группа?", reply_markup= markup)

def menu(message):

    markup   = types.ReplyKeyboardMarkup(resize_keyboard = True)
    today    = types.KeyboardButton("Сегодня")
    tomorrow = types.KeyboardButton("Завтра")
    week     = types.KeyboardButton("Неделя")
    options  = types.KeyboardButton("Опции")

    markup.add(today,tomorrow,week, options)

    bot.send_message(message.chat.id,"Это меню" ,reply_markup = markup)




@bot.message_handler(commands = ['start', 'help'])
def welcome(message):#Приветствие и получение информации ученик/преподаватель

    stik = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stik)

    markup     = types.ReplyKeyboardMarkup(resize_keyboard = True,one_time_keyboard=True)
    apprentice = types.KeyboardButton("Ученик")
    teacher    = types.KeyboardButton("Преподаватель")

    markup.add(apprentice, teacher)

    bot.send_message(message.chat.id, 'Представься', reply_markup = markup)



@bot.message_handler(content_types = ['text'])
def get_text_messages(message):


    if message.text == "Ученик":

        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id ,'Привет падаван',reply_markup=a)

        get_group(message)

    elif message.text == "Преподаватель":

        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Здравствуй джедай\nНапиши своё ФИО", reply_markup=a)

    elif message.text.replace(' ', '').lower() in th:

        bot.send_message(message.chat.id, "Nice")
        menu(message)

    elif message.text == "Сегодня":

        day = get_day()
        bot.send_message(message.chat.id, plan[day])

    elif message.text == "Завтра":

        day = get_day()
        if day == 6:
            day = 0
        else:
            day+=1
        bot.send_message(message.chat.id, plan[day])

    elif message.text == "Неделя":
        for i in range(7):
            bot.send_message(message.chat.id, plan[i])

    else:

        bot.send_message(message.chat.id, "WTF")



@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):

    try:

        if call.message:

            if call.data in callmas:

                menu(call.message)



            else:

                bot.send_message(call.message.chat.id,'SAD')

            bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text="Отлично")

    except Exception as e:

        print(repr(e))



@bot.message_handler(content_types = ['sticker'])
def conti(message):

    stik = open('sticker1.webp', 'rb')
    bot.send_sticker(message.chat.id, stik)

bot.polling(none_stop=True)




