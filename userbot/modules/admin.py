import time

from telethon import events
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest

from telethon.tl.types import ChatAdminRights, ChatBannedRights

from userbot import (BRAIN_CHECKER, LOGGER, LOGGER_GROUP, bot)


@bot.on(events.NewMessage(outgoing=True, pattern="^.promote$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.promote$"))
async def wizzard(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        chats=await e.get_chat()
        rights = chats.admin_rights
        rights3 = chats.creator
        rights2 = ChannelAdminRights(
            add_admins=True,
            invite_users=True,
            change_info=True,
            ban_users=True,
            delete_messages=True,
            pin_messages=True,
            invite_link=True,
        )
        if not (await e.get_reply_message()):
            await e.edit("`Give a reply message`")
            return
        elif not rights and rights3:
            rights=rights2
        elif not rights and not rights3:
            rights=None
        await e.edit("`Trying to promote the bitch.....`")
        time.sleep(3)
        try:
            await bot(
            EditAdminRequest(e.chat_id, (await e.get_reply_message()).sender_id, rights)
            )
        except Exception:
            await e.edit("`You Don't have sufficient permissions to paramod`")

        except BadRequestError:
            await promt.edit(
                "`You Don't have sufficient permissions to parmod`"
                )
            return
        await e.edit("`Promoted the bitch Successfully!`")



@bot.on(events.NewMessage(outgoing=True, pattern="^.demote$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.demote$"))
async def demote(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        rights = ChannelAdminRights(
            add_admins=False,
            invite_users=False,
            change_info=False,
            ban_users=False,
            delete_messages=False,
            pin_messages=False,
            invite_link=False,
        )
        chat=await e.get_chat()
        rights = chat.admin_rights
        rights2 = chat.creator
        if not (await e.get_reply_message()):
            await e.edit("`Give a reply message`")
            return
        if not rights and not rights2:
            await e.edit("`Ooof Jeepeo, U aren't an admin!`")
            return
        await e.edit("`Trying to demote the bitch.....`")
        time.sleep(3)
        try:
            await bot(
            EditAdminRequest(e.chat_id, (await e.get_reply_message()).sender_id, rights)
            )
        except Exception:
            await e.edit("`You Don't have sufficient permissions to demhott`")

        except BadRequestError:
            await dmod.edit("`You Don't have sufficient permissions to demhott`")
            return
        await e.edit("`Demoted the bitch Successfully!`")



@bot.on(events.NewMessage(outgoing=True, pattern="^.ban$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.ban$"))
async def thanos(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        rights = ChannelBannedRights(
            until_date=None,
            view_messages=True,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True,
        )

        sender = await bon.get_reply_message()
        try:
            if sender.sender_id in BRAIN_CHECKER:
                await bon.edit("`Ban Error! I am not supposed to ban this user`")
                return
        except AttributeError:
            await bon.edit("`You don't seems to do this right`")
            return

        await bon.edit("`Whacking the pest!`")
        time.sleep(5)
        try:
            await bot(
                EditBannedRequest(
                    bon.chat_id,
                    sender.sender_id,
                    rights
                )
            )

        except BadRequestError:
            if bon.sender_id in BRAIN_CHECKER:
                await bon.respond(
                    "<triggerban> " +
                    str((await bon.get_reply_message()).sender_id)
                )
                return
        await e.delete()
        await e.respond("`Banned that Bitch !`")
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                str((await e.get_reply_message()).sender_id) + " was banned.",
            )


@bot.on(events.NewMessage(outgoing=True, pattern="^.mute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.mute$"))
async def spider(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if (await e.get_reply_message()).sender_id in BRAIN_CHECKER:
            await e.edit("`Mute Error! I am not supposed to mute this user`")
            return
        try:
            from userbot.modules.sql_helper.spam_mute_sql import mute
        except Exception:
            await e.edit("`Running on Non-SQL mode!`")
            return
        chat=await e.get_chat()
        rights = chat.admin_rights
        rights2 = chat.creator
        if not rights and not rights2:
            await e.edit("`Ooof Jeepeo , We can try next time becoZ You aren't an admin in this cancerous group !`")
            return
        mute(e.chat_id, str((await e.get_reply_message()).sender_id))
        await e.edit("`Gets a tape!`")
        time.sleep(5)
        await e.delete()
        await e.respond("`Safely taped!`")
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                str((await spdr.get_reply_message()).sender_id) +
                " was muted.",
            )


@bot.on(events.NewMessage(incoming=True, pattern="<triggerban>"))
async def triggered_ban(triggerbon):
    ban_id = int(triggerbon.text[13:])
    if triggerbon.sender_id in BRAIN_CHECKER:  # non-working module#
        rights = ChatBannedRights(
            until_date=None,
            view_messages=True,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True,
        )

        if ban_id in BRAIN_CHECKER:
            await triggerbon.edit("`Sorry Master!`")
            return

        time.sleep(5)
        await bot(EditBannedRequest(triggerbon.chat_id, ban_id, rights))
        await triggerbon.delete()
        await bot.send_message(triggerbon.chat_id,
                               "Job was done, Master! Gimme Cookies!")


@bot.on(events.NewMessage(outgoing=True, pattern="^.unmute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.unmute$"))
async def unmoot(unmot):
    if not unmot.text[0].isalpha() and unmot.text[0] not in ("/", "#", "@", "!"):
        from userbot.modules.sql_helper.spam_mute_sql import unmute

        unmute(unmot.chat_id, str((await unmot.get_reply_message()).sender_id))
        await unmot.edit("```Unmuted Successfully```")


@bot.on(events.NewMessage(incoming=True))
@bot.on(events.MessageEdited(incoming=True))
async def muter(e):
    try:
        from userbot.modules.sql_helper.spam_mute_sql import is_muted
        from userbot.modules.sql_helper.gmute_sql import is_gmuted
    except:
        return
    mootd = is_muted(moot.chat_id)
    gmootd = is_gmuted(moot.sender_id)
    if mootd:
        for i in mootd:
            if str(i.sender) == str(moot.sender_id):
                await moot.delete()
    for i in gmootd:
        if i.sender == str(moot.sender_id):
            await moot.delete()


@bot.on(events.NewMessage(outgoing=True, pattern="^.ungmute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.ungmute$"))
async def ungmoot(ungmoot):
    if not ungmoot.text[0].isalpha() and ungmoot.text[0] \
            not in ("/", "#", "@", "!"):

        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
            await e.edit('`Ooh my Master  connect me to DB!`')
        ungmute(str((await e.get_reply_message()).sender_id))
        await e.edit("```Ungmuted Successfully```")



@bot.on(events.NewMessage(outgoing=True, pattern="^.gmute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.gmute$"))
async def gmute(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if (await e.get_reply_message()).sender_id in BRAIN_CHECKER:
            await e.edit("`Mute Error! Couldn't mute this user`")
            return
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except Exception as er:
            print(er)
            await e.edit("`Ooh my Jeepeo connect me to DB!`")
            return
        gmute(str((await e.get_reply_message()).sender_id))
        await e.edit("`Grabs a huge, sticky duct tape!`")
        time.sleep(5)
        await e.delete()
        await e.respond("`Taped!`")
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                str((await e.get_reply_message()).sender_id) + " was muted.",
            )
