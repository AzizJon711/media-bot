from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

uz_tiktok_callback=CallbackData("tiktok", "action")
en_tiktok_callback=CallbackData("tiktok", "action")
ru_tiktok_callback=CallbackData("tiktok", "action")

uz_tiktok_btn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📹 Videoni yuklash", callback_data=uz_tiktok_callback.new(action="t_video")),
            InlineKeyboardButton(text="🔉 Audioni yuklash", callback_data=uz_tiktok_callback.new(action="t_audio")),
        ],
        [
            InlineKeyboardButton(text="💬 Post haqida qisqacha ma'lumot", callback_data=uz_tiktok_callback.new(action="t_info")),
        ]
    ]
)

ru_tiktok_btn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📹 Скачать видео", callback_data=ru_tiktok_callback.new(action="t_video")),
            InlineKeyboardButton(text="🔉 Скачать аудио", callback_data=ru_tiktok_callback.new(action="t_audio")),
        ],
        [
            InlineKeyboardButton(text="💬 Краткая информация о посту", callback_data=ru_tiktok_callback.new(action="t_info")),
        ]
    ]
)

en_tiktok_btn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📹 Download video", callback_data=en_tiktok_callback.new(action="t_video")),
            InlineKeyboardButton(text="🔉 Download audio", callback_data=en_tiktok_callback.new(action="t_audio")),
        ],
        [
            InlineKeyboardButton(text="💬 Brief information about the post", callback_data=en_tiktok_callback.new(action="t_info")),
        ]
    ]
)