from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from googletrans import Translator

from loader import dp
from states.languages_state import Language


text=f"Assalomu alaykum hurmatli  bot foydalanuvchisi! Bizning MediaAssistBot botimiz nimalar qila oladi?\n\n"
text+=f"🔹<i>Instagramdan istalgan turdagi media fayllarni yuklab oladi. Ya'ni video, rasm, karusel, reels, story</i>\n"
text+=f"🔸<i>TikTokdan video va rasmlarni yuklab oladi, bundan tashqari videoning audio formatini ham yuklab oladi</i>\n"
text+=f"🔸<i>Va juda ham katta imkoniyatga ega bo'lgan funksiya bu YouTubedan videolarning barcha turdagi formatda yuklab uning audio faylini ham yuklaydi</i>\n"
text+=f"🔹<i>YouTubedan videoni telegramda qidirish imkoniyati, @vid kalit so'zidan so'ng kerakli nom bilan qidirishingiz mumkin</i>\n"
text+=f"🔸<i>/languages buyrug'i bilan kerakli tilni tanlashingiz mumkin</i> \n\n@media_assist_bot"

image_path="media/MediaAssistBot.png"
@dp.message_handler(CommandStart(), state=Language.english)
async def english_bot_start(message: types.Message):
    tarjimon=Translator()
    tarjima=tarjimon.translate(text, "en")
    with open(image_path, "rb") as image:
        await message.answer_photo(photo=image,caption=tarjima.text)

@dp.message_handler(CommandStart(), state=Language.russian)
async def russian_bot_start(message: types.Message):
    tarjimon=Translator()
    tarjima=tarjimon.translate(text, "ru")
    with open(image_path, "rb") as image:
        await message.answer_photo(photo=image, caption=tarjima.text)

@dp.message_handler(CommandStart(), state=Language.uzbek)
async def uzbek_bot_start(message: types.Message):
    tarjimon=Translator()
    tarjima=tarjimon.translate(text, "uz")
    with open(image_path, "rb") as image:
        await message.answer_photo(photo=image, caption=text)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    with open(image_path, "rb") as image:
        await message.answer_photo(photo=image, caption=text)
