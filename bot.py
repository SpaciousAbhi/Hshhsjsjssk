from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://telegra.ph/file/eb119179b4d2a13e71163.jpg',
    'https://telegra.ph/file/eb119179b4d2a13e71163.jpg',
    'https://telegra.ph/file/eb119179b4d2a13e71163.jpg',
    'https://telegra.ph/file/eb119179b4d2a13e71163.jpg'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m: Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)

        # Caption text
        caption_text = """🎬 Want to download any movie or series?

👉 Steps to download:

1. Click on the group link below and join the group.
2. Type the name of the movie or series you want to download and send it.
4. Download the files shared in the group.

✅ It’s very easy! Just follow these steps and get your movies/series.

💥 Available in: 480p, 720p, 1080p, Full HD
🌐 Languages: Hindi, English, Tamil, Telugu, Kannada, Malayalam"""

        # Inline buttons with updated labels
        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("✅ GROUP LINK ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                [InlineKeyboardButton("✅ GROUP LINK ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                [InlineKeyboardButton("✅ GROUP LINK ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")]
            ]
        )

        # Send video with caption and buttons
        await app.send_video(kk.id, img, caption=caption_text, reply_markup=buttons)

        add_user(kk.id)
    except Exception as err:
        print(str(err))
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import enums

@app.on_message(filters.command("start"))
async def op(_, m: Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            # Inline keyboard for other links
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/Venom_Stone_Movies_Official"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/IAmVenomStone")
                    ],
                    [
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/VenomStoneAutoApproveBot?startgroup")
                    ]
                ]
            )

            # Caption text
            caption_text = """🎬 Want to download any movie or series?

👉 Steps to download:

1. Click on the group link below and join the group.
2. Type the name of the movie or series you want to download and send it.
4. Download the files shared in the group.

✅ It’s very easy! Just follow these steps and get your movies/series.

💥 Available in: 480p, 720p, 1080p, Full HD
🌐 Languages: Hindi, English, Tamil, Telugu, Kannada, Malayalam"""

            # Inline buttons for the group links
            group_buttons = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✅ GROUP LINK ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                    [InlineKeyboardButton("✅ GROUP LINK ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                    [InlineKeyboardButton("✅ GROUP LINK ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")]
                ]
            )

            add_user(m.from_user.id)
            # Send photo with caption and inline buttons
            await m.reply_photo(
                "https://telegra.ph/file/eb119179b4d2a13e71163.jpg",
                caption=caption_text,
                reply_markup=group_buttons
            )

        elif m.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/VenomStoneAutoApproveBot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text(
                "**🦊 Hello {}!\nwrite me private for more details**".format(m.from_user.first_name),
                reply_markup=keyboar
            )
        print(m.from_user.first_name + " Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 Check Again 🍀", "chk")
                ]
            ]
        )
        await m.reply_text(
            "**⚠️Access Denied!⚠️\n\nPlease Join @{} to use me.If you joined click check again button to confirm.**".format(cfg.FSUB),
            reply_markup=key
        )

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/Venom_Stone_Movies_Official"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/IAmVenomStone")
                    ],[
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/VenomStoneAutoApproveBot?startgroup")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By : @Venom_Stone_Movies_Official__**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
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
🚧 Total users & groups : `{tot}` """)

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

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
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

print("I'm Alive Now!")
app.run()
