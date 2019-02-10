from async_generator import aclosing
<<<<<<< HEAD
import asyncio
from telethon import TelegramClient, events
from userbot import bot
from userbot import LOGGER, LOGGER_GROUP
import time
=======
from telethon import events
from telethon.errors import rpcbaseerrors
>>>>>>> 851d860... userbot: modules: purge: introduce .delmsg as /del equivalents



@bot.on(events.NewMessage(outgoing=True, pattern="^.purge$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.purge$"))
async def fastpurger(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        chat = await e.get_input_chat()
        msgs = []
        count = 0
        async with aclosing(bot.iter_messages(chat, min_id=e.reply_to_msg_id)) as h:
            async for m in h:
                msgs.append(m)
                count = count + 1
                msgs.append(e.reply_to_msg_id)
                if len(msgs) == 100:
                    await bot.delete_messages(chat, msgs)
                    msgs = []
        if msgs:
            await bot.delete_messages(chat, msgs)
        r = await bot.send_message(
            e.chat_id,
            "`Master! my boy😎 , Fast purge is completed!\n`Purged "
            + str(count)
            + " messages. **Dont worry! This msg will deleted soonly!.**",
        )
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP, "Purge of " + str(count) + " messages done successfully."
            )
        time.sleep(2)
        await r.delete()


@bot.on(events.NewMessage(outgoing=True, pattern="^.purgeme"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.purgeme"))
<<<<<<< HEAD
async def purgeme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        count = int(message[9:])
        i = 1
        async for message in bot.iter_messages(e.chat_id, from_user="me"):
=======
async def purgeme(delme):
    if not delme.text[0].isalpha() and delme.text[0] not in ("/", "#", "@", "!"):
        message = delme.text
        chat = await delme.get_input_chat()
        self_id = await bot.get_peer_id('me')
        count = int(message[9:])
        i = 1

        async for message in bot.iter_messages(chat, self_id):
>>>>>>> d014ba3... [FIXUP] : modules: purge: use wider entity for chat
            if i > count + 1:
                break
            i = i + 1
            await message.delete()
        r = await bot.send_message(
            e.chat_id,
            "`Purge complete!` Purged "
            + str(count)
            + " messages. **This auto-generated message shall be self destructed in 2 seconds.**",
        )
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP, "Purge of " + str(count) + " messages done successfully."
            )
        time.sleep(2)
        i = 1
        await r.delete()


@bot.on(events.NewMessage(outgoing=True, pattern="^.delmsg$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.delmsg$"))
<<<<<<< HEAD
async def delmsg(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        i = 1
        async for message in bot.iter_messages(e.chat_id, from_user="me"):
=======
async def delmsg(delme):
    if not delme.text[0].isalpha() and delme.text[0] not in ("/", "#", "@", "!"):
<<<<<<< HEAD
        self_id = await bot.get_peer_id('me')
        chat = await delme.get_input_chat()
        i = 1
        async for message in bot.iter_messages(chat, self_id):
>>>>>>> d014ba3... [FIXUP] : modules: purge: use wider entity for chat
            if i > 2:
                break
            i = i + 1
            await message.delete()
=======
        msg_src = await delme.get_reply_message()
        if delme.reply_to_msg_id:
            try:
                await msg_src.delete()
                await delme.delete()
                if LOGGER:
                    await bot.send_message(
                        LOGGER_GROUP,
                        "Deletion of message was successful"
                        )
            except Exception is rpcbaseerrors.BadRequestError:
                if LOGGER:
                    await bot.send_message(
                        LOGGER_GROUP,
                        "Well, I can't delete a message"
                        )
>>>>>>> 851d860... userbot: modules: purge: introduce .delmsg as /del equivalents


@bot.on(events.NewMessage(outgoing=True, pattern="^.editme"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.editme"))
<<<<<<< HEAD
async def editer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        string = str(message[8:])
        i = 1
        async for message in bot.iter_messages(e.chat_id, from_user="me"):
=======
async def editer(edit):
    if not edit.text[0].isalpha() and edit.text[0] not in ("/", "#", "@", "!"):
        message = edit.text
        chat = await edit.get_input_chat()
        self_id = await bot.get_peer_id('me')
        string = str(message[8:])
        i = 1
        async for message in bot.iter_messages(chat, self_id):
>>>>>>> d014ba3... [FIXUP] : modules: purge: use wider entity for chat
            if i == 2:
                await message.edit(string)
                await e.delete()
                break
            i = i + 1
        if LOGGER:
            await bot.send_message(LOGGER_GROUP, "Edit query was executed successfully")


@bot.on(events.NewMessage(outgoing=True, pattern="^.sd"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.sd"))
async def selfdestruct(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[4:6])
        text = str(e.text[6:])
        text = (
            text
            + "`This message shall be self-destructed in "
            + str(counter)
            + " seconds`"
        )
        await e.delete()
        x=await bot.send_message(e.chat_id, text)
        time.sleep(counter)
        await x.delete()
        if LOGGER:
            await bot.send_message(LOGGER_GROUP, "sd query done successfully")
