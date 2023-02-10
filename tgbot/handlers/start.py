from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import Message

from tgbot.states import State


async def user_start(message: Message):
    await message.reply("Привет, присылай мне URL видео и я буду кидать тебе необходимое")
    await State.main.set()


async def reg_user_start(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start'])
