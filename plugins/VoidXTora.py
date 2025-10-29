# VoidXTora.py

from config import OWNER_ID, USER_REPLY_TEXT, USER_ROAST_TEXT
from database.database import db


# ✅ Check if user is the owner
async def is_owner(user_id: int) -> bool:
    return user_id == OWNER_ID


# ✅ Check if user is in admin database
async def is_admin(user_id: int) -> bool:
    admin_ids = await db.get_all_admins()
    return user_id in admin_ids


# ✅ For owner-only commands
async def check_owner_only(message):
    if not await is_owner(message.from_user.id):
        await message.reply(USER_REPLY_TEXT, quote=True)
        return False
    return True


# ✅ For owner + admins commands
async def check_admin_or_owner(message):
    if await is_owner(message.from_user.id) or await is_admin(message.from_user.id):
        return True
    await message.reply(USER_REPLY_TEXT, quote=True)
    return False


# ✅ For owner + admins special commands
async def voidRoast(message):
    if await is_owner(message.from_user.id) or await is_admin(message.from_user.id):
        return True
    await message.reply(USER_ROAST_TEXT,
 quote=True)
    return False


#=====================================================================================##
# Credits:- @VoidXTora
# Maintained by: Mythic_Bots
# Support: @MythicBot_Support
#=====================================================================================##
#This file is part of MythicBots Project.#
