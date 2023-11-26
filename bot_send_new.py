import os
import asyncio
import time
from aiogram import Bot, Router, types
from aiogram.filters import Command, Text
from aiogram.types import Message, User, BotCommand
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from sql import get_info_sql
from parser_news import get_quardian, get_allfootball

router: Router = Router()

@router.message(Command(commands=['start']))
async def start_command(message: Message, bot:Bot):
    list_id = []
    last_new = {'Guardian': None, 'Allfootbal': None}
    while True:

        for i in [get_quardian(), get_allfootball()]:
            #print(i[0])

            if str(i[5]) != last_new[i[4]]:

                button = InlineKeyboardButton(text='More', url=str(i[3]))
                key = InlineKeyboardMarkup(inline_keyboard=[[button]])

                #print(i[2])
                await bot.send_photo(chat_id=os.environ.get('chat_id_futboll'), photo=i[2], caption= f'<b>{str(i[0]).capitalize()}</b>\n{str(i[1])}\nSource: {i[4]}', reply_markup=key)
                last_new[i[4]] = str(i[5])
                print([0], last_new)

            else:
                print('no')
                time.sleep(120)
                continue

            print('Спим')
            time.sleep(300)
#@router.channel_post()
# @router.channel_post
async def channel_send_post(message, bot:Bot):
    button = InlineKeyboardButton(text='Подробнее', url=str(get_quardian()[3]))
    key = InlineKeyboardMarkup(inline_keyboard=[[button]])

    print(get_quardian()[2])
    await bot.send_photo(chat_id=os.environ.get('chat_id'), photo=get_quardian()[2],
                         caption=f'<b>{str(*get_quardian()[0]).capitalize()}</b>\n{str(get_quardian()[1])}\nИсточник: Guardian',
                         reply_markup=key)
    # for i in get_info_sql():
    #
    #     button = InlineKeyboardButton(text='Подробнее', url=str(i[10]))
    #     key = InlineKeyboardMarkup(inline_keyboard=[[button]])
    #
    #     await bot.send_photo(chat_id=os.environ.get('chat_id'), photo=i[11],
    #                          caption=f'<b>{str(i[1]).capitalize()}\nЦена: {i[3]}\nРайон: {i[4]}\nИсточник: {i[9]}</b>',
    #                          reply_markup=key)

#         time.sleep(10)

# async def restart():
#     asyncio.run(start_command())
async def main():
    x = ''
    if str(get_quardian()[0]) != x:
        asyncio.run(channel_send_post(get_quardian()[0]))
