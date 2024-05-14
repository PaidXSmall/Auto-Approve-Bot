from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
import random, asyncio
from configs import cfg
    

 
app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)
 
ABOUT = """<b>
• 𝖬𝖺𝗁 𝖭𝖺𝗆𝖾: <a href='https://t.me/KaipullaNetworks_Bot'>𝖠𝗎𝗍𝗈 𝖠𝗉𝗉𝗋𝗈𝗏𝖾 𝖡𝗈𝗍</a>
• 𝖢𝗋𝖾𝖺𝗍𝗈𝗋: <a href='https://t.me/Abt_Kristy'>𝖪𝗋𝗂𝗌𝗍𝗒 கிறிஸ்டி | 🇮🇳 |</a>
• 𝖫𝗂𝖻𝗋𝖺𝗋𝗒: <a href='https://docs.pyrogram.org/'>𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖵2.0.106</a>
• 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾: <a href='https://www.python.org/download/releases/3.0/'>𝖯𝗒𝗍𝗁𝗈𝗇</a>
• 𝖣𝖡: <a href='https://www.mongodb.com/'>𝖬𝗈𝗇𝗀𝗈𝖣𝖡</a>
• 𝖡𝗈𝗍'𝗌 𝖲𝖾𝗋𝗏𝖾𝗋: <a href='https://heroku.com/'>𝖪𝗋𝗂𝗌𝗍𝗒'𝗌 𝖲𝖾𝗋𝗏𝖾𝗋</a>
• 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌: v2.7.2 [ 𝖪𝖷 ]</b>"""


gif = [
    'https://te.legra.ph/file/12fdf89910d7e87cc743a.mp4'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 𝖩𝗈𝗂𝗇 𝖡𝗈𝗍𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url="https://t.me/BotsXKristy"),
                        InlineKeyboardButton("𝖬𝗈𝗏𝗂𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 🎈", url="https://t.me/MadrasRockersTG")
                    ],
             

                    [
                        InlineKeyboardButton("🧩 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗍 🧩", url="https://t.me/KaipullaNetworks_Bot?startgroup")
                    ]
                ]
        )
        await app.send_video(kk.id,img, "** {} 𝖸𝗈𝗎𝗋 𝖩𝗈𝗂𝗇 𝖱𝖾𝗊 𝖶𝖺𝗌 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 𝖠𝗉𝗉𝗋𝗈𝗏𝖾𝖽 𝖡𝗒 𝖬𝖾 💌**".format(m.from_user.mention), reply_markup=keyboard)
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ About ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("about"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/c4ea3761bb73bab726334.jpg",caption=ABOUT,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="</> 𝖡𝗈𝗍𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url="t.me/BotsXKristy")]]))

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 𝖡𝗈𝗍𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url="https://t.me/BotsXKristy"),
                        InlineKeyboardButton("💬 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋", url="https://t.me/Kristy_TG")
                    ],
             

                    [
                        InlineKeyboardButton("🧩 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗍 🧩", url="https://t.me/KaipullaNetworks_Bot?startgroup")
                    ]
                ]
        )
            add_user(m.from_user.id)
            await m.reply_photo("https://te.legra.ph/file/80caa5d62b5dea231ac7d.jpg", caption="""**𝖧𝖾𝗒 𝖡𝗋𝗎𝗁𝗁! {}\n\n𝖨'𝗆 𝖺𝗇 𝖺𝗎𝗍𝗈 𝖺𝗉𝗉𝗋𝗈𝗏𝖾 𝖠𝖽𝗆𝗂𝗇 𝖩𝗈𝗂𝗇 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗌 𝖡𝗈𝗍.
\n𝖨 𝖼𝖺𝗇 𝖺𝗉𝗉𝗋𝗈𝗏𝖾 𝗎𝗌𝖾𝗋𝗌 𝗂𝗇 𝖦𝗋𝗈𝗎𝗉𝗌/𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌. \n𝖩𝗎𝗌𝗍 𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗍 𝖺𝗇𝖽 𝗉𝗋𝗈𝗆𝗈𝗍𝖾 𝗆𝖾 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 𝗐𝗂𝗍𝗁 𝖺𝖽𝖽 𝗆𝖾𝗆𝖻𝖾𝗋𝗌 𝗉𝖾𝗋𝗆𝗂𝗌𝗌𝗂𝗈𝗇.\n\n𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝖽 & 𝖬𝖺𝗂𝗇𝗍𝖺𝗂𝗇𝗀 𝖡𝗒: <a href=https://telegram.dog/Kristy_TG>𝖪𝗋𝗂𝗌𝗍𝗒 கிறிஸ்டி 🇮🇳</a></b> """.format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/{BOT_USERNAME}?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("*⚡️ Hello {}!\n Write me private for more details**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 Check Again 🍀", "chk")
                ]
            ]
        )
        await m.reply_text("**⚠️Access Denied!⚠️\n\nPlease Join @{} to use me.If you joined click check again button to confirm.** \n\n".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/EmoBotDevolopers"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/EmoBotSupport")
                    ],
                    [
                        InlineKeyboardButton("🧩 Repo 🧩", url="https://github.com/RishBropromax/Auto-Approve-Bot"),
                        InlineKeyboardButton("💻 Devoloper 💻", url="https://t.me/AboutRishmika")
                    ],
                    [
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/{BOT_USERNAME}?startgroup")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**⚡️ Hello {}!\n\nI m Auto Approve Bot.**\nI can approve users in Groups/Channels. Add me to your chat and promote me to admin with add members permission.\n\n⚡️Powerd By @EmoBotDevolopers**".format(cb.from_user.mention, "https://t.me/EmoBotDevolopers"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ You are not joined to channel join and try again. 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀

🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}`
💠 Programmer :- @AboutRishmika

""")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users. \n\n ⚠️ Warning :- Don't Boardcast Everyday ")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Fcast Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("Starting..")
print("Checking Code Erorrs..!")
print("Bot Running..")
print("Bot Started")
app.run()
