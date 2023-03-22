from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

group = InlineKeyboardMarkup()

group1 = InlineKeyboardButton("1МДА7", callback_data='1MDA7')
group2 = InlineKeyboardButton("1МДА9", callback_data='1MDA9')
group3 = InlineKeyboardButton("1МД16", callback_data='1MD16')
group4 = InlineKeyboardButton("1МДА14", callback_data='1MDA14')
group5 = InlineKeyboardButton("1МДП12", callback_data='1MDP12')
group6 = InlineKeyboardButton("1МД14", callback_data='1MD14')
group7 = InlineKeyboardButton("1МДП1", callback_data='1MDP1')
group8 = InlineKeyboardButton("1МДП10", callback_data='1MDP10')
group9 = InlineKeyboardButton("1МДА29", callback_data='1MDA29')
group10 = InlineKeyboardButton("1МД4", callback_data='1MD4')
group11 = InlineKeyboardButton("1МД8", callback_data='1MD8')
group12 = InlineKeyboardButton("1МД5", callback_data='1MD5')
group13 = InlineKeyboardButton("1МД15", callback_data='1MD15')
group14 = InlineKeyboardButton("1МД17", callback_data='1MD17')
group15 = InlineKeyboardButton("1МД2", callback_data='1MD2')
group16 = InlineKeyboardButton("1МД19", callback_data='1MD19')
group17 = InlineKeyboardButton("1МД20", callback_data='1MD20')
group18 = InlineKeyboardButton("2МДП1", callback_data='2MDP1')
group19 = InlineKeyboardButton("2МД8", callback_data='2MDP8')
group20 = InlineKeyboardButton("2МДА7", callback_data='2MDA7')
group21 = InlineKeyboardButton("2МДА9", callback_data='2MDA9')
group22 = InlineKeyboardButton("2МД16", callback_data='2MD16')
group23 = InlineKeyboardButton("3МДА7", callback_data='3MDA7')
group24 = InlineKeyboardButton("3МДА9", callback_data='3MDA9')
group25 = InlineKeyboardButton("4МДА7", callback_data='4MDA7')
group26 = InlineKeyboardButton("4МДА9", callback_data='4MDA9')

group.add(group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12,
           group13, group14, group15, group16, group17, group18, group19, group20, group21, group22,
           group23, group24, group25, group26)