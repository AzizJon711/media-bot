from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from utils.YTDownloader import GetVideoInfo

yt_callback=CallbackData("youtube", "action")

yt_btn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📹 360p ⚡", callback_data=yt_callback.new(action="360p")),
            InlineKeyboardButton(text="📹 720p ⚡", callback_data=yt_callback.new(action="720p"))
        ],
[
            InlineKeyboardButton(text="🔉 Audio 128 kbs 🎵", callback_data=yt_callback.new(action="audio"))
        ],
    ]
)
