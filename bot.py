import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.types.web_app_info import WebAppInfo
import bot_send_new

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    API_TOKEN = os.environ.get('bot_futboll_id')

    bot = Bot(token=API_TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(bot_send_new.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == '__main__':
    try:
        asyncio.run(main())

    except:
        logger.error('Bot Stop')