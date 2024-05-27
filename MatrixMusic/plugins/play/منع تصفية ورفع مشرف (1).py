
from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus , ChatType
from pyrogram.types import ChatPermissions, ChatPrivileges
import asyncio
from MatrixMusic import app




#by > ####


welcome_enabled = True






@app.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    if not welcome_enabled:
        return
    
    if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"⎉︙المستخدم {user.username} ({user.first_name}) تم طرده من الجروب بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"━━━━━✯𝐒𝐎𝐔𝐑𝐂𝐄 𝐄𝐑𝐎𝐑 ✯━━━━━\n⎉︙تـم طـرد الـعـضـو @{user.username}\n⎉︙بـواسـطـة @{kicked_by.username}\n⎉︙تـم حـظـر الـمـسـتـخدام بـي نـجـاح ✅"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\n {str(e)}"
            else:
                message = f"⎉︙المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"
            
            
        
        await client.send_message(chat_member_updated.chat.id, message)




