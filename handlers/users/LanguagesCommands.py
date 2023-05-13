from loader import dp

from aiogram import types
from aiogram.dispatcher.filters import Command
from states.languages_state import Language
from keyboards.default.languages_buttons import tillar

@dp.message_handler(Command("languages"), state=Language.uzbek)
async def select_lan(message: types.Message):
    await message.answer(text="Quyidagilardan birini tanlang", reply_markup=tillar)

@dp.message_handler(Command("languages"), state=Language.english)
async def select_lan(message: types.Message):
    await message.answer(text="Choose one of the following", reply_markup=tillar)

@dp.message_handler(Command("languages"), state=Language.russian)
async def select_lan(message: types.Message):
    await message.answer(text="Выберите один из следующих", reply_markup=tillar)

@dp.message_handler(Command("languages"))
async def select_lan(message: types.Message):
    await message.answer(text="Quyidagilardan birini tanlang", reply_markup=tillar)