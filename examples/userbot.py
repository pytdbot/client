import asyncio

try:
    import readline  # noqa: F401
except ImportError:
    pass

from pytdbot import Client, types

try:
    import qrcode
except ImportError:
    qrcode = None

client = Client(
    api_id=0,
    api_hash="API_HASH",
    files_directory="UserBot",
    database_encryption_key="tahinidates$",
    td_verbosity=2,
    td_log=types.LogStreamFile("tdlib.log", 104857600),
    user_bot=True,
)


@client.on_message()
async def handle_commands(_: Client, message: types.Message):
    if message.from_id == client.options["my_id"]:  # it's me
        if message.text == "!hi":
            await message.edit_text("Hi, this is from Pytdbot!")


def async_input(prompt: str = "") -> str:
    return asyncio.to_thread(lambda: input(prompt))


def clear_print():
    print("\033c", end="")


def get_via_code_type(code_type):
    if isinstance(code_type, types.AuthenticationCodeTypeTelegramMessage):
        return "Telegram app"
    elif isinstance(code_type, types.AuthenticationCodeTypeSms):
        return "SMS"
    elif isinstance(
        code_type,
        (types.AuthenticationCodeTypeSmsWord, types.AuthenticationCodeTypeSmsPhrase),
    ):
        sms_type = (
            "Word"
            if isinstance(code_type, types.AuthenticationCodeTypeSmsWord)
            else "Phrase"
        )
        return (
            f"SMS {sms_type}" + ""
            if not code_type.first_letter
            else f" (first letter: {code_type.first_letter})"
        )
    elif isinstance(code_type, types.AuthenticationCodeTypeCall):
        return "Call"
    elif isinstance(code_type, types.AuthenticationCodeTypeFlashCall):
        return "Flash call"
    elif isinstance(code_type, types.AuthenticationCodeTypeMissedCall):
        return f"Missed call (prefix: {code_type.phone_number_prefix}, length: {code_type.phone_number_length})"
    elif isinstance(code_type, types.AuthenticationCodeTypeFragment):
        return f"Fragment (url: {code_type.url})"
    else:
        return "Unknown"


@client.on_updateAuthorizationState()
async def handle_auth(_: Client, auth: types.UpdateAuthorizationState):
    state = auth.authorization_state

    if isinstance(state, types.AuthorizationStateWaitPhoneNumber):
        while True:
            user_input = await async_input(
                'Enter your phone number, or type "qr" to log in using a QR code: '
            )
            user_input = user_input.strip()

            if not user_input:
                continue

            if user_input.lower() == "qr":
                res = await client.requestQrCodeAuthentication()
            else:
                res = await client.setAuthenticationPhoneNumber(
                    user_input,
                )

            if isinstance(res, types.Error):
                print(f"Error: {res.message}")
                continue

            return
    elif isinstance(state, types.AuthorizationStateWaitCode):
        code_info = state.code_info
        code_type = get_via_code_type(code_info.type)
        while True:
            user_input = await async_input(f"Enter the code recevied via {code_type}: ")
            user_input = user_input.strip()

            if not user_input:
                continue

            res = await client.checkAuthenticationCode(user_input)

            if isinstance(res, types.Error):
                print(f"Error: {res.message}")
                continue

            return
    elif isinstance(state, types.AuthorizationStateWaitOtherDeviceConfirmation):
        if not qrcode:
            print(
                "\nThe 'qrcode' module is not installed.\n"
                "Install it with:\n"
                "  pip install qrcode\n"
            )
            await client.stop()
            return

        clear_print()

        qr = qrcode.QRCode(border=1)
        qr.add_data(state.link)
        qr.make(fit=True)

        print("\nScan this QR code using your Telegram mobile app.")
        print("Go to Settings → Devices → Link Desktop Device.\n")

        qr.print_ascii()
        qr.clear()
    elif isinstance(state, types.AuthorizationStateWaitPassword):
        clear_print()
        while True:
            user_input = await async_input(
                f"Enter your 2FA password (hint: {state.password_hint}): "
            )
            user_input = user_input.strip()

            if not user_input:
                continue

            res = await client.checkAuthenticationPassword(user_input)

            if isinstance(res, types.Error):
                print(f"Error: {res.message}")
                continue

            return
    elif isinstance(state, types.AuthorizationStateReady):
        me = await client.getMe()
        clear_print()
        print(f"Logged in as {me.first_name} (ID: {me.id})")


# Run the client
client.run()
