from keyboards.inline.YT_Buttons import *
from loader import dp

from aiogram import types
from aiogram.dispatcher.filters import Text
from states.languages_state import *
from utils.InstagramDownloader import *
from utils.TikTokDownloader import TikTokVideo_info
from keyboards.inline.TikTok_Buttons import *
from aiogram.dispatcher import FSMContext

from utils.YTDownloader import GetVideoInfo, GetAudioInfo

states=[Language.english, Language.russian, None]
for state in states:
    @dp.message_handler(Text("🇺🇿 Uzbek"), state=state)
    async def uz_lan(message: types.Message):
        await message.answer(text="✅ O'zbek tili muvaffaqiyatli tanlandi", reply_markup=types.ReplyKeyboardRemove())
        await Language.uzbek.set()

state1=[Language.uzbek, None]
for holat in state1:
    #TikTok dan yuklovchi bo'lim
    @dp.message_handler(Text(startswith="https://www.tiktok.com/"), state=holat)
    async def TikTok(message: types.Message, state: FSMContext):
        all_info = await TikTokVideo_info(video_link=message.text)
        await state.update_data(video_link=message.text)
        try:
            await message.answer(text=f"{message.text}\nSiz yuborgan url manzil orqali quyidagilarni yuklab olishingiz mumkin",
                                 reply_markup=uz_tiktok_btn)
        except:
            await message.answer(
                text="Siz yuborgan url manzil orqali hech nimani aniqlay oldik, iltimos url manzilni qaytadan tekshiring yoki boshqa url manzil yuboring!")


    @dp.callback_query_handler(uz_tiktok_callback.filter(action="t_video"), state=holat)
    async def get_video(query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            video_url = data.get("video_link")
        all_info = await TikTokVideo_info(video_link=video_url)
        try:
            await query.message.answer(text="Marhamat yuklab olishingiz mumkin 📥📥📥")
            await query.message.answer_video(video=all_info["video"])
            await query.answer(cache_time=60)
        except:
            await query.message.answer(
                text="Siz yuborgan url manzil orqali hech nimani aniqlay oldik, iltimos url manzilni qaytadan tekshiring yoki boshqa url manzil yuboring!")


    @dp.callback_query_handler(uz_tiktok_callback.filter(action="t_audio"), state=holat)
    async def get_video(query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            video_url = data.get("video_link")
        all_info = await TikTokVideo_info(video_link=video_url)
        try:
            await query.message.answer(text="Marhamat yuklab olishingiz mumkin 📥📥📥")
            await query.message.answer_audio(audio=all_info["music"])
            await query.answer(cache_time=60)
        except:
            await query.message.answer(
                text="Siz yuborgan url manzil orqali hech nimani aniqlay oldik, iltimos url manzilni qaytadan tekshiring yoki boshqa url manzil yuboring!")


    @dp.callback_query_handler(uz_tiktok_callback.filter(action="t_info"), state=holat)
    async def get_video(query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            video_url = data.get("video_link")
        all_info = await TikTokVideo_info(video_link=video_url)
        info=f"Siz yuborgan url manzil orqali video haqida quyidagilarni aniqladik\n\n" \
             f"🔘 Postning nomi: {all_info['title']}\n" \
             f"🔘 Post egasining nicknamei: {all_info['nickname']}\n" \
             f"🔘 Davlat: {all_info['region']}\n" \
             f"🔘 Ko'rishlar soni: {all_info['play_count']}\n" \
             f"🔘 Sharhlar (Comments): {all_info['comment_count']}\n" \
             f"🔘 Yuklab olishlar soni: {all_info['download_count']}\n" \
             f"🔘 Ulashishlar soni: {all_info['share_count']}"
        await state.finish()
        try:
            await query.message.answer(text=info)
            await query.answer(cache_time=60)
        except:
            await query.message.answer(
                text="Siz yuborgan url manzil orqali hech nimani aniqlay oldik, iltimos url manzilni qaytadan tekshiring yoki boshqa url manzil yuboring!")

    @dp.message_handler(Text(startswith=["https://www.instagram.com/", "https://instagram.com/"]), state=holat)
    async def Instagram(message: types.Message, state: FSMContext):
        data=await GetInstagram(message.text)
        try:
            name=data["title"]
        except:
            name="Bu post nomsiz joylangan!"
        try:
            if data["Type"]=="Post-Image":
                await message.answer_photo(photo=data["media"], caption=name)
            elif data["Type"]=="Post-Video":
                await message.answer_video(video=data["media"], caption=name)
            elif data["Type"]=="Story-Video":
                await message.answer_video(video=data["media"], caption=name)
            elif data["Type"]=="Carousel":
                media_group = types.MediaGroup()
                lengh=len(data["media"])
                data1=data["media"]
                for i in range(0,lengh-1):
                    if ".mp4" and "video" in data1[i]:
                        media_group.attach_video(video=data1[i])
                    elif ".jpg" or ".png" or ".php" in data1[i]:
                        media_group.attach_photo(photo=data1[i])
                if ".mp4" and "video" in data1[-1]:
                    media_group.attach_video(video=data1[-1], caption=name)
                elif ".jpg" or ".png" or ".php" in data1[-1]:
                    media_group.attach_photo(photo=data1[-1], caption=name)
                await message.answer_media_group(media=media_group)
        except:
            await message.answer(
                text="Siz yuborgan url manzil orqali hech nimani aniqlay oldik, iltimos url manzilni qaytadan tekshiring yoki boshqa url manzil yuboring!")

    @dp.message_handler(Text(startswith=["https://youtu.be/","http://www.youtube.com/"]), state=holat)
    async def YouTube(message: types.Message, state: FSMContext):
        try:
            data = await GetVideoInfo(message.text)
            await state.update_data(info=message.text)
            await message.delete()
            await message.answer(text="🔍 Tekshirilmoqda")
            await message.answer_photo(
                photo=data["thumbnail"],
                caption=f"ℹ {data['video_title']} <a href='{message.text}'>-></a>\n"
                        f"👤 {data['channel_title']} <a href='{message.text}'>-></a>\n"
                        f"👁 {data['view_count']}\n\n"
                        f"Quyidagilardan birini tanlang ⬇",
                reply_markup=yt_btn
            )
        except:
            await message.answer(
                text="Siz yuborgan url manzil orqali hech nimani aniqlay oldik, iltimos url manzilni qaytadan tekshiring yoki boshqa url manzil yuboring!")


    @dp.callback_query_handler(yt_callback.filter(action="360p"), state=holat)
    async def SendVideo1(query: types.CallbackQuery, state: FSMContext):
        try:
            async with state.proxy() as url:
                video_url = url.get("info")
            data = await GetVideoInfo(video_url)
            await query.message.answer_video(
                video=data["video"][1]["url"],
                caption=f"ℹ {data['video_title']} <a href='{video_url}'>-></a>\n"
                        f"👤 {data['channel_title']} <a href='{video_url}'>-></a>\n"
                        f"@media_assist_bot 📹360p"
            )
            await query.answer(cache_time=60)
        except:
            await query.message.answer(
                text="Ushbu formatda faylni topa olmadik!")

    @dp.callback_query_handler(yt_callback.filter(action="720p"), state=holat)
    async def SendVideo2(query: types.CallbackQuery, state: FSMContext):
        try:
            async with state.proxy() as url:
                video_url = url.get("info")
            data = await GetVideoInfo(video_url)
            await query.message.answer_video(
                video=data["video"][2]["url"],
                caption=f"ℹ {data['video_title']} <a href='{video_url}'>-></a>\n"
                        f"👤 {data['channel_title']} <a href='{video_url}'>-></a>\n"
                        f"@media_assist_bot 📹720p"
            )
            await query.answer(cache_time=60)
        except:
            await query.message.answer(
                text="Ushbu formatda faylni topa olmadik!")


    @dp.callback_query_handler(yt_callback.filter(action="audio"), state=holat)
    async def SendAudio(query: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as url:
            video_url = url.get("info")
        data = await GetVideoInfo(video_url)
        audio = await GetAudioInfo(video_url)
        try:
            await query.message.answer_audio(
                audio=audio["link"],
                caption=f"ℹ {data['video_title']} <a href='{video_url}'>-></a>\n"
                        f"👤 {data['channel_title']} <a href='{video_url}'>-></a>\n"
                        f"@media_assist_bot"
            )
            await query.answer(cache_time=60)
        except:
            await query.message.answer(
                text="Ushbu formatda faylni topa olmadik!")