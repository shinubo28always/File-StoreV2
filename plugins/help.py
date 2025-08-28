import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction
from config import HELP_TXT  # ✅ Import the help text

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    # Show typing animation
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    
    # Send a single temporary message that we will edit
    typing_msg = await message.reply_text("⌛ Preparing help...", quote=True)
    
    # Wait a moment before starting the "typing effect"
    await asyncio.sleep(1)
    
    # Progressive typing effect
    text_to_send = ""
    for char in HELP_TXT:
        text_to_send += char
        # Edit the message to show current text
        await typing_msg.edit_text(text_to_send)
        await asyncio.sleep(0.02)  # Adjust typing speed (0.02 = fast, 0.05 = slower)
    
    # Optional: delete the temporary "Preparing help..." part is already replaced by final text
    # No duplicate messages will be sent


# Added by VoidXTora 