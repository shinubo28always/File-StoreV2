import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction
from config import HELP_TXT  # ✅ Import the help text

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    # Show typing animation
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    
    # Wait for 2-3 seconds to simulate typing
    await asyncio.sleep(3)
    
    # Optionally, you can send a temporary "loading" message first
    temp_msg = await message.reply_text("⌛ Generating help... Please wait", quote=True)
    
    # Wait a bit more before sending the actual help
    await asyncio.sleep(2)
    
    # Send actual help text
    await message.reply_text(
        text=HELP_TXT,
        disable_web_page_preview=True,
        quote=True
    )
    
    # Delete the temporary message
    await temp_msg.delete()


# Added by VoidXTora 