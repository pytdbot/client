import json
from base64 import b64encode
from typing import Any

from .. import types, utils

_type_cache: dict[str, type] = {}


def obj_to_json(obj: Any, **kwargs: Any) -> str:
    return json.dumps(obj_to_dict(obj), **kwargs)


def obj_to_dict(obj: Any) -> Any:
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


def dict_to_obj(dict_obj: Any, client: Any = None) -> Any:
    if isinstance(dict_obj, dict):
        if "@type" in dict_obj:
            td_type = dict_obj["@type"]
            obj_type = _type_cache.get(td_type)
            if obj_type is None:
                obj_type = getattr(types, utils.to_camel_case(td_type))
                _type_cache[td_type] = obj_type

            obj = obj_type.from_dict(
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
