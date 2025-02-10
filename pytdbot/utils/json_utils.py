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

    def json_dumps(obj, encode: bool = False) -> Union[str, bytes]:
        # Null-terminated string is needed for orjson with c_char_p in tdjson
        d = json.dumps(obj) + b"\0"
        return d if encode else d.decode("utf-8")
else:

    def json_dumps(obj, encode: bool = False) -> Union[str, bytes]:
        d = json.dumps(obj)
        return d if not encode else d.encode("utf-8")


def json_loads(obj):
    return json.loads(obj)
