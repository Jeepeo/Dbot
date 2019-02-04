# Special module to block pms automatically
from telethon.tl.functions.contacts import BlockRequest
import sqlite3
from telethon import TelegramClient, events
from userbot import bot
from userbot import PM_AUTO_BAN
from userbot import COUNT_PM, NOTIF_OFF
from userbot import LOGGER, LOGGER_GROUP


@bot.on(events.NewMessage(incoming=True))
@bot.on(events.MessageEdited(incoming=True))
async def permitpm(e):
    if PM_AUTO_BAN:
        global COUNT_PM
        if e.is_private and not (await e.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
            except:
                return
            E = is_approved(e.chat_id)
            if not E and e.text != "`Hey! This is jeepeo's Assistant. \n\nJeepeo doesn't said me about your PM. \
I will say about you to Jeepeo . He actually reply to all execpt👇.\n\n\
He doesn't reply to retard/shit people .😝`" :
                await e.reply(
                    "` Hey! This is jeepeo's Assistant\n\nJeepeo doesn't said me about your PM \
I will say about you to Jeepeo . He actually reply to all execpt👇\n\n\
He doesn't reply to retard/shit people.😝.`"
                )
                if NOTIF_OFF:
                    await bot.send_read_acknowledge(e.chat_id)
                if e.chat_id not in COUNT_PM:
                    COUNT_PM.update({e.chat_id: 1})
                else:
                    COUNT_PM[e.chat_id] = COUNT_PM[e.chat_id] + 1
                if COUNT_PM[e.chat_id] > 4:
                    await e.respond(
                        "`Bitch! You are spaming chat! Bitch!mc bc mf ! I am going to report you bitch!.`"
                    )
                    del COUNT_PM[e.chat_id]
                    await bot(BlockRequest(e.chat_id))
                    if LOGGER:
                        name = await bot.get_entity(e.chat_id)
                        name0 = str(name.first_name)
                        await bot.send_message(
                            LOGGER_GROUP,
                            "["
                            + name0
                            + "](tg://user?id="
                            + str(e.chat_id)
                            + ")"
                            + " was just another retarded nibba",
                        )


@bot.on(events.NewMessage(outgoing=True,pattern="^.notifoff$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifoff$"))
async def notifoff(e):
    global NOTIF_OFF
    NOTIF_OFF=True
    await e.edit("`Notifications silenced!`")


@bot.on(events.NewMessage(outgoing=True,pattern="^.notifon$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifon$"))
async def notifoff(e):
    global NOTIF_OFF
    NOTIF_OFF=False
    await e.edit("`Notifications unmuted!`")


@bot.on(events.NewMessage(outgoing=True, pattern="^.approve$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.approve$"))
async def approvepm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.pm_permit_sql import approve
        except:
            await e.edit("`Running on Non-SQL mode!`")
            return
        approve(e.chat_id)
        await e.edit("`Mmm! You are approved to PM by Jeepeo😎`")
        if LOGGER:
            aname = await bot.get_entity(e.chat_id)
            name0 = str(aname.first_name)
            await bot.send_message(
                LOGGER_GROUP,
                "["
                + name0
                + "](tg://user?id="
                + str(e.chat_id)
                + ")"
                + " Jeepeo😎 has approved you to PM!.",
            )
@bot.on(events.NewMessage(outgoing=True, pattern="^.disapprove$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.disapprove$"))
async def disapprovepm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.pm_permit_sql import dissprove
        except:
            await e.edit("`Running on Non-SQL mode!`")
            return
        dissprove(e.chat_id)
        await e.edit("`Sad!😐 You have been disapproved to PM Jeepeo😎`")
        if LOGGER:
            aname = await bot.get_entity(e.chat_id)
            name0 = str(aname.first_name)
            await bot.send_message(
                LOGGER_GROUP,
                "["
                + name0
                + "](tg://user?id="
                + str(e.chat_id)
                + ")"
                + " Was disapproved to PM! Jeepeo😎.",
            )
