#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ALEN TL

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram import (
    Client,
    filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Legend User", "1970.01.01.12.00.00")
    Config.AUTH_USERS
    return expires_at


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
          [
            [
              InlineKeyboardButton('⭕️ Channel ⭕️', url='https://telegram.me/VKPROJECTS'),
              InlineKeyboardButton('⭕️ Group ⭕️', url='https://t.me/VKP_BOTS')
            ]
          ]
        ),
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
          [
            [
              InlineKeyboardButton('⭕️ Channel ⭕️', url='https://telegram.me/VKPROJECTS'),
              InlineKeyboardButton('⭕️ Group ⭕️', url='https://t.me/VKP_BOTS')
            ]
          ]
        ),
        reply_to_message_id=update.message_id
    )
