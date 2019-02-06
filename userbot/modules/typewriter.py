userbot/modules/typewriter.py

from telethon import TelegramClient, events
from userbot import bot
import asyncio


@bot.on(events.NewMessage(pattern='(?i).type'))
async def typewriter(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        textx = await e.get_reply_message()
        message = e.text

        if message[6:]:
            message = str(message[6:])
        elif textx:
            message = textx
            message = str(message.message)
        sleep_time = 0.015
        typing_symbol = "|"
        index = 1
        old_text = ''
        await e.edit(typing_symbol)
        await asyncio.sleep(sleep_time)    
        for character in message:
            old_text = old_text + "" + character
            typing_text = old_text + "" + typing_symbol
            await e.edit(typing_text)
            await asyncio.sleep(sleep_time)
            await e.edit(old_text)
            await asyncio.sleep(sleep_time)
