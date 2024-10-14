try:
    import orjson as json
except ImportError:
    try:
        import ujson as json
    except ImportError:
        import json

JSON_ENCODER = json.__name__

if JSON_ENCODER == "orjson":

    def json_dumps(obj) -> bytes:
        # Null-terminated string is needed for orjson with c_char_p in tdjson
        return json.dumps(obj) + b"\0"
else:

    def json_dumps(obj) -> bytes:
        return json.dumps(obj).encode("utf-8")


def json_loads(obj):
    return json.loads(obj)
