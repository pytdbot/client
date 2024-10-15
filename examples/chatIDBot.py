from pytdbot import Client, filters, types, utils
import logging, asyncio

logging.basicConfig(
    level=logging.INFO,
    # level=logging.DEBUG,
    format="[%(levelname)s][p %(process)d %(threadName)s][%(created)f][%(filename)s:%(lineno)d][%(funcName)s]  %(message)s",
)
is_private_filter = filters.create(lambda _, message: message.chat_id > 0)
lock = asyncio.Lock()

client = Client(
    api_id=0,
    api_hash="",
    token="",
    database_encryption_key="WhatIDisThat",
    files_directory="ChatIDbot",
    options={
        "disable_network_statistics": True,
        "disable_time_adjustment_protection": True,
        "ignore_inline_thumbnails": True,
        "ignore_background_updates": True,
        "message_unload_delay": 60,
        "disable_persistent_network_statistics": True,
    },
    use_chat_info_database=False,
    use_file_database=False,
    use_message_database=False,
    sleep_threshold=60,
    default_parse_mode="markdownv2",
)

request_buttons = types.ReplyMarkupShowKeyboard(
    [
        [
            types.KeyboardButton(
                text="Channel",
                type=types.KeyboardButtonTypeRequestChat(
                    id=1,
                    chat_is_channel=True,
                    restrict_chat_is_forum=False,
                    chat_is_forum=False,
                    restrict_chat_has_username=False,
                    chat_has_username=False,
                    chat_is_created=False,
                ),
            ),
            types.KeyboardButton(
                text="Group",
                type=types.KeyboardButtonTypeRequestChat(
                    id=2,
                    chat_is_channel=False,
                    restrict_chat_is_forum=False,
                    chat_is_forum=False,
                    restrict_chat_has_username=False,
                    chat_has_username=False,
                    chat_is_created=False,
                ),
            ),
        ],
        [
            types.KeyboardButton(
                text="User",
                type=types.KeyboardButtonTypeRequestUsers(
                    id=3,
                    max_quantity=1,
                    restrict_user_is_bot=True,
                    user_is_bot=False,
                    restrict_user_is_premium=False,
                    user_is_premium=False,
                ),
            ),
            types.KeyboardButton(
                text="Bot",
                type=types.KeyboardButtonTypeRequestUsers(
                    id=4,
                    max_quantity=1,
                    restrict_user_is_bot=True,
                    user_is_bot=True,
                    restrict_user_is_premium=False,
                    user_is_premium=False,
                ),
            ),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Select chat type",
)


async def increase_usage(by: int = 1):
    async with lock:
        if "x_usage" not in client.options:
            await client.call_method(
                "setOption",
                name="x_usage",
                value={"@type": "optionValueInteger", "value": by},
            )
        else:
            await client.call_method(
                "setOption",
                name="x_usage",
                value={
                    "@type": "optionValueInteger",
                    "value": client.options["x_usage"] + by,
                },
            )


@client.on_message(is_private_filter)
async def start(client: Client, message: types.Message):
    if message.text == "/start":
        await message.reply_text(
            "*Your ID*: {}".format(
                utils.code(str(message.from_id)),
            ),
            reply_markup=request_buttons,
        )
        await increase_usage()
    elif message.text == "/usage":
        await message.reply_text(
            "*Bot usage*: {}".format(client.options.get("x_usage", 0))
        )


@client.on_message(is_private_filter)
async def handle_shared_chat(client: Client, message: types.Message):
    if isinstance(message.content, types.MessageUsersShared):
        if message.content.button_id == 3:
            user_type_text = "*User ID*"
        elif message.content.button_id == 4:
            user_type_text = "*Bot ID*"

        await message.reply_text(
            "{}: {}".format(
                user_type_text,
                utils.code(str(message.content.users[0].user_id)),
            ),
        )
        await increase_usage()
    elif isinstance(message.content, types.MessageChatShared):
        await message.reply_text(
            "*Chat ID*: {}".format(
                utils.code(str(message.content.chat.chat_id)),
            ),
        )
        await increase_usage()


@client.on_updateChatMember()
async def chat_member(client: Client, update: types.UpdateChatMember):
    if (
        isinstance(update.new_chat_member.member_id, types.MessageSenderUser)
        and update.new_chat_member.member_id.user_id == client.options["my_id"]
    ):
        if isinstance(update.new_chat_member.status, types.ChatMemberStatusMember):
            await client.sendTextMessage(
                update.chat_id,
                "*Chat ID*: {}".format(
                    utils.code(str(update.chat_id)),
                ),
            )
            await client.leaveChat(update.chat_id)
            await increase_usage()


# Run the bot
client.run()
