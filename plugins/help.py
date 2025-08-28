from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction
from config import HELP_TXT  # ✅ Import the help text

@Client.on_message(filters.command("help") & filters.private)
async def help_command(bot: Client, message: Message):
    # Show upload animation while sending help
    await client.send_chat_action(chat_id, "typing")        # Shows "typing..."

    # Send help message from config
    await message.reply_text(
        text=HELP_TXT,
        disable_web_page_preview=True,
        quote=True
    )


# Added by VoidXTora 