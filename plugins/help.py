import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatAction
import logging

# Setup logging to catch any errors
logging.basicConfig(filename="bot_errors.log", level=logging.ERROR)

# Help text with a placeholder for user mention
HELP_TEXT = """⁉️ Hᴇʏ...!! {user_mention} ~

➪ I ᴀᴍ ᴀ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇ sʜᴀʀɪɴɢ ʙᴏᴛ, ᴍᴇᴀɴᴛ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ғɪʟᴇs ᴀɴᴅ ɴᴇᴄᴇssᴀʀʏ sᴛᴜғғ ᴛʜʀᴏᴜɢʜ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴄʜᴀɴɴᴇʟs.

➪ Iɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴀʟʟ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄʜᴀɴɴᴇʟ ᴛʜᴀᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛᴏ ᴊᴏɪɴ. Yᴏᴜ ᴄᴀɴ ɴᴏᴛ ᴀᴄᴄᴇss ᴏʀ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴜɴʟᴇss ʏᴏᴜ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴄʜᴀɴɴᴇʟs.

➪ Sᴏ ᴊᴏɪɴ Mᴇɴᴛɪᴏɴᴇᴅ Cʜᴀɴɴᴇʟs ᴛᴏ ɢᴇᴛ Fɪʟᴇs ᴏʀ ɪɴɪᴛɪᴀᴛᴇ ᴍᴇssᴀɢᴇs...

‣ /help - Oᴘᴇɴ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ !

◈ Sᴛɪʟʟ ʜᴀᴠᴇ ᴅᴏᴜʙᴛs, ᴄᴏɴᴛᴀᴄᴛ ʙᴇʟᴏᴡ ᴘᴇʀsᴏɴs/ɢʀᴏᴜᴘ ᴀs ᴘᴇʀ ʏᴏᴜʀ ɴᴇᴇᴅ !"""

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    user_mention = message.from_user.mention
    help_text = HELP_TEXT.format(user_mention=user_mention)

    # Show typing animation
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)

    # Start with a single dot to initialize the message
    typing_msg = await message.reply_text(".", quote=True)
    await asyncio.sleep(0.5)

    # Chunk typing logic
    text_to_send = ""
    last_sent_text = ""

    # Split help text into lines for smooth pauses
    lines = help_text.split("\n")
    for line in lines:
        # Type line in small character chunks
        for i in range(0, len(line), 5):  # 5 characters per edit
            chunk = line[:i+5]
            new_text = text_to_send + chunk
            if new_text != last_sent_text:
                try:
                    await typing_msg.edit_text(new_text)
                    last_sent_text = new_text
                except Exception as e:
                    logging.error(e)
            await asyncio.sleep(0.02)  # Typing speed per chunk
        text_to_send += line + "\n"
        await asyncio.sleep(0.2)  # Small pause between lines