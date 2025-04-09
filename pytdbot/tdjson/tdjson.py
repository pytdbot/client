try:
    import tdjson
except ImportError:
    tdjson = None

from ctypes import c_int, c_double, c_char_p, CDLL

from logging import getLogger
from typing import Union
from ..utils import JSON_ENCODER, json_dumps, json_loads

import sys

logger = getLogger(__name__)


class TdJson:
    def __init__(self, lib_path: str = None, verbosity: int = 2) -> None:
        """TdJson client

        Parameters:
            lib_path (``str``, optional):
                Path to shared library; if ``None`` then [`tdjson`](https://github.com/AYMENJD/tdjson) binding will be used. Default is ``None``

            verbosity (``int``, optional):
                TDLib verbosity level. Default is ``2``

        Raises:
            :py:class:``ValueError``: If library not found
        """

        self._build_client(lib_path, verbosity)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def _build_client(self, lib_path: str, verbosity: int) -> None:
        """Build TdJson client

        Parameters:
            lib_path (``str``):
                Path to shared library

            verbosity (``int``):
                TDLib verbosity level
        """

        self.using_binding = False

        if lib_path is None:
            if not tdjson:
                raise ValueError(
                    f"tdjson binding not found. Try install using: `{sys.executable} -m pip install --upgrade tdjson`"
                )

            # Use tdjson binding that already include TDLib
            self._td_create_client_id = tdjson.td_create_client_id
            self._td_send = tdjson.td_send
            self._td_receive = tdjson.td_receive
            self._td_execute = tdjson.td_execute

            self.using_binding = True

            logger.info(f"Using tdjson binding {tdjson.__version__}")
        else:
            if not lib_path:
                raise ValueError(
                    "Could not find TDLib, provide full path to libtdjson.so in lib_path"
                )

            logger.info(f"Initializing TdJson client with library: {lib_path}")

            self._tdjson = CDLL(lib_path)

            # load TDLib functions from shared library
            self._td_create_client_id = self._tdjson.td_create_client_id
            self._td_create_client_id.restype = c_int
            self._td_create_client_id.argtypes = []

            self._td_receive = self._tdjson.td_receive
            self._td_receive.restype = c_char_p
            self._td_receive.argtypes = [c_double]

            self._td_send = self._tdjson.td_send
            self._td_send.restype = None
            self._td_send.argtypes = [c_int, c_char_p]

            self._td_execute = self._tdjson.td_execute
            self._td_execute.restype = c_char_p
            self._td_execute.argtypes = [c_char_p]

        td_version, td_commit_hash = (
            self.execute({"@type": "getOption", "name": "version"}),
            self.execute({"@type": "getOption", "name": "commit_hash"}),
        )

        logger.info(
            f"Using TDLib {td_version['value']} ({td_commit_hash['value'][:9]}) with {JSON_ENCODER} encoder"
        )

        if isinstance(verbosity, int):
            res = self.execute(
                {"@type": "setLogVerbosityLevel", "new_verbosity_level": verbosity}
            )

            if res["@type"] == "error":
                logger.error("Can't set log level: {}".format(res["message"]))

    def create_client_id(self) -> int:
        """Returns an opaque identifier of a new TDLib instance"""
        return self._td_create_client_id()

    def receive(self, timeout: float = 2.0) -> Union[None, dict]:
        """Receives incoming updates and results from TDLib

        Parameters:
            timeout (``float``, *optional*):
                The maximum number of seconds allowed to wait for new data. Default is ``2.0``

        Returns:
            :py:class:``dict``: An incoming update or result to a request. If no data is received, ``None`` is returned
        """

        if res := self._td_receive(
            timeout if self.using_binding else c_double(timeout)
        ):
            return json_loads(res)

    def send(self, client_id: int, data: dict) -> None:
        """Sends a request to TDLib

        Parameters:
            client_id (``int``):
                TDLib Client identifier

            data (``dict``):
                Request to be sent
        """

        if not client_id:
            raise ValueError("client_id is required")

        self._td_send(client_id, json_dumps(data, encode=not self.using_binding))

    def execute(self, data: dict) -> Union[None, dict]:
        """Executes a TDLib request

        Parameters:
            data (``dict``): The request to be executed

        Returns:
            :py:class:``dict``: The result of the request
        """

        if res := self._td_execute(json_dumps(data, encode=not self.using_binding)):
            return json_loads(res)
