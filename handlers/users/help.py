from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.languages_state import Language

@dp.message_handler(CommandHelp(), state=Language.english)
async def bot_help(message: types.Message):
    text = ("Commands: ",
            "/start - Starting the bot",
            "/help - Help",
            "/languages - Language selection",
            "/admin - Contact admin")

    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp(), state=Language.uzbek)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/languages - Tilni tanlash",
            "/admin - Admin bilan bog'lanish")

    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp(), state=Language.russian)
async def bot_help(message: types.Message):
    text = ("Команды: ",
            "/start - Запустить бота",
            "/help - Помощь",
            "/languages - Выбор языка",
            "/admin - Связаться с администратором")

    await message.answer("\n".join(text))

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/languages - Tilni tanlash",
            "/admin - Admin bilan bog'lanish")
    
    await message.answer("\n".join(text))
