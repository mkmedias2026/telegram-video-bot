import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

app = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("🖼 Thumb/Cover Extractor", callback_data="thumb")],
    [InlineKeyboardButton("✏️ Caption And Buttons Editor", callback_data="caption")],
    [InlineKeyboardButton("🎥 Metadata Editor", callback_data="meta"), InlineKeyboardButton("🎥 Stream Mapper", callback_data="mapper")],
    [InlineKeyboardButton("✂️ Video Trimmer", callback_data="trim"), InlineKeyboardButton("➕ Video Merger", callback_data="merge")],
    [InlineKeyboardButton("🔇 Remove Audio", callback_data="noaudio"), InlineKeyboardButton("🎵 Audio Converter", callback_data="audio")],
    [InlineKeyboardButton("🎵 Video To Audio", callback_data="v2a")],
    [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
])

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Please choose your desired action below 👇", reply_markup=BUTTONS)

app.run()
