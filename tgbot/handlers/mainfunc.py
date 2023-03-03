from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import Message

from audiothing import audio
from bot_data import bot
from tgbot.states import State
from thumbnail import download_preview


async def mainfunc(message: Message):
    # try:
        url = message.text
        try:
            audiofile = audio(url)
            path = audiofile.download_path
            thumb_path = download_preview(audiofile.thumbnail_url)
            audiof = open(path, mode="rb")
            thumbf = open(thumb_path, mode="rb")
            text = f"<a href='{message.text}'>origin</a> | <a href = 'https://t.me/Aoteulamusicbot'>from</a>"
            await bot.send_audio(message.from_id, audio=audiof, thumb=thumbf, caption=text, parse_mode="HTML", duration=audiofile.duration, protect_content=False)
            print("sent")
        except:
            await bot.send_message(message.from_id, text="Отправьте ссылку на YouTube видеоролик, аудио, которого хотите загрузить")



# except Exception as ex:
#     await message.reply(text="Что-то пошло не так")
#     print(ex)


async def reg_main(dp: Dispatcher):
    dp.register_message_handler(mainfunc)
