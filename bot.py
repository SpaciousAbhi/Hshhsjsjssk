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
        caption_text = """🎬 𝗪𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀?

👉 𝗛𝗼𝘄 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱:

1️⃣ 𝗝𝗼𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗹𝗶𝗻𝗸 𝗯𝗲𝗹𝗼𝘄.
2️⃣ 𝗧𝘆𝗽𝗲 𝘁𝗵𝗲 𝗻𝗮𝗺𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱.
3️⃣ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲𝘀 𝘀𝗵𝗮𝗿𝗲𝗱 𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽.

✅ 𝗙𝗼𝗹𝗹𝗼𝘄 𝘁𝗵𝗲𝘀𝗲 𝘀𝘁𝗲𝗽𝘀 𝗮𝗻𝗱 𝗴𝗲𝘁 𝘆𝗼𝘂𝗿 𝗺𝗼𝘃𝗶𝗲𝘀/𝘀𝗲𝗿𝗶𝗲𝘀.

💥 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗶𝗻: 480p, 720p, 1080p, Full HD
🌐 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲𝘀: Hindi, English, Tamil, Telugu, Kannada, Malayalam"""

        # Inline buttons with updated labels
        buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("✅ 𝗠𝗢𝗩𝗜𝗘 𝗚𝗥𝗢𝗨𝗣 𝗟𝗜𝗡𝗞 ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                [InlineKeyboardButton("✅ 𝗠𝗢𝗩𝗜𝗘 𝗚𝗥𝗢𝗨𝗣 𝗟𝗜𝗡𝗞 ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                [InlineKeyboardButton("✅ 𝗠𝗢𝗩𝗜𝗘 𝗚𝗥𝗢𝗨𝗣 𝗟𝗜𝗡𝗞 ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")]
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
                        InlineKeyboardButton("🗯 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/Venom_Stone_Movies_Official"),
                        InlineKeyboardButton("💬 𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/IAmVenomStone")
                    ],
                    [
                        InlineKeyboardButton("➕ 𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗖𝗵𝗮𝘁 ➕", url="https://t.me/VenomStoneAutoApproveBot?startgroup")
                    ]
                ]
            )

            # Caption text
            caption_text = """🎬 𝗪𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀?

👉 𝗛𝗼𝘄 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱:

1️⃣ 𝗝𝗼𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗹𝗶𝗻𝗸 𝗯𝗲𝗹𝗼𝘄.
2️⃣ 𝗧𝘆𝗽𝗲 𝘁𝗵𝗲 𝗻𝗮𝗺𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱.
3️⃣ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲𝘀 𝘀𝗵𝗮𝗿𝗲𝗱 𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽.

✅ 𝗙𝗼𝗹𝗹𝗼𝘄 𝘁𝗵𝗲𝘀𝗲 𝘀𝘁𝗲𝗽𝘀 𝗮𝗻𝗱 𝗴𝗲𝘁 𝘆𝗼𝘂𝗿 𝗺𝗼𝘃𝗶𝗲𝘀/𝘀𝗲𝗿𝗶𝗲𝘀.

💥 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗶𝗻: 480p, 720p, 1080p, Full HD
🌐 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲𝘀: Hindi, English, Tamil, Telugu, Kannada, Malayalam"""

            # Inline buttons for the group links
            group_buttons = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✅ 𝗠𝗢𝗩𝗜𝗘 𝗚𝗥𝗢𝗨𝗣 𝗟𝗜𝗡𝗞 ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                    [InlineKeyboardButton("✅ 𝗠𝗢𝗩𝗜𝗘 𝗚𝗥𝗢𝗨𝗣 𝗟𝗜𝗡𝗞 ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                    [InlineKeyboardButton("✅ 𝗠𝗢𝗩𝗜𝗘 𝗚𝗥𝗢𝗨𝗣 𝗟𝗜𝗡𝗞 ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")]
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
                        InlineKeyboardButton("💁‍♂️ 𝗦𝘁𝗮𝗿𝘁 𝗺𝗲 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 💁‍♂️", url="https://t.me/VenomStoneAutoApproveBot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text(
                "**🦊 𝗛𝗲𝗹𝗹𝗼 {}!\n𝗪𝗿𝗶𝘁𝗲 𝗺𝗲 𝗽𝗿𝗶𝘃𝗮𝘁𝗲 𝗳𝗼𝗿 𝗺𝗼𝗿𝗲 𝗱𝗲𝘁𝗮𝗶𝗹𝘀**".format(m.from_user.first_name),
                reply_markup=keyboar
            )
        print(m.from_user.first_name + " 𝗜𝘀 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 𝗬𝗼𝘂𝗿 𝗕𝗼𝘁!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 𝗖𝗵𝗲𝗰𝗸 𝗔𝗴𝗮𝗶𝗻 🍀", "chk")
                ]
            ]
        )
        await m.reply_text(
            "**⚠️ 𝗔𝗰𝗰𝗲𝘀𝘀 𝗗𝗲𝗻𝗶𝗲𝗱! ⚠️\n\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗝𝗼𝗶𝗻 @{} 𝘁𝗼 𝘂𝘀𝗲 𝗺𝗲. 𝗜𝗳 𝘆𝗼𝘂 𝗷𝗼𝗶𝗻𝗲𝗱, 𝗰𝗹𝗶𝗰𝗸 𝗰𝗵𝗲𝗰𝗸 𝗮𝗴𝗮𝗶𝗻 𝗯𝘂𝘁𝘁𝗼𝗻 𝘁𝗼 𝗰𝗼𝗻𝗳𝗶𝗿𝗺.**".format(cfg.FSUB),
            reply_markup=key
        )

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import enums

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb: CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            # Inline keyboard for other links
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url="https://t.me/Venom_Stone_Movies_Official"),
                        InlineKeyboardButton("💬 𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/IAmVenomStone")
                    ],
                    [
                        InlineKeyboardButton("➕ 𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗖𝗵𝗮𝘁 ➕", url="https://t.me/VenomStoneAutoApproveBot?startgroup")
                    ]
                ]
            )

            # Caption / explanatory text
            caption_text = """🎬 𝗪𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀?

👉 𝗛𝗼𝘄 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱:

1️⃣ 𝗝𝗼𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽 𝘂𝘀𝗶𝗻𝗴 𝘁𝗵𝗲 𝗹𝗶𝗻𝗸 𝗯𝗲𝗹𝗼𝘄.
2️⃣ 𝗧𝘆𝗽𝗲 𝘁𝗵𝗲 𝗻𝗮𝗺𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱.
3️⃣ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲𝘀 𝘀𝗵𝗮𝗿𝗲𝗱 𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽.

✅ 𝗙𝗼𝗹𝗹𝗼𝘄 𝘁𝗵𝗲𝘀𝗲 𝘀𝘁𝗲𝗽𝘀 𝗮𝗻𝗱 𝗴𝗲𝘁 𝘆𝗼𝘂𝗿 𝗺𝗼𝘃𝗶𝗲𝘀/𝘀𝗲𝗿𝗶𝗲𝘀.

💥 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗶𝗻: 480p, 720p, 1080p, Full HD
🌐 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲𝘀: Hindi, English, Tamil, Telugu, Kannada, Malayalam"""

            # Inline buttons for the group links
            group_buttons = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✅ 𝗠𝗢𝗩𝗜𝗘 𝗚𝗥𝗢𝗨𝗣 𝗟𝗜𝗡𝗞 ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                    [InlineKeyboardButton("✅ 𝗠𝗢𝗩𝗜𝗘 𝗚𝗥𝗢𝗨𝗣 𝗟𝗜𝗡𝗞 ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")],
                    [InlineKeyboardButton("✅ 𝗠𝗢𝗩𝗜𝗘 𝗚𝗥𝗢𝗨𝗣 𝗟𝗜𝗡𝗞 ✅", url="https://t.me/+OXGKooMMA_U0Yjg1")]
                ]
            )

            add_user(cb.from_user.id)
            # Edit message with new text and inline buttons
            await cb.message.edit(
                caption_text,
                reply_markup=group_buttons,
                disable_web_page_preview=True
            )

        print(cb.from_user.first_name + " 𝗜𝘀 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 𝗬𝗼𝘂𝗿 𝗕𝗼𝘁!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗷𝗼𝗶𝗻𝗲𝗱 𝘁𝗼 𝘁𝗵𝗲 𝗰𝗵𝗮𝗻𝗻𝗲𝗹. 𝗝𝗼𝗶𝗻 𝗮𝗻𝗱 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻! 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m: Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 𝗖𝗵𝗮𝘁𝘀 𝗦𝘁𝗮𝘁𝘀 🍀
🙋‍♂️ 𝗨𝘀𝗲𝗿𝘀 : `{xx}`
👥 𝗚𝗿𝗼𝘂𝗽𝘀 : `{x}`
🚧 𝗧𝗼𝘁𝗮𝗹 𝗨𝘀𝗲𝗿𝘀 & 𝗚𝗿𝗼𝘂𝗽𝘀 : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success += 1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated += 1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked += 1
        except Exception as e:
            print(e)
            failed += 1

    await lel.edit(f"✅ 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹 𝘁𝗼 `{success}` 𝗨𝘀𝗲𝗿𝘀.\n❌ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 `{failed}` 𝗨𝘀𝗲𝗿𝘀.\n👾 𝗕𝗹𝗼𝗰𝗸𝗲𝗱 : `{blocked}` 𝗨𝘀𝗲𝗿𝘀 \n👻 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲𝗱 : `{deactivated}` 𝗨𝘀𝗲𝗿𝘀.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m: Message):
    allusers = users
    lel = await m.reply_text("`⚡️ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success += 1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated += 1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked += 1
        except Exception as e:
            print(e)
            failed += 1

    await lel.edit(f"✅ 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹 𝘁𝗼 `{success}` 𝗨𝘀𝗲𝗿𝘀.\n❌ 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 `{failed}` 𝗨𝘀𝗲𝗿𝘀.\n👾 𝗕𝗹𝗼𝗰𝗸𝗲𝗱 : `{blocked}` 𝗨𝘀𝗲𝗿𝘀 \n👻 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲𝗱 : `{deactivated}` 𝗨𝘀𝗲𝗿𝘀.")

print("🚀 𝗜'𝗺 𝗔𝗹𝗶𝘃𝗲 𝗡𝗼𝘄!")
app.run()
