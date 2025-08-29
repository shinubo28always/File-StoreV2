import asyncio
import contextlib
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatAction, ParseMode

# ==== Configurable ====
HELP_IMAGE_URL = "https://graph.org/file/53bab5e049a9b0133c354-b8767e238320087219.jpg"

HELP_TEXT = """⁉️ Hᴇʏ...!! {user_mention} ~

➪ I ᴀᴍ ᴀ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇ sʜᴀʀɪɴɢ ʙᴏᴛ, ᴍᴇᴀɴᴛ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ғɪʟᴇs ᴀɴᴅ ɴᴇᴄᴇssᴀʀʏ sᴛᴜғғ ᴛʜʀᴏᴜɢʜ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴄʜᴀɴɴᴇʟs.

➪ Iɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴀʟʟ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄʜᴀɴɴᴇʟ ᴛʜᴀᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛᴏ ᴊᴏɪɴ. Yᴏᴜ ᴄᴀɴ ɴᴏᴛ ᴀᴄᴄᴇss ᴏʀ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴜɴʟᴇss ʏᴏᴜ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴄʜᴀɴɴᴇʟs.

➪ Sᴏ ᴊᴏɪɴ Mᴇɴᴛɪᴏɴᴇᴅ Cʜᴀɴɴᴇʟs ᴛᴏ ɢᴇᴛ Fɪʟᴇs ᴏʀ ɪɴɪᴛɪᴀᴛᴇ ᴍᴇssᴀɢᴇs...

‣ /help - Oᴘᴇɴ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ !

◈ Sᴛɪʟʟ ʜᴀᴠᴇ ᴅᴏᴜʙᴛs, ᴄᴏɴᴛᴀᴄᴛ ʙᴇʟᴏᴡ ᴘᴇʀsᴏɴs/ɢʀᴏᴜᴘ ᴀs ᴘᴇʀ ʏᴏᴜʀ ɴᴇᴇᴅ !"""
# =====================

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    # Step 1: Show typing & send fake loading
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    loader = await message.reply_text("!!!!!!!", quote=True)

    # Step 2: Keep "typing…" while loader is visible
    for _ in range(3):  # ~3 seconds total
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        await asyncio.sleep(1)

    # Step 3: Delete /help message (if possible) and loader
    with contextlib.suppress(Exception):
        await message.delete()
    with contextlib.suppress(Exception):
        await loader.delete()

    # Step 4: Final caption with user mention
    caption = HELP_TEXT.format(user_mention=message.from_user.mention)

    # Step 5: Inline buttons
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Owner", url="https://t.me/VoidXTora")],
            [InlineKeyboardButton("👨‍💻 Support", url="https://t.me/Anime_Talk_Mythic")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
    )

    # Step 6: Keep typing just before sending final help
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)

    # Step 7: Send help image + text + buttons
    await client.send_photo(
        chat_id=message.chat.id,
        photo=HELP_IMAGE_URL,
        caption=caption,
        reply_markup=buttons,
        parse_mode=ParseMode.MARKDOWN
    )