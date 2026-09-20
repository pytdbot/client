# Userbot

Log in as a regular Telegram account (`user_bot=True`, no bot token).

!!! warning "Account risk"
    Userbots can get the account restricted or banned. Only use an account you can afford to lose. Do not automate anything that violates Telegram’s [Terms of Service](https://telegram.org/tos).

```python
from pytdbot import Client, types

client = Client(
    api_id=0,
    api_hash="API_HASH",
    files_directory="UserBot",
    database_encryption_key="change-me",
    user_bot=True,
)
```

Authorization is an update stream. Handle [`UpdateAuthorizationState`][pytdbot.types.UpdateAuthorizationState] and respond to wait states (phone number, code, password, QR). A complete prompt loop is in [`examples/userbot.py`](https://github.com/pytdbot/client/blob/main/examples/userbot.py).

```python
@client.on_updateAuthorizationState()
async def on_auth(c: Client, update: types.UpdateAuthorizationState):
    state = update.authorization_state
    if isinstance(state, types.AuthorizationStateWaitPhoneNumber):
        ...  # await c.setAuthenticationPhoneNumber(...)
```

[`setAuthenticationPhoneNumber`][pytdbot.functions.setAuthenticationPhoneNumber] when the state is [`AuthorizationStateWaitPhoneNumber`][pytdbot.types.AuthorizationStateWaitPhoneNumber]. Look up each wait type with `python -m pytdbot.docs type AuthorizationStateWaitPhoneNumber`.
