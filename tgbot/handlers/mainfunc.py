import re

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import Message

from audiothing import audio
from bot_data import bot, logger
from tgbot.states import State


def normalize_youtube_link(link):
    # Regular expression pattern to extract video ID
    video_id_pattern = re.compile(r'(?:\?v=|youtu\.be/)([\w-]+)')

    # Find the video ID in the link
    match = video_id_pattern.search(link)
    if match:
        video_id = match.group(1)
        normalized_link = f'https://www.youtube.com/watch?v={video_id}'
        return normalized_link
    else:
        return None


async def mainfunc(message: Message):
    url = normalize_youtube_link(message.text)
    if (url != None):
        try:
            audiofile = audio(url)
            path = audiofile.download_path
            thumb_path = audiofile.thumbnail
            audiof = open(path, mode="rb")
            thumbf = open(thumb_path, mode="rb")
            text = f"<a href='{message.text}'>origin</a> | <a href = 'https://t.me/Aoteulamusicbot'>from</a>"
            await bot.send_audio(message.from_id, audio=audiof, thumb=thumbf, caption=text, parse_mode="HTML",
                                 duration=audiofile.duration, protect_content=False)
            logger.info(f"{message.from_user.username} - {path[5:-17]} - sent")
        except:
            await bot.send_message(message.from_id,
                                   text="Отправьте ссылку на YouTube видеоролик, аудио, которого хотите загрузить")
    else:
        await bot.send_message(message.from_id,
                               text="хуйню не пиши, заебал")


async def reg_main(dp: Dispatcher):
    dp.register_message_handler(mainfunc, )
