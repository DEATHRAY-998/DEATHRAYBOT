# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DEATHRAY BOT"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/8c103b3a39b71a129bae1.jpg"
file2 = "https://telegra.ph/file/8c103b3a39b71a129bae1.jpg"
file3 = "https://telegra.ph/file/8c103b3a39b71a129bae1.jpg"
file4 = "https://telegra.ph/file/8c103b3a39b71a129bae1.jpg"

""" =======================CONSTANTS====================== """
pm_caption = "** 𝔻𝕖𝕒𝕥𝕙ℝ𝕒𝕪 𝕌𝕤𝕖𝕣𝔹𝕠𝕥 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n"
pm_caption += "**Yes Sir, I Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 15.0.0\n"
pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/deathray_support)\n"
pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [𝚃𝙴𝙰𝙼 DEATHRAY](https://github.com/DEATHRAY-998)\n"
pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [DeathRay team](https://github.com/DEATHRAY-998/DEATHRAY-998)\n\n"
pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ {DEFAULTUSER}\n"

@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
