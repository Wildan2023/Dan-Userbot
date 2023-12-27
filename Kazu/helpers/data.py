from pyrogram.types import InlineKeyboardButton

class Data:

    text_help_menu = (
        "**Command List & Help**\n**Prefixes:**Modules:52 ., ?, !, *"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("**ʀᴇ-ᴏᴘᴇɴ**", callback_data="reopen")]]
