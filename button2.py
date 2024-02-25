from aiogram import types

help = [
    [types.KeyboardButton(text="🌐 Python haqida"), types.KeyboardButton(text="📸 Foto")],
    [types.KeyboardButton(text="🛒 Xarid qilish"), types.KeyboardButton(text="🎼 Musiqa")],
    [types.KeyboardButton(text="💬 Biz bilan aloqa")]
]
pomosh = types.ReplyKeyboardMarkup(keyboard=help, resize_keyboard=True)

