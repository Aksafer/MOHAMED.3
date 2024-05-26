from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="ᘜᖇ᥆ᥙρ", url= "https://t.me/SOPER_EROR"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مـطـور الـسـورس", url= "https://t.me/Y_D_ll"),
            InlineKeyboardButton(text="ᘜᖇ᥆ᥙρ", url=f"https://t.me/SOPER_EROR"), 
        ],
        [
            
            InlineKeyboardButton(text="᥉᥆ᥙᖇᥴᥱ", url=f"https://t.me/SOURCE_EROR") , 
        ],
    ]
    return buttons
