import pytest
from pytdbot import types, utils


@pytest.mark.asyncio
async def test_media_album_future_completes():
    fut = utils.MediaAlbumFuture(types.Messages(total_count=2, messages=[]))
    assert not fut.done()
    fut.set_result(types.Ok())
    assert not fut.done()
    fut.set_result(types.Ok())
    assert fut.done()
    result = await fut
    assert result.total_count == 2
    assert len(result.messages) == 2
