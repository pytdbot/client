from pytdbot import Client
from pytdbot.exception import StopHandlers
from pytdbot.types import (
    LogStreamFile,
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ShowKeyboardButton,
    ShowKeyboardMarkup,
    ForceReply,
    RemoveKeyboard,
)
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s]  %(message)s",
)

client = Client(
    api_id=0,  # Your api_id. You can get it from https://my.telegram.org/
    api_hash="API_HASH",  # Your api_hash. You can get it from https://my.telegram.org/
    database_encryption_key="1234echobot$",  # Your database encryption key
    token="1088394097:AAQX2DnWiw4ihwiJUhIHOGog8gGOI",  # Your bot token. You can get it from https://t.me/botfather
    files_directory="BotDB",  # Path where to store TDLib files
    workers=2,  # Number of workers
    td_verbosity=2,  # TDLib verbosity level
    td_log=LogStreamFile("tdlib.log"),  # Set TDLib log file path
)


@client.on_updateNewMessage()
async def start(c: Client, message: Update):
    if message.text == "/start":
        text = "Hello {}!\n".format(await message.mention("markdown"))
        text += "Here is some bot commands:\n\n"
        text += "- /keyboard - show keyboard\n"
        text += "- /inline - show inline keyboard\n"
        text += "- /remove - remove keyboard\n"
        text += "- /force - force reply"

        await message.reply_text(
            text,
            parse_mode="markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton.url(
                            "GitHub", "https://github.com/pytdbot/client"
                        )
                    ]
                ]
            ),
        )


@client.on_updateNewMessage()
async def commands(c: Client, message: Update):
    if message.text == "/inline":
        await message.reply_text(
            "This is a Inline keyboard",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton.callback("OwO", "OwO"),
                        InlineKeyboardButton.callback("UwU", "UwU"),
                    ],
                ]
            ),
        )
    elif message.text == "/keyboard":
        await message.reply_text(
            "This is a keyboard",
            reply_markup=ShowKeyboardMarkup(
                [
                    [ShowKeyboardButton.text("OwO"), ShowKeyboardButton.text("UwU")],
                ],
                one_time=True,
                resize_keyboard=True,
            ),
        )
    elif message.text == "/remove":
        await message.reply_text(
            "Keyboards removed",
            reply_markup=RemoveKeyboard(),
        )
    elif message.text == "/force":
        await message.reply_text(
            "This is a force reply",
            reply_markup=ForceReply(),
        )
    elif message.text:
        if "/start" not in message.text:
            await message.reply_text('You said "{}"'.format(message.text))


@client.on_updateNewCallbackQuery()
async def callback_query(c: Client, message: Update):
    if message.data:
        await c.editTextMessage(
            message.chat_id,
            message.message_id,
            "You pressed {}".format(message.data),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton.url(
                            "GitHub", "https://github.com/pytdbot/client"
                        )
                    ]
                ]
            ),
        )


# Run the client
client.run()
