import os
import requests
import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import Message 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

TEXT = """ Testing"""

@Client.on_message(filters.regex("/rks1 e1"))
async def kuchhbhimsg(_, message):
  await message.reply_text(TEXT)


EP = """ **| S4 E590 | 480p** 💥
**Title** : [Krishna to the Rescue](https://t.me/RKrishnaa)
**Date** : 26th Dec, 2022 
**By** : @RKrishnaa ❣
..
• @RadheKrishn_sb 🍁 
.."""

@Client.on_message(filters.regex("/rks4 E590"))
async def ep1msg(_, message):
 #   reply = message.reply_to_message
   #   msg = await message.reply("Processing...⏳")
  #  return 
    pk = await message.reply_video('BAACAgQAAx0CanN8uQACGbFjqXRemXG2Jk2BLxB8m_8G05rFbQACPBYAAglgSFEK-uNSiqHz_h4E', caption=EP, reply_to_message_id=message.id)
    await asyncio.sleep(30)
    await pk.delete()
    await message.delete()
