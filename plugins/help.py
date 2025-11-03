import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot  # your bot instance
from pyrogram.enums import ParseMode


HELP_IMAGE_URL = "https://graph.org/file/468ced08a20ce21d2794d-94b1a5448990e4b683.jpg"

HELP_TEXT = """🥰 Kon’nichiwa {user_mention}! ~

⚔️ I’ᴍ ᴀɴ ᴀɴɪᴍᴇ-ᴛʜᴇᴍᴇᴅ ғɪʟᴇ ʙᴏᴛ 🎥
Bᴏʀɴ ɪɴ ᴛʜᴇ ʀᴇᴀʟᴍ ᴏғ ᴅᴀᴛᴀ ᴀɴᴅ ᴄᴏᴅᴇ, I sᴇʀᴠᴇ ᴛᴏ ᴅᴇʟɪᴠᴇʀ sᴘᴇᴄɪᴀʟ ᴀɴɪᴍᴇ ғɪʟᴇs ᴛᴏ ᴛʜᴇ ᴡᴏʀᴛʜʏ ⚡

💮 Tᴏ ᴀᴄᴄᴇss ᴍʏ sᴇᴄʀᴇᴛ ᴀʀᴄʜɪᴠᴇs, ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴀʟʟ ᴛʜᴇ ᴀʟʟɪᴇᴅ ᴄʜᴀɴɴᴇʟs 🎯
Oɴʟʏ ᴛʜᴇɴ ᴛʜᴇ ᴘᴏʀᴛᴀʟ ᴡɪʟʟ ᴏᴘᴇɴ 🔓

🌌 Oɴᴄᴇ ʏᴏᴜ’ʀᴇ ɪɴ, ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʀᴇᴠᴇᴀʟ ᴛʜᴇɪʀ ᴛʀᴜᴛʜ 💫
Aɴɪᴍᴇ sᴘɪʀɪᴛs ᴀʀᴇ ᴡᴀɪᴛɪɴɢ ғᴏʀ ʏᴏᴜ 🌀

‣ /help – Sᴜᴍᴍᴏɴ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ 📜
◈ Nᴇᴇᴅ ᴀssɪsᴛᴀɴᴄᴇ? Cᴏɴᴛᴀᴄᴛ ᴍʏ Mᴀsᴛᴇʀ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ⚙️"""
# =====================

@Bot.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    user_mention = f"<a href='tg://user?id={message.from_user.id}'>➣ {message.from_user.first_name}</a>"

    # Step 1: Loading animation
    loading = await message.reply_text("Loading!")
    for dots in ["!!", "!!!", "!!!!", "!!!!!"]:
        await asyncio.sleep(0.5)
        await client.send_chat_action(message.chat.id, enums.ChatAction.PLAYING)
        await loading.edit_text(f"Loading{dots}")

    await asyncio.sleep(0.5)
    await loading.delete()

    # Step 2: Send help message
    await client.send_photo(
        chat_id=message.chat.id,
        photo=HELP_IMAGE_URL,
        caption=HELP_TEXT.format(user_mention=user_mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👤 Owner", url="https://t.me/AniReal_Support")],
                [InlineKeyboardButton("👨‍💻 Support", url="https://t.me/AniReal_Chat_Group_Asia")],
            ]
        ),
        parse_mode=ParseMode.HTML
    )
