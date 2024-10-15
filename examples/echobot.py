from pytdbot import Client, types
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s]  %(message)s",
)


client = Client(
    token="1088394097:AAQX2DnWiw4ihwiJUhIHOGog8gGOI",  # Your bot token or phone number if you want to login as user
    api_id=0,
    api_hash="API_HASH",
    lib_path="/path/to/libtdjson.so",  # Path to TDjson shared library
    files_directory="BotDB",  # Path where to store TDLib files
    database_encryption_key="1234echobot$",
    td_verbosity=2,  # TDLib verbosity level
    td_log=types.LogStreamFile("tdlib.log"),  # Set TDLib log file path
)


@client.on_updateNewMessage()
async def print_message(c: Client, message: types.Message):
    print(message)


@client.on_message()
async def echo(c: Client, message: types.Message):
    if isinstance(message.content, types.MessageText):
        await message.reply_text(message.text, entities=message.entities)

    elif isinstance(message.content, types.MessageAnimation):
        await message.reply_animation(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif isinstance(message.content, types.MessageAudio):
        await message.reply_audio(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif isinstance(message.content, types.MessageDocument):
        await message.reply_document(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif isinstance(message.content, types.MessagePhoto):
        await message.reply_photo(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif isinstance(message.content, types.MessageSticker):
        await message.reply_sticker(message.remote_file_id)

    elif isinstance(message.content, types.MessageVideo):
        await message.reply_video(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )

    elif isinstance(message.content, types.MessageVoiceNote):
        await message.reply_voice(
            message.remote_file_id,
            caption=message.caption,
            caption_entities=message.entities,
        )
    else:
        await message.reply_text("Oops! i don't know how to handle this message.")


# Run the client
client.run()
