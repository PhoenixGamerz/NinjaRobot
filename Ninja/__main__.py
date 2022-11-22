import os
import logging
import pyrogram
from os import getenv
from pyrogram import Client
import config
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING,
)

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID", "O"))

linda = "🎉 sᴜᴄᴄᴇsғᴜʟʟʏ ᴅᴇᴘʟᴏʏᴇᴅ ʏᴏᴜʀ ʙᴏᴛ!!"
tinda = "🤣 ᴀʀᴇᴇ ʙʜᴀɪ ᴀʙ ʙᴀɴ ɢᴀʏᴀ ʜᴀɪ ᴄʜᴀɴɴᴇʟ ᴊᴏɪɴ ᴋᴀʀʟᴇ."

if __name__ == "__main__" :
    print()
    print()
    app = pyrogram.Client(
         "Ninja",
         config.API_ID,
         config.API_HASH,
         bot_token=BOT_TOKEN,
         plugins=dict(root="plugins")
)
         app.run()
