import binascii
import os

RETRY_AFTER_PREFEX = "Too Many Requests: retry after "


def to_camel_case(input_str: str, delimiter: str = ".", is_class: bool = True) -> str:
    if not input_str:
        return ""

    parts = input_str.split(delimiter)

    result = [parts[0]]
    for part in parts[1:]:
        result.append(part[0].upper())
        result.append(part[1:])

    joined = "".join(result)

    if not joined:
        return ""

    if is_class:
        return joined[0].upper() + joined[1:]
    return joined[0].lower() + joined[1:]


def create_extra_id(bytes_size: int = 9):
    return binascii.hexlify(os.urandom(bytes_size)).decode()


def get_bot_id_from_token(token: str) -> str:
    if len(token) > 80:
        return ""
    return token.split(":")[0] if ":" in token else ""


def get_retry_after_time(error_message: str) -> int:
    r"""Get the retry after time from flood wait error message

    Parameters:
        error_message (``str``):
            The returned error message from TDLib

    Returns:
        py:class:`int`
    """

    try:
        return int(error_message.removeprefix(RETRY_AFTER_PREFEX))
    except (ValueError, AttributeError):
        return 0
