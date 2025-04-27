from pytdbot import Client, types
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s]  %(message)s",
)

# Initialize the client
client = Client(
    api_id=0,  # Your api_id. You can get it from https://my.telegram.org/
    api_hash="API_HASH",  # Your api_hash. You can get it from https://my.telegram.org/
    database_encryption_key="1234echobot$",  # Your database encryption key
    token="1088394097:AAQX2DnWiw4ihwiJUhIHOGog8gGOI",  # Your bot token. You can get it from https://t.me/botfather
    files_directory="BotDB",  # Path where to store TDLib files
    workers=2,  # Number of workers
    td_verbosity=2,  # TDLib verbosity level
    td_log=types.LogStreamFile("tdlib.log", 104857600),  # Set TDLib log file path
)

# Define the welcome message
async def welcome_message(message: types.Message):
    return f"Hello {await message.mention('html')}!\n" \
           "Here are some bot commands:\n\n" \
           "- /keyboard - show keyboard\n" \
           "- /inline - show inline keyboard\n" \
           "- /remove - remove keyboard\n" \
           "- /force - force reply"

# Handle the '/start' command
@client.on_message()
async def start(c: Client, message: types.Message):
    if message.text == "/start":
        text = await welcome_message(message)

        await message.reply_text(
            text,
            reply_markup=types.ReplyMarkupInlineKeyboard(
                [
                    [
                        types.InlineKeyboardButton(
                            text="GitHub",
                            type=types.InlineKeyboardButtonTypeUrl("https://github.com/pytdbot/client"),
                        )
                    ]
                ]
            ),
        )

# Handle other commands
@client.on_message()
async def commands(c: Client, message: types.Message):
    if message.text == "/inline":
        await message.reply_text(
            "This is an Inline keyboard",
            reply_markup=types.ReplyMarkupInlineKeyboard(
                [
                    [
                        types.InlineKeyboardButton(text="OwO", type=types.InlineKeyboardButtonTypeCallback(b"OwO")),
                        types.InlineKeyboardButton(text="UwU", type=types.InlineKeyboardButtonTypeCallback(b"UwU")),
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
                        types.KeyboardButton("OwO", type=types.KeyboardButtonTypeText()),
                        types.KeyboardButton("UwU", type=types.KeyboardButtonTypeText()),
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
            await message.reply_text(f'You said "{message.text}"')

# Handle callback queries
@client.on_updateNewCallbackQuery()
async def callback_query(c: Client, message: types.UpdateNewCallbackQuery):
    if message.payload.data:
        await c.editTextMessage(
            message.chat_id,
            message.message_id,
            f"You pressed {message.payload.data.decode()}",
            reply_markup=types.ReplyMarkupInlineKeyboard(
                [
                    [
                        types.InlineKeyboardButton(
                            text="GitHub",
                            type=types.InlineKeyboardButtonTypeUrl("https://github.com/pytdbot/client"),
                        )
                    ]
                ]
            ),
        )

# Run the client
client.run()
