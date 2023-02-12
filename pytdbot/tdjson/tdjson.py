from ctypes.util import find_library
from ctypes import c_int, c_double, c_void_p, c_char_p, CDLL
from logging import getLogger
from typing import Union
from platform import system
from pkg_resources import resource_filename
from ujson import loads, dumps


logger = getLogger(__name__)


class TDjson:
    def __init__(self, lib_path: str = None, verbosity: int = 2) -> None:
        """TDjson client.

        Args:
            lib_path (``str``, optional):
                Path to shared library. Defaults to ``None``.

            verbosity (``int``, optional):
                TDLib verbosity level. Defaults to ``2``.

        Raises:
            :py:class:``ValueError``: If library not found.
        """

        if lib_path is None:
            if system() == "Linux":
                lib_path = find_library("tdjson") or resource_filename(
                    "pytdbot", "lib/libtdjson.so"
                )
            else:
                lib_path = find_library("tdjson")

            if not lib_path:
                raise ValueError("TDLib library not found")

        logger.info("Initializing TDjson client with library: %s", lib_path)
        self._build_client(lib_path, verbosity)

    def _build_client(self, lib_path: str, verbosity: int) -> None:
        """Build TDjson client.

        Args:
            lib_path (``str``):
                Path to shared library.

            verbosity (``int``):
                TDLib verbosity level.
        """
        self._tdjson = CDLL(lib_path)

        # load TDLib functions from shared library
        self._td_create_client_id = self._tdjson.td_create_client_id
        self._td_create_client_id.restype = c_int
        self._td_create_client_id.argtypes = []

        self._td_client_destroy = self._tdjson.td_json_client_destroy
        self._td_client_destroy.restype = None
        self._td_client_destroy.argtypes = [c_void_p]

        self._td_receive = self._tdjson.td_receive
        self._td_receive.restype = c_char_p
        self._td_receive.argtypes = [c_double]

        self._td_send = self._tdjson.td_send
        self._td_send.restype = None
        self._td_send.argtypes = [c_int, c_char_p]

        self._td_execute = self._tdjson.td_execute
        self._td_execute.restype = c_char_p
        self._td_execute.argtypes = [c_char_p]

        self.client_id = self._td_create_client_id()

        td_version, td_commit_hash = self.execute(
            {"@type": "getOption", "name": "version"}
        ), self.execute({"@type": "getOption", "name": "commit_hash"})
        logger.info(
            "Using TDLib {} ({})".format(
                td_version["value"], td_commit_hash["value"][:9]
            )
        )

        if isinstance(verbosity, int):
            res = self.execute(
                {"@type": "setLogVerbosityLevel", "new_verbosity_level": verbosity}
            )

            if res["@type"] == "error":
                logger.error("Can't set log level: {}".format(res["message"]))

    def receive(self, timeout: float = 2.0) -> Union[None, dict]:
        """Receives incoming updates and results from TDLib.

        Args:
            timeout (``float``, *optional*):
                The maximum number of seconds allowed to wait for new data. Defaults to 2.0.

        Returns:
            :py:class:``dict``: An incoming update or result to a request. If no data is received, ``None`` is returned.
        """
        try:
            if res := self._td_receive(self.client_id, c_double(timeout)):
                return loads(res.decode("utf-8"))
        except Exception:
            logger.exception("Exception while receiving")
            raise

    def send(self, data: dict) -> None:
        """Sends a request to TDLib.

        Args:
            data (``dict``):
                The request to be sent.
        """
        try:
            self._td_send(self.client_id, dumps(data).encode("utf-8"))
        except Exception:
            logger.exception("Exception while sending", data)
            raise

    def execute(self, data: dict) -> Union[None, dict]:
        """Executes a TDLib request.

        Args:
            data (``dict``): The request to be executed.

        Returns:
            :py:class:``dict``: The result of the request.
        """
        try:
            if res := self._td_execute(dumps(data).encode("utf-8")):
                return loads(res.decode("utf-8"))
        except Exception:
            logger.exception("Exception while executing")
            raise

    def destroy(self) -> None:
        """Destroys the TDLib client."""
        self._td_client_destroy(self.client_id)
