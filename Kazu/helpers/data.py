from pyrogram.types import InlineKeyboardButton

class Data:

    text_help_menu = ("modules:52"
        "**Command List & Help**\n**Prefixes:** ., ?, !, *"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("**ʀᴇ-ᴏᴘᴇɴ**", callback_data="reopen")]]
