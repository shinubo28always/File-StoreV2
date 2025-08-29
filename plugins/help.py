import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatAction, ParseMode

# ==== Configurable ====
HELP_IMAGE_URL = "https://graph.org/file/53bab5e049a9b0133c354-b8767e238320087219.jpg"  # <- replace with your image

HELP_TEXT = """⁉️ Hᴇʏ...!! {user_mention} ~

➪ I ᴀᴍ ᴀ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇ sʜᴀʀɪɴɢ ʙᴏᴛ, ᴍᴇᴀɴᴛ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ғɪʟᴇs ᴀɴᴅ ɴᴇᴄᴇssᴀʀʏ sᴛᴜғғ ᴛʜʀᴏᴜɢʜ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴄʜᴀɴɴᴇʟs.

➪ Iɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴀʟʟ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄʜᴀɴɴᴇʟ ᴛʜᴀᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛᴏ ᴊᴏɪɴ. Yᴏᴜ ᴄᴀɴ ɴᴏᴛ ᴀᴄᴄᴇss ᴏʀ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴜɴʟᴇss ʏᴏᴜ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴄʜᴀɴɴᴇʟs.

➪ Sᴏ ᴊᴏɪɴ Mᴇɴᴛɪᴏɴᴇᴅ Cʜᴀɴɴᴇʟs ᴛᴏ ɢᴇᴛ Fɪʟᴇs ᴏʀ ɪɴɪᴛɪᴀᴛᴇ ᴍᴇssᴀɢᴇs...

‣ /help - Oᴘᴇɴ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ !

◈ Sᴛɪʟʟ ʜᴀᴠᴇ ᴅᴏᴜʙᴛs, ᴄᴏɴᴛᴀᴄᴛ ʙᴇʟᴏᴡ ᴘᴇʀsᴏɴs/ɢʀᴏᴜᴘ ᴀs ᴘᴇʀ ʏᴏᴜʀ ɴᴇᴇᴅ !"""
# =====================

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    # Show typing while we display a temporary loader
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)

    # Temporary loading effect (exactly as requested)
    loader = await message.reply_text("!!!!!!!", quote=True)

    # Small effect delay (tweak if you want)
    await asyncio.sleep(1.2)

    # Try deleting the user's /help command (Telegram doesn't allow deleting user messages in private chats)
    try:
        await message.delete()
    except Exception:
        pass  # Ignored if not permitted

    # Delete the loader we sent
    try:
        await loader.delete()
    except Exception:
        pass

    # Build a safe clickable mention for Markdown
    user = message.from_user
    user_mention = f"[{user.first_name}](tg://user?id={user.id})"

    caption = HELP_TEXT.format(user_mention=user_mention)

    # Inline buttons
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Owner", url="https://t.me/VoidXTora")],
            [InlineKeyboardButton("👨‍💻 Support", url="https://t.me/Anime_Talk_Mythic")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
    )

    # Optional: show typing again just before sending the final help
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)

    # Send final Help: image + caption + buttons (all at once)
    await client.send_photo(
        chat_id=message.chat.id,
        photo=HELP_IMAGE_URL,
        caption=caption,
        reply_markup=buttons,
        parse_mode=ParseMode.MARKDOWN
    )