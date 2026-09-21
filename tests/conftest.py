import os

import pytest
import pytest_asyncio
from pytdbot import Client, types


@pytest.fixture
def assert_ok():
    def _assert_ok(result):
        if isinstance(result, types.Error):
            if result.code == 500:
                pytest.skip(f"TDLib/Telegram 500: {result.message}")
            pytest.fail(f"TDLib error {result.code}: {result.message}")
        return result

    return _assert_ok


@pytest.fixture(scope="session")
def chat_id():
    raw = os.environ.get("PYTDBOT_TEST_CHAT_ID")
    if not raw:
        pytest.skip("PYTDBOT_TEST_CHAT_ID not set")
    return int(raw)


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def client(tmp_path_factory):
    token = os.environ.get("PYTDBOT_TEST_BOT_TOKEN")
    api_id = os.environ.get("PYTDBOT_API_ID")
    api_hash = os.environ.get("PYTDBOT_API_HASH")
    if not token or not api_id or not api_hash:
        pytest.skip("test DC credentials not set")

    files = tmp_path_factory.mktemp("tdlib")
    bot = Client(
        token=token,
        api_id=int(api_id),
        api_hash=api_hash,
        files_directory=str(files),
        database_encryption_key="pytest-tdlib",
        use_test_dc=True,
        use_file_database=False,
        use_chat_info_database=False,
        use_message_database=False,
        workers=1,
        td_verbosity=1,
    )
    await bot.start()
    try:
        yield bot
    finally:
        await bot.stop()
