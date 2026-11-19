import asyncio
import logging

from pytdbot import Client, types

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s]  %(message)s",
)


client = Client(
    token="1088394097:AAQX2DnWiw4ihwiJUhIHOGog8gGOI",  # Your bot token
    api_id=0,
    api_hash="API_HASH",
    files_directory="BotDB",  # Path where to store TDLib files
    database_encryption_key="1234echobot$",
    td_verbosity=2,  # TDLib verbosity level
    td_log=types.LogStreamFile(
        path="tdlib.log", max_file_size=104857600
    ),  # Set TDLib log file path
)


@client.on_command("start", "help")
async def start(_: Client, message: types.Message):
    await message.reply_text(
        "Hi! Send `echo <text>` and I will send it back.", parse_mode="markdown"
    )


@client.on_command("echo", prefix=True)
async def echo(_: Client, message: types.Message):
    text = message.text.removeprefix("echo").strip()
    if text:
        await message.reply_text(text)


@client.on_command("id")
async def id(_: Client, message: types.Message):
    await message.reply_text(
        f"Chat ID: <code>{message.chat_id}</code>", parse_mode="html"
    )


asyncio.run(client.run())
