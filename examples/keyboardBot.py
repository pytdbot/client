from pytdbot import Client, types
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
    td_log=types.LogStreamFile("tdlib.log"),  # Set TDLib log file path
)


@client.on_message()
async def start(c: Client, message: types.Message):
    if message.text == "/start":
        text = "Hello {}!\n".format(await message.mention("html"))
        text += "Here is some bot commands:\n\n"
        text += "- /keyboard - show keyboard\n"
        text += "- /inline - show inline keyboard\n"
        text += "- /remove - remove keyboard\n"
        text += "- /force - force reply"

        await message.reply_text(
            text,
            reply_markup=types.ReplyMarkupInlineKeyboard(
                [
                    [
                        types.InlineKeyboardButton(
                            text="GitHub",
                            type=types.InlineKeyboardButton(
                                "https://github.com/pytdbot/client"
                            ),
                        )
                    ]
                ]
            ),
        )


@client.on_message()
async def commands(c: Client, message: types.Message):
    if message.text == "/inline":
        await message.reply_text(
            "This is a Inline keyboard",
            reply_markup=types.ReplyMarkupInlineKeyboard(
                [
                    [
                        types.InlineKeyboardButton(
                            text="OwO",
                            type=types.InlineKeyboardButtonTypeCallback(b"OwO"),
                        ),
                        types.InlineKeyboardButton(
                            text="UwU",
                            type=types.InlineKeyboardButtonTypeCallback(b"UwU"),
                        ),
                    ],
                ]
            ),
        )
    elif message.text == "/keyboard":
        await message.reply_text(
            "This is a keyboard",
            reply_markup=types.ReplyMarkupShowKeyboard(
                [
                    [
                        types.KeyboardButton(
                            "OwO", type=types.KeyboardButtonTypeText()
                        ),
                        types.KeyboardButton(
                            "UwU", type=types.KeyboardButtonTypeText()
                        ),
                    ],
                ],
                one_time=True,
                resize_keyboard=True,
            ),
        )
    elif message.text == "/remove":
        await message.reply_text(
            "Keyboards removed",
            reply_markup=types.ReplyMarkupRemoveKeyboard(),
        )
    elif message.text == "/force":
        await message.reply_text(
            "This is a force reply",
            reply_markup=types.ReplyMarkupForceReply(),
        )
    elif message.text:
        if "/start" not in message.text:
            await message.reply_text('You said "{}"'.format(message.text))


@client.on_updateNewCallbackQuery()
async def callback_query(c: Client, message: types.UpdateNewCallbackQuery):
    if message.payload.data:
        await c.editTextMessage(
            message.chat_id,
            message.message_id,
            "You pressed {}".format(message.payload.data.decode()),
            reply_markup=types.ReplyMarkupInlineKeyboard(
                [
                    [
                        types.InlineKeyboardButton(
                            text="GitHub",
                            type=types.InlineKeyboardButton(
                                "https://github.com/pytdbot/client"
                            ),
                        )
                    ]
                ]
            ),
        )


# Run the client
client.run()
