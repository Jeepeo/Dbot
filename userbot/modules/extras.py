import asyncio
from userbot import bot
from telethon import events
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, ExportInviteRequest, CreateChannelRequest, DeleteMessagesRequest

@bot.on(events.NewMessage(outgoing=True, pattern='^\.timer '))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.timer '))
async def timer_blankx(e):
	txt=e.text[7:] + '\nJeepeo , Im Deleting in '
	j=15
	k=j
	for j in range(j):
		await e.edit(txt + str(k))
		k=k-1
		await asyncio.sleep(1)
	await e.delete()

@bot.on(events.NewMessage(outgoing=True, pattern='^\.stimer '))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.stimer '))
async def stimer_blankx(e):
	await e.edit(e.text[7:])
	await asyncio.sleep(10)
	await e.delete()

@bot.on(events.NewMessage(outgoing=True, pattern='^\.time$'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.time$'))
async def time_blankx(e):
	if e.reply_to_msg_id != None:
		thed='Jeepeo , I am Deleting replied to message in '
		j=10
		k=j
		for j in range(j):
			await e.edit(thed + str(k))
			k=k-1
			await asyncio.sleep(1)
		await bot.delete_messages(e.input_chat, [e.reply_to_msg_id, e.id])

@bot.on(events.NewMessage(outgoing=True, pattern='^\.stime$'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.stime$'))
async def stime_blankx(e):
	await e.delete()
	if e.reply_to_msg_id != None:
		await asyncio.sleep(10)
		await bot.delete_messages(e.input_chat, [e.reply_to_msg_id])

@bot.on(events.NewMessage(outgoing=True, pattern='^\.sedit '))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.sedit '))
async def sedit_blankx(e):
	await e.edit('s/\X+/' + e.text[7:])
	await e.delete()

@bot.on(events.NewMessage(outgoing=True, pattern='^\.sedita '))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.sedita '))
async def sedit_blankx(e):
	await e.delete()
	if e.reply_to_msg_id != None:
		f=await bot.send_message(await bot.get_input_entity(e.chat_id), message='s/((.+|\\n+))+/' + e.text[8:], reply_to=e.reply_to_msg_id)
		await asyncio.sleep(0.25)
		await f.delete()

@bot.on(events.NewMessage(outgoing=True, pattern="^.block$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.block$"))
async def blocks(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if '-' not in str(e.chat_id):
            await bot(BlockRequest(await bot.get_input_entity(e.chat_id)))
        else:
            await e.edit('`In PM sar`')

@bot.on(events.NewMessage(outgoing=True, pattern="^.leave$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`This is dead group!`')
