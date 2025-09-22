import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot  # use your Bot instance

# ==== Configurable ====
HELP_IMAGE_URL = "https://graph.org/file/53bab5e049a9b0133c354-b8767e238320087219.jpg"

HELP_TEXT = """⁉️ Hᴇʏ...!! {user_mention} ~

➪ Mᴀɪɴ ᴇᴋ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇ sʜᴀʀɪɴɢ ʙᴏᴛ ʜᴜ, ᴊᴏ ᴀᴘᴋᴏ ғɪʟᴇs ᴀᴜʀ ᴅɪғғᴇʀᴇɴᴛ sᴛᴜғғ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ sᴇ ᴅᴇᴛᴀ ʜᴀɪ ғᴏʀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀɴɴᴇʟs.

➪ Fɪʟᴇ ʟᴇɴᴇ ᴋᴇ ʟɪʏᴇ ᴀᴘᴋᴏ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄʜᴀɴɴᴇʟs ᴊᴏɪɴ ᴋᴀʀɴᴀ ᴘᴀᴅᴇɢᴀ. Jᴀʙ ᴛᴀᴋ ᴀᴘ ᴀʟʟ ᴄʜᴀɴɴᴇʟs ᴊᴏɪɴ ɴᴀʜɪɴ ᴋᴀʀᴛᴇ, ғɪʟᴇ ᴀᴄᴄᴇss ɴᴀʜɪɴ ʜᴏɢᴀ.

➪ Isʟɪʏᴇ sᴀʀᴇ ᴄʜᴀɴɴᴇʟs ᴊᴏɪɴ ᴋᴀʀᴏ, ᴛᴀʙʜɪ ғɪʟᴇ ᴍɪʟᴇɢᴀ ʏᴀ ᴍᴇssᴀɢᴇs ɪɴɪᴛɪᴀᴛᴇ ʜᴏɴɢᴇ...

‣ /help - Yᴇʜ ʜᴇʟᴘ ᴍᴇɴᴜ ᴘʜɪʀ sᴇ ᴏᴘᴇɴ ᴋᴀʀᴏ !

◈ Aɢᴀʀ ᴀʙʜɪ ʙʜɪ ᴅᴏᴜʙᴛ ʜᴀɪ, ɴɪᴄʜᴇ ʙᴜᴛᴛᴏɴ sᴇ ᴄᴏɴᴛᴀᴄᴛ ᴋᴀʀᴏ..."""
# =====================

@Bot.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    user_mention = f"<a href='tg://user?id={message.from_user.id}'>➣ {message.from_user.first_name}</a>"

    # Step 1: Loading animation
    loading = await message.reply_text("Loading!")
    for dots in ["!!", "!!!", "!!!!", "!!!!!"]:
        await asyncio.sleep(0.5)
        await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
        await loading.edit_text(f"Loading{dots}")

    await asyncio.sleep(0.5)
    await loading.delete()

    # Step 2: Send help message with image + caption
    await client.send_photo(
        chat_id=message.chat.id,
        photo=HELP_IMAGE_URL,
        caption=HELP_TEXT.format(user_mention=user_mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👤 Owner", url="https://t.me/VoidXTora")],
                [InlineKeyboardButton("👨‍💻 Support", url="https://t.me/Anime_Talk_Mythic")],
            ]
        ),
        parse_mode="HTML"
    )