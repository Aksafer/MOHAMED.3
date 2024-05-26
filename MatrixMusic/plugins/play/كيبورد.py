import asyncio
from pyrogram import Client, filters
from strings.filters import command
from MatrixMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "🧑🏻‍✈️︙اهلا بك بك عزيزي العضو ♥️\n\n اليـكـ كـيب الاعـضاء الـخاص بــ سورس ايـرور"




REPLY_MESSAGE_BUTTONS = [
    [
        ("المطور"),
        ("مطور السورس")
    ],
    
    [
        ("السورس"),
        ("الاوامر")
    ],
    [
        ("استوري"),
        ("اقتباس")
    ],
   
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("نكته"),
        ("احكام")
    ],
    [
        ("متحركه"),
        ("انمي")
    ],
    [
        ("فيلم"),
        ("قران")
    ],    
    [
        ("انصحني"),
        ("لو خيروك")
    ],
    [
        ("نقشبندي"),
        ("عبد الباسط")
    ],
    [
        ("حروف"),
        ("سوال")
    ],
    [
        ("كتابات"),
        ("اذكار")
    ],
    [
        ("غنيلي"),
        ("تلاوات")
    ],
    [
        ("افاتار شباب"),
        ("افاتار بنات")
    ],
    [
        ("❎ ¦ حذف الكيبورد")
    ]
  
]



  

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("❎ ¦ حذف الكيبورد"))
async def down(client, message):
          m = await message.reply("❎ ¦ تم حذف الكيبورد بنجاح", reply_markup= ReplyKeyboardRemove(selective=True))

