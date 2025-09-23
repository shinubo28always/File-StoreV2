# Don't Remove Credit @VoidXTora
# Ask Doubt on telegram @MythicBot_Support


import asyncio
import os
import random
import sys
import time
from datetime import datetime, timedelta
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode, ChatAction
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, ChatInviteLink, ChatPrivileges
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserNotParticipant
from bot import Bot
from config import *
from helper_func import *
from database.database import *
from plugins.VoidXTora import check_owner_only, check_admin_or_owner


#BAN-USER-SYSTEM
@Bot.on_message(filters.private & filters.command("ban"))
async def add_banuser(client: Client, message: Message):  
    # ✅ Custom check for ban command
    if not await voidRoast(message):
        #await message.reply(
         #   "ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ᴛᴏ ʙᴀɴ ᴀɴʏᴏɴᴇ? Kɴᴏᴡ ʏᴏᴜʀ ᴘʟᴀᴄᴇ ғɪʀsᴛ.",
        #    quote=True
      #  )
        return      

    pro = await message.reply("⏳ <i>Processing request...</i>", quote=True)
    banuser_ids = await db.get_ban_users()
    banusers = message.text.split()[1:]

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]])

    if not banusers:
        return await pro.edit(
            "<b>❗ Provide user IDs to ban.</b>\n\n"
            "<b>Usage:</b>\n"
            "<code>/ban [user_id]</code> — Ban one or more users by ID.",
            reply_markup=reply_markup
        )

    report, success_count = "", 0
    for uid in banusers:
        try:
            uid_int = int(uid)
        except:
            report += f"⚠️ Invalid ID: <code>{uid}</code>\n"
            continue

        if uid_int in await db.get_all_admins() or uid_int == OWNER_ID:
            report += f"⛔ Skipped admin/owner: <code>{uid_int}</code>\n"
            continue

        if uid_int in banuser_ids:
            report += f"⚠️ Already banned: <code>{uid_int}</code>\n"
            continue

        await db.add_ban_user(uid_int)
        report += f"✅ Banned: <code>{uid_int}</code>\n"
        success_count += 1

    await pro.edit(
        f"<b>✅ Ban List Updated:</b>\n\n{report}" if success_count else f"<b>❌ No users banned.</b>\n\n{report}",
        reply_markup=reply_markup
    )

# Unban
@Bot.on_message(filters.private & filters.command("unban"))
async def delete_banuser(client: Client, message: Message): 
    if not await check_admin_or_owner(message):
        return
    pro = await message.reply("⏳ <i>Processing...</i>", quote=True)
    banuser_ids = await db.get_ban_users()
    banusers = message.text.split()[1:]

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]])

    if not banusers:
        return await pro.edit(
            "<b>❗ Provide user IDs to unban.</b>\n\n"
            "<b>Usage:</b>\n"
            "<code>/unban [user_id]</code> — Unban specific user(s)\n"
            "<code>/unban all</code> — Remove all banned users",
            reply_markup=reply_markup
        )

    if banusers[0].lower() == "all":
        if not banuser_ids:
            return await pro.edit("<b>✅ No banned users.</b>", reply_markup=reply_markup)
        for uid in banuser_ids:
            await db.del_ban_user(uid)
        listed = "\n".join([f"✅ Unbanned: <code>{uid}</code>" for uid in banuser_ids])
        return await pro.edit(f"<b>🚫 Cleared Ban List:</b>\n\n{listed}", reply_markup=reply_markup)

    report = ""
    for uid in banusers:
        try:
            uid_int = int(uid)
        except:
            report += f"⚠️ Invalid ID: <code>{uid}</code>\n"
            continue

        if uid_int in banuser_ids:
            await db.del_ban_user(uid_int)
            report += f"✅ Unbanned: <code>{uid_int}</code>\n"
        else:
            report += f"⚠️ Not in ban list: <code>{uid_int}</code>\n"

    await pro.edit(f"<b>🚫 Unban Report:</b>\n\n{report}", reply_markup=reply_markup)

# Ban list
@Bot.on_message(filters.private & filters.command("banlist"))
async def get_banuser_list(client: Client, message: Message): 
    if not await check_admin_or_owner(message):
        return       
    pro = await message.reply("⏳ <i>Fetching Ban List...</i>", quote=True)
    banuser_ids = await db.get_ban_users()

    if not banuser_ids:
        return await pro.edit("<b>✅ No users in the ban list.</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]]))

    result = "<b>🚫 Banned Users:</b>\n\n"
    for uid in banuser_ids:
        await message.reply_chat_action(ChatAction.PLAYING_GAME)  # ✅ Fixed
        try:
            user = await client.get_users(uid)
            user_link = f'<a href="tg://user?id={uid}">{user.first_name}</a>'
            result += f"• {user_link} — <code>{uid}</code>\n"
        except:
            result += f"• <code>{uid}</code> — <i>Unknown</i>\n"

    await pro.edit(result, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]]))