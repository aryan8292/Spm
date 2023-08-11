from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("😎ᴄᴏᴍᴍᴀɴᴅs😎", data="help_back")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"𝙰𝙿𝙽𝙰 𝙺𝙰𝙼 𝙺𝚁𝙾 𝙽𝙰 𝙱𝙷𝙸"
        TEXT += f"ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ARY](https://t.me/ARY_BOTZ)**\n\n"
           await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/ffc3ef60523c4ae56f6dc.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
