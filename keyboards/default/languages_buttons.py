from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tillar = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)

tillar.add(
    KeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English"),
    KeyboardButton(text="🇷🇺 Русский"),
    KeyboardButton(text="🇺🇿 Uzbek")
)