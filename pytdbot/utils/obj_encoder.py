import json

from base64 import b64encode
from .. import types, utils


def obj_to_json(obj, **kwargs):
    return json.dumps(obj_to_dict(obj), **kwargs)


def obj_to_dict(obj):
    if hasattr(obj, "to_dict"):
        return obj_to_dict(obj.to_dict())
    elif isinstance(obj, list):
        return [obj_to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: obj_to_dict(value) for key, value in obj.items()}
    elif isinstance(obj, bytes):
        return b64encode(obj).decode("utf-8")
    else:
        return obj


def dict_to_obj(dict_obj, client=None):
    if isinstance(dict_obj, dict):
        if "@type" in dict_obj:
            obj = getattr(types, utils.to_camel_case(dict_obj["@type"])).from_dict(
                {key: dict_to_obj(value, client) for key, value in dict_obj.items()}
            )
            if client:
                obj._client = client
            return obj
        else:
            return {key: dict_to_obj(value, client) for key, value in dict_obj.items()}
    elif isinstance(dict_obj, list):
        return [dict_to_obj(item, client) for item in dict_obj]
    else:
        return dict_obj
