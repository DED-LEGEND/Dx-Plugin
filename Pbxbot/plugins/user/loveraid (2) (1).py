import random
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import MessageEntityType as MET, ChatAction as CA
from pyrogram.types import Message
from . import *
RAID_STR = ["HAYEE MERI JAAN 🤩🤩",
    "MERI JAAN KITNI OSM HAI YAAR 😁🌹🌹😍😍😍",
    "I LOVE YOU MERI JAAN❤️❤️",
    "MERI JAAN I KISS YOU ❤️😋😊😘😘😘",
    "I MISS YOU JAAN 🥀🥀✨✨",
    "Mat muskurao itna ki Phoolo ko khabar lag jaye Ke wo kare taaref tumhari Aur tumhe unki najar lag jaye",
    "Chand se haseen hai chandni Chandni se haseen hai Raat Raat se haseen hai chand Aur chand se haseen hai aap",
    "You look so beautiful and pretty I feel lucky because you love me I love you now and I’ll always do Because I just can’t live without you",
    "Chand sa tera masoom chehra Tu haya ki ek murat hai Tujhe dekh ke kaliya bhi sharmaaye Tu itni khoobsurat hai",
    "कैसे करुं बयाँ मै खुबसुरती उसकी मेने तो उसे बिना देखे ही प्यार किया है।",
    "Mai tumhari sadagi ki kya misal du Is saare jaha me Be misaal ho tum",
    "LOVE YOU JAAN 😁😁🔥🔥😂",
    "I HUG YOU BABY 🤣🤣",
    "I LOVE YOU SO MUCH 🌹💫💖",
    "MADE BY DEV JAAN 😂😂",
    "нello 😍мerι jaan",
    "oye вaвy ѕυno na 😍",
    "ι love υ вaвe😘",
    "тυм нι нo🥺❤️",
    "आप ही के बिना हम क्यों बेचैन हैं",
    "आप ही क्यों मेरी जरूरत हैं",
    "वहम इतना हसीं नहीं होता",
    "वाकई आप खूबसूरत हैं",
    "ᴏyᴇ ʜᴏyᴇ ꜱᴀʀᴍᴀ ɢyɪ ᴋᴀᴀ ᴩʜᴏɴᴇ ᴋᴀᴛ ᴅɪ ᴍᴜᴍᴍy ᴀᴀ ɢyɪ ᴋyᴀ 🤣",
    "TU MAAN MERI JAAN TUJHE JANE NA DUNGA 🤣🤣✨",
    "TUJHE APNI BAHO ME SAJAKE 🤣🤣🤣",
    "EK UCHA LMBA KAD DUJA SONI HONI HAD TIJHA TERA RUP CHAM CHAM KR DANI TERE SIVHA DIL ME KOI UTRA THA NHI🤣🤣🤣🤣🌹🌹",
    "BS KHAFI HO GYI JHUT KI TARIF🤣🤣🤣",
    "HEY HA YOU....YOU ARE SO BEAUTIFUL ✨🌹 I LOVE YOU 🤣🥀🥀🥀✨✨🌹🌹",
    "MERI JAAN TUJHE NAZAR NA 🤣LGA JAYE KISI KI 🙄🆘",
    "KIN NA SONA TUJHE RAB NE BNAYA KI JI KRE DEKH THA RHU 😂😂🌹🌹❤️❤️😜🤣🤣",
    "LAL DUPATTA UD GYA HAYE MERI BEAUTY SE 🤣🤣😜😜",
    "BS BS HO GYI AB JHUTI TARIF JAAN 🤣🤣🤣",
    "#LOVE YOU JAAN",
    "I WANT YOU 👀BABY",
    "UMMMMM MAAA MERI JAAN 😍😘😘😘😘😘"]
except Exception:
to_del = await m.reply_text("Unable to fetch user from the given entity")
await asyncio.sleep(10)
await m.delete(True)
await to_del.delete(True)
return
Pbx = await m.reply_text("Reply LRaid Activating....")
u_id = user.id
username = f"@{user.username}" if user.username else user.mention
if u_id not in que:
que.append(u_id)
await Pbx.edit_text(f"Reply LRaid has been activated on {username}")
else:
await Pbx.edit_text("You already have started reply raid for this user")
@on_message("dlove", allow_stan=True)
async def deactivate_reply_raid(c: Client, m: Message):
global que
if m.forward_from:
return
if m.reply_to_message:
reply_to = m.reply_to_message.from_user
if not reply_to:
await m.reply_text("reply to and user")
return
u_id = reply_to.id
username = f"@{reply_to.username}" if reply_to.username else reply_to.mention
Pbx = await m.reply_text("reply LRaid De-activating....")
try:
if u_id in que:
que.remove(u_id)
await Pbx.edit_text(f"reply Raid has been De-activated on {username}")
return
await Pbx.edit_text("You haven't started reply raid for this user")
except Exception:
await Pbx.edit_text("You haven't activated reply raid for this user")
return
else:
try:
user = int(m.command[1])
except ValueError:
user = m.command[1]
if m.entities[1].type == MET.TEXT_MENTION:
user = m.entities[1].user.id
try:
user = await c.get_users(user)
except Exception:
to_del = await m.reply_text("Unable to fetch user from the given entity")
await asyncio.sleep(10)
await m.delete(True)
await to_del.delete(True)
return
Pbx = await m.reply_text("reply Raid De-activating....")
u_id = user.id
username = f"@{user.username}" if user.username else user.mention
try:
if u_id in que:
que.remove(u_id)
await Pbx.edit_text(f"Hreply Raid has been De-activated on {username}")
return
await Pbx.edit_text("You haven't started reply raid for this user")
except Exception:
await Pbx.edit_text("You haven't activated reply raid for this user")
return
HelpMenu("lovereplyraid").add(
"lovereplyraid", None, "Starts reply raid on mentioned user.",
).add(
"dlove", None, "Stops reply raid on mentioned user."
).info(
"Spammer Module\nMay cause floodwait!"
).done()
