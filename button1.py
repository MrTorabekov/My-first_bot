from aiogram import types


pythonn = [
    [types.KeyboardButton(text="0 dan o'rganish 📚"), types.KeyboardButton(text="Python va sun'iy intellekt 🦾")],
    [types.KeyboardButton(text="Orqaga qaytish")]
]
python1 = types.ReplyKeyboardMarkup(keyboard=pythonn, resize_keyboard=True)

key = [
    [types.KeyboardButton(text="Kiyimlar", ), types.KeyboardButton(text="Texnika", )],
    [types.KeyboardButton(text="Orqaga qaytish")]
]
keyboard1 = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)

board = [
    [types.KeyboardButton(text="Erkak", ), types.KeyboardButton(text="Ayol", )],
    [types.KeyboardButton(text="Orqaga qaytish")]
]
board1 = types.ReplyKeyboardMarkup(keyboard=board, resize_keyboard=True)



dres =[
    [types.KeyboardButton(text="Jenfir") , types.KeyboardButton(text="kurtka")],
    [types.KeyboardButton(text="Etik") , types.KeyboardButton(text="Shapka")]
]
dress = types.ReplyKeyboardMarkup(keyboard=dres, resize_keyboard=True)







# dress = [
#     types.InlineKeyboardButton(text="Narxi", callback_data="narxi"),
#     types.InlineKeyboardButton(text="Kurtka", callback_data="kurtka"),
#     types.InlineKeyboardButton(text="Etik", callback_data="etik"),
#     types.InlineKeyboardButton(text="Shapka", callback_data="shapka"),
#     types.InlineKeyboardButton(text="Texnika", callback_data="texnika"),
#     types.InlineKeyboardButton(text="Iphone", callback_data="iphone"),
#     types.InlineKeyboardButton(text="Samsung", callback_data="samsung"),
#     types.InlineKeyboardButton(text="Redmi", callback_data="redmi"),
#     types.InlineKeyboardButton(text="Vivo", callback_data="vivo"),
# ]



kb = [
    [types.KeyboardButton(text="Iphone"), types.KeyboardButton(text="Samsung")],
    [types.KeyboardButton(text="Redmi"), types.KeyboardButton(text="vivo")],
    [types.KeyboardButton(text="Orqaga qaytish ")]

]
keyboard2 = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Word")



sezon = [
    [types.KeyboardButton(text="Qish 🥶"), types.KeyboardButton(text="Bahor 🍀")],
    [types.KeyboardButton(text="Kuz 🍁"), types.KeyboardButton(text="Yoz 😎")],
    [types.KeyboardButton(text="Orqaga qaytish")]
]
sezonkey = types.ReplyKeyboardMarkup(keyboard=sezon, resize_keyboard=True)







