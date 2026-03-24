from . import exception, filters, types, utils
from .client import Client
from .client_manager import ClientManager
from .tdjson import TdJson

__all__ = [
    "types",
    "utils",
    "filters",
    "exception",
    "TdJson",
    "ClientManager",
    "Client",
]

__version__ = "0.10.0.dev0"
__copyright__ = "Copyright (c) 2022-2026 Pytdbot, AYMENJD"
__license__ = "MIT License"

VERSION = __version__
