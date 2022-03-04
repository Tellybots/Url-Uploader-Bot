# (c) @Tellybots

import asyncio
from plugins.database.database import db
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def OpenSettings(event: Message, user_id: int):
    try:
        await event.edit(
            text="**⚙ Configure My Behaviour**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(f"🔰 Upload as {'File 🗃️' if ((await db.get_upload_as_doc(user_id)) is True) else 'Video 🎥'}",
                                          callback_data="triggerUploadMode")],
                    [InlineKeyboardButton("🌆 Custom Thumbnail ", callback_data="triggerThumbnail")],
                    [InlineKeyboardButton("⛔ Close Settings", callback_data="close")]
                ]
            )
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await OpenSettings(event, user_id)
    except MessageNotModified:
        pass
