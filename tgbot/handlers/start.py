from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import Message

from config import bot_name
from tgbot.states import State


async def user_start(message: Message):
    await message.answer(f"Привет, я музыкальный бот {bot_name}, присылай мне URL видео, аудио которого нужно вам.")
    await State.main.set()


async def reg_user_start(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start', 'help'])
