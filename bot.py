import os
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Dummy web server to keep Render Free Web Service alive
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
    def log_message(self, format, *args):
        pass

def run_http():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

threading.Thread(target=run_http, daemon=True).start()

# Config keys
api_id_raw = os.environ.get("API_ID", "0").strip()
API_ID = int(api_id_raw) if api_id_raw.isdigit() else 0
API_HASH = os.environ.get("API_HASH", "").strip()
BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()

print(f"Starting bot with API_ID: {API_ID}")

app = Client(
    "video_bot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

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
async def start_handler(client, message):
    await message.reply_text("Please choose your desired action below 👇", reply_markup=BUTTONS)

if __name__ == "__main__":
    app.run()
