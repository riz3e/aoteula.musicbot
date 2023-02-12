from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import Message

from audiothing import video_to_audio
from tgbot.states import State
from thumbnail import download_preview


async def mainfunc(message: Message):
    # try:
        if ("youtube.com" in message.text):
            url = message.text
            path = video_to_audio(url)
            thumb_path = download_preview(url)
            file = open(path, encoding="latin-1")
            thumb = open(thumb_path, encoding="latin-1")
            # message.reply_audio()
            await message.reply_audio(audio=file, thumb=thumb)
            print("sent")
        else:
            await message.reply(text="Что-то пошло не так")
    # except Exception as ex:
    #     await message.reply(text="Что-то пошло не так")
    #     print(ex)


async def reg_main(dp: Dispatcher):
    dp.register_message_handler(mainfunc, state=State.main)
