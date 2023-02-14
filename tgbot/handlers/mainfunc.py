from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import Message

from audiothing import video_to_audio
from bot_data import bot
from tgbot.states import State
from thumbnail import download_preview


async def mainfunc(message: Message):
    # try:
    if ("youtube.com" in message.text):
        url = message.text
        path = video_to_audio(url)
        thumb_path = download_preview(url)
        audiofile = open(path, mode="rb")
        thumbfile = open(thumb_path, mode="rb")
        await bot.send_audio(message.from_id, audio=audiofile, thumb=thumbfile, )
        print("sent")
    else:
        await message.reply(text="Что-то пошло не так")


# except Exception as ex:
#     await message.reply(text="Что-то пошло не так")
#     print(ex)


async def reg_main(dp: Dispatcher):
    dp.register_message_handler(mainfunc)
