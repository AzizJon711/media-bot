from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_admin_uz=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
contact_admin_uz.add(
    KeyboardButton(text="📲 Admin bilan bog'lanish")
)

contact_admin_en=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
contact_admin_uz.add(
    KeyboardButton(text="📲 Contact admin")
)

contact_admin_ru=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
contact_admin_uz.add(
    KeyboardButton(text="📲 Связаться с администратором")
)