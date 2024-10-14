import binascii
import os


def to_camel_case(input_str: str, delimiter: str = ".", is_class: bool = True) -> str:
    if not input_str:
        return ""

    parts = input_str.split(delimiter)
    camel_case_str = ""

    for i, part in enumerate(parts):
        if i > 0:
            camel_case_str += part[0].upper() + part[1:]
        else:
            camel_case_str += part

    if camel_case_str:
        camel_case_str = (
            camel_case_str[0].upper() if is_class else camel_case_str[0].lower()
        ) + camel_case_str[1:]

    return camel_case_str


def create_extra_id(bytes_size: int = 9):
    return binascii.hexlify(os.urandom(bytes_size)).decode()


def get_bot_id_from_token(token: str) -> str:
    if len(token) > 80:
        return ""
    return token.split(":")[0] if ":" in token else ""
