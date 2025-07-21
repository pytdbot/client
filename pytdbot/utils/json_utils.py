try:
    import orjson as json
except ImportError:
    try:
        import ujson as json
    except ImportError:
        import json

from typing import Union

JSON_ENCODER = json.__name__

if JSON_ENCODER == "orjson":

    def json_dumps(
        obj, encode: bool = False, null_terminated: bool = False
    ) -> Union[str, bytes]:
        d = json.dumps(obj)
        if (
            null_terminated
        ):  # Null-terminated string is needed for orjson with c_char_p in tdjson
            d += b"\0"

        return d if encode else d.decode("utf-8")
else:

    def json_dumps(
        obj, encode: bool = False, null_terminated: bool = False
    ) -> Union[str, bytes]:
        d = json.dumps(obj, separators=(",", ":"))
        return d if not encode else d.encode("utf-8")


def json_loads(obj):
    return json.loads(obj)


class CallbackData:
    def __init__(self, action, data=None):
        self.action = action
        self.data = data


empty_callback_data = CallbackData("")


def load_callback_data(data: bytes) -> CallbackData:
    r"""loads already created callback data by :func:`~pytdbot.utils.callback_data`. Returns empty CallbackData on error"""

    if not (data[0] == 0x5B and data[-1] == 0x5D):
        return empty_callback_data

    try:
        d = json_loads(data)
        if not isinstance(d, list) or len(d) != 2:
            return empty_callback_data
    except Exception:
        return empty_callback_data
    else:
        return CallbackData(*d)


def callback_data(action, data=None) -> bytes:
    r"""Create callback data for inline buttons

    Parameters:
        action (``Any``):
            Action name, can be any type, but must be JSON serializable

        data (``Any``, *optional*):
            Callback data, can be any type, but must be JSON serializable

    Returns:
        ``bytes``: Callback data encoded as bytes
    """

    d = json_dumps((action, data), encode=True)
    if len(d) > 64:
        raise ValueError(
            f"Callback data must be less than 64 bytes (got {len(d)} bytes)"
        )

    return d
