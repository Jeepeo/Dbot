import importlib
import sqlite3
import sys

from userbot import BRAIN_CHECKER, LOGS, bot
from userbot.modules import ALL_MODULES

db = sqlite3.connect("brains.check")
cursor = db.cursor()
cursor.execute("""SELECT * FROM BRAIN1""")
all_rows = cursor.fetchall()
for i in all_rows:
    BRAIN_CHECKER.append(i[0])
db.close()
bot.start()
for module_name in ALL_MODULES:
    imported_module = importlib.import_module("userbot.modules." + module_name)
<<<<<<< HEAD
LOGS.info('Your Bot is alive! Test it by typing .alive on any chat. Should you need assistance, head to https://t.me/userbot_support. Your Bot Version is 2.1.1-b')
if len(sys.argv) not in (1,3,4):
=======

LOGS.info("Your Bot is alive! Test it by typing .alive on any chat."
<<<<<<< HEAD
          "Should you need assistance, head to https: // t.me / userbot_support."
          "Your Bot Version is 2.1.1-b")
=======
          "Should you need assistance, head to https://t.me/userbot_support")
LOGS.info("Your Bot Version is 2.2-a")
>>>>>>> 98e8a44... userbot: main, init: remove redundant commands and bump to v2.2-a

if len(sys.argv) not in (1, 3, 4):
>>>>>>> 871fa92... [REFACTOR] : Linting the stuff (3)
    bot.disconnect()
else:
    bot.run_until_disconnected()
