from loader import dp

from aiogram import types
from aiogram.dispatcher.filters import Command
from states.languages_state import Language
from googletrans import Translator


text=f"Botdagi turli xil muammolar va kamchiliklar bo'lsa ular uchun uzr so'rayman!\nMarhamat qanday savol yoki taklifingiz bo'lsa adminga yozishingiz mumkin\n"
text+=f"📲 Murojaat uchun: @Azizjon_Bahromov"
image_path="E:\Python_Dasturlash_tili\Codes\Telegram__Bot\MediaAssistBot\media\\admin.png"

@dp.message_handler(Command("admin"), state=Language.english)
async def ContactAdmin(message: types.Message):
    tarjimon=Translator()
    tarjima=tarjimon.translate(text, dest="en")
    with open(image_path, "rb") as image:
        await message.answer_photo(photo=image, caption=tarjima.text)

@dp.message_handler(Command("admin"), state=Language.russian)
async def ContactAdmin(message: types.Message):
    tarjimon=Translator()
    tarjima=tarjimon.translate(text, dest="ru")
    with open(image_path, "rb") as image:
        await message.answer_photo(photo=image, caption=tarjima.text)

@dp.message_handler(Command("admin"), state=Language.uzbek)
async def ContactAdmin(message: types.Message):
    with open(image_path, "rb") as image:
        await message.answer_photo(photo=image, caption=text)

@dp.message_handler(Command("admin"))
async def ContactAdmin(message: types.Message):
    with open(image_path, "rb") as image:
        await message.answer_photo(photo=image, caption=text)