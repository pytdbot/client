from pytdbot import Client
from pytdbot.types import LogStreamFile, Update
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s]  %(message)s",
)

client = Client(
    api_id=0,  # your api_id. You can get it from https://my.telegram.org/
    api_hash="API_HASH",  # your api_hash. You can get it from https://my.telegram.org/
    database_encryption_key="1234echobot$",  # your database encryption key.
    token="1088394097:AAQX2DnWiw4ihwiJUhIHOGog8gGOI",  # Your bot token. You can get it from https://t.me/botfather
    files_directory="BotDB",  # path where to store files.
    workers=2,  # number of workers.
    td_verbosity=2,  # TDLib verbosity level.
    td_log=LogStreamFile("pytdbot.log"),  # Set TDLib log file path
)


@client.on_updateNewMessage()
async def print_message(c: Client, message: Update):
    print(message)


@client.on_updateNewMessage()
async def echo(c: Client, message: Update):
    if message.content_type == "messageText":
        await message.reply_text(message.text, entities=message.entities)

    elif message.content_type == "messageAnimation":
        await message.reply_animation(
            message.file_id, caption=message.caption, caption_entities=message.entities
        )

    elif message.content_type == "messageAudio":
        await message.reply_audio(
            message.file_id, caption=message.caption, caption_entities=message.entities
        )

    elif message.content_type == "messageDocument":
        await message.reply_document(
            message.file_id, caption=message.caption, caption_entities=message.entities
        )

    elif message.content_type == "messagePhoto":
        await message.reply_photo(
            message.file_id, caption=message.caption, caption_entities=message.entities
        )

    elif message.content_type == "messageSticker":
        await message.reply_sticker(message.file_id)

    elif message.content_type == "messageVideo":
        await message.reply_video(
            message.file_id, caption=message.caption, caption_entities=message.entities
        )

    elif message.content_type == "messageVoiceNote":
        await message.reply_voice(
            message.file_id, caption=message.caption, caption_entities=message.entities
        )
    else:
        await message.reply_text("Oops! i don't know how to handle this message.")


# Run the client
client.run()
