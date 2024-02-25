from aiogram import types


key = [
    [types.KeyboardButton(text="Texnika", )],[types.KeyboardButton(text="Boshiga qaytish")]
]
value = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)






user = [
    [types.KeyboardButton(text="Noutbuk"), types.KeyboardButton(text="Telefon")],
    [types.KeyboardButton(text="Texnikaga qaytish"), types.KeyboardButton(text="PowerBank")]
]
users = types.ReplyKeyboardMarkup(keyboard=user, resize_keyboard=True)





lap = [
    [types.KeyboardButton(text="HP"), types.KeyboardButton(text="Lenovo")],
    [types.KeyboardButton(text="Acer"), types.KeyboardButton(text="Macbook")],
    [types.KeyboardButton(text="Ortga qaytish")]
]

top = types.ReplyKeyboardMarkup(keyboard=lap , resize_keyboard=True)





kb = [
    [types.KeyboardButton(text="Iphone"), types.KeyboardButton(text="Samsung")],
    [types.KeyboardButton(text="Redmi"), types.KeyboardButton(text="vivo")],
    [types.KeyboardButton(text="Ortga qaytish")]

]
keys = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Word")



phone = [
    [types.KeyboardButton(text="Iphone 11,pro,max"), types.KeyboardButton(text="Iphone 12,pro,max")],
    [types.KeyboardButton(text="Iphone 13,pro,max"), types.KeyboardButton(text="Iphone 14,pro,max")],
    [types.KeyboardButton(text="Iphone 15,pro,max"), types.KeyboardButton(text="Telefonlarga qaytish")]
]

phone1 = types.ReplyKeyboardMarkup(keyboard=phone, resize_keyboard=True, input_field_placeholder="Phone")


samsu = [
    [types.KeyboardButton(text="Samsung A21"),types.KeyboardButton(text="Samsung A34")],
    [types.KeyboardButton(text="Samsung A50"),types.KeyboardButton(text="Samsung A51")],
    [types.KeyboardButton(text="Samsung A54"),types.KeyboardButton(text="Samsung A62")],
    [types.KeyboardButton(text="Samsung A71"),types.KeyboardButton(text="Samsung S21, Ultra, Plus")],
    [types.KeyboardButton(text="Samsung S22, Ultra, Plus"),types.KeyboardButton(text="Samsung S23, Ultra, Plus")],
    [types.KeyboardButton(text="Samsung S24, Ultra, Plus"),types.KeyboardButton(text="Telefonlarga qaytish")]
]
samsun = types.ReplyKeyboardMarkup(keyboard=samsu, resize_keyboard=True, input_field_placeholder="Samsung")





power = [
    [types.KeyboardButton(text="Iphone uchun"), types.KeyboardButton(text="Samsung uchun")],
]
Bank = types.ReplyKeyboardMarkup(keyboard=power, resize_keyboard=True)




















