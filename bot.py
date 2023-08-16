import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config
from bot_data import dp, bot, logger
from tgbot.handlers.mainfunc import reg_main
from tgbot.handlers.start import reg_user_start


async def reg_all_handlers(dp):
    await reg_user_start(dp)
    await reg_main(dp)


async def main():
    logger.info("Starting bot")

    await reg_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
