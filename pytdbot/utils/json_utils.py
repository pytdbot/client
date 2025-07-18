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
