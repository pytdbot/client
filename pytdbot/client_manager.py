import asyncio
import logging
from typing import List
from concurrent.futures import ThreadPoolExecutor

import pytdbot
from .tdjson import TdJson

logger = logging.getLogger(__name__)


class ClientManager:
    """Client manager for Pytdbot"""

    def __init__(
        self,
        clients: List[pytdbot.Client] = None,
        lib_path: str = None,
        verbosity: int = 2,
        loop: asyncio.AbstractEventLoop = None,
    ) -> None:
        """Manage multiple Pytdbot clients

        Example:
            .. code-block:: python

                >>> from pytdbot import ClientManager, Client
                >>> clients = [Client(...), Client(...), Client(...)]
                >>> client_manager = ClientManager(clients)
                >>> await client_manager.start()

        Parameters:
            clients (``List[pytdbot.Client]``, *optional*):
                List of clients to manage

            lib_path (``str``, *optional*):
                Path to TDlib library

            verbosity (``int``, *optional*):
                Verbosity level of TDlib. Default is ``2``

            loop (``asyncio.AbstractEventLoop``, *optional*):
                Event loop to use
        """

        if clients and not isinstance(clients, (list, pytdbot.Client)):
            raise TypeError("clients must be a list of pytdbot.Client")

        self.loop = loop or pytdbot.utils.get_running_loop()
        self.__tdjson = TdJson(lib_path, verbosity)

        self.__clients: dict[int, pytdbot.Client] = {}

        if isinstance(clients, list):
            self.__pending_clients = clients
            self.start_clients_on_add = True
        elif isinstance(clients, pytdbot.Client):
            self.__pending_clients = [clients]
            self.start_clients_on_add = False
        else:
            self.__pending_clients = None
            self.start_clients_on_add = False

        self.__receiver_task = None
        self.__should_exit = False
        self.is_running = False

    async def start(self) -> None:
        """Start the Client Manager"""

        if self.is_running:
            return

        self.__receiver_task = self.loop.create_task(self.__td_receiver_loop())

        for client in self.__pending_clients:
            await self.add_client(client, start_client=self.start_clients_on_add)

        self.__pending_clients = None

    async def add_client(
        self, client: pytdbot.Client, start_client: bool = False
    ) -> None:
        """Add a client to the manager

        Parameters:
            client (``pytdbot.Client``):
                Client to add

            start_client (``bool``, *optional*):
                Whether to start the client immediately. Default is ``False``
        """

        if not isinstance(client, pytdbot.Client):
            raise TypeError("client must be an instance of pytdbot.Client")

        client_id = self.__tdjson.create_client_id()
        client.client_id = client_id
        client.client_manager = self

        self.__clients[client_id] = client

        if start_client:
            await client.start()

        logger.debug(f"Client {client_id} added")

    async def delete_client(self, client_id: int, close_client: bool = False) -> None:
        """Remove a client from the manager

        Parameters:
            client_id (``int``):
                ID of client to remove

            close_client (``bool``, *optional*):
                Whether to close the client before removing. Default is ``False``
        """

        client = self.__clients.pop(client_id, None)
        if not client:
            raise ValueError(f"Client with ID {client_id} not found")

        if close_client:
            await client.stop()
        logger.debug(f"Client {client_id} deleted")

    def send(self, client_id: int, request: dict) -> None:
        """Send a request to TDlib

        Parameters:
            client_id (``int``):
                ID of client to send request from

            request (``dict``):
                Request to send
        """

        self.__tdjson.send(client_id, request)

    async def __td_receiver_loop(self) -> None:
        with ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="ClientManager"
        ) as executor:
            try:
                self.is_running = True
                logger.info("ClientManager started")

                while not self.__should_exit:
                    update = await self.loop.run_in_executor(
                        executor,
                        self.__tdjson.receive,
                        100000.0,  # Seconds
                    )

                    if not update or self.__should_exit:
                        continue

                    client = self.__clients.get(update["@client_id"])
                    if client:
                        self.loop.create_task(client.process_update(update))
                    else:
                        logger.warning(
                            f"Unknown client ID in update: {update['@client_id']}"
                        )

            except Exception:
                logger.exception("Error in td_receiver")
            finally:
                self.is_running = False
                logger.debug("ClientManager stopped")

    async def close(self, close_all_clients: bool = False) -> bool:
        """Close the Client Manager

        Parameters:
            close_all_clients (``bool``, *optional*):
                Whether to close all managed clients. Default is ``False``

        Returns:
            ``bool``
        """
        if self.__should_exit:
            return True

        self.__should_exit = True

        if close_all_clients:
            for client_id in list(self.__clients.keys()):
                await self.delete_client(client_id, close_client=True)

        # Send dummy request to wake up receiver
        self.send(1, {"@type": "getOption", "name": "version"})

        await self.__receiver_task

        logger.info("ClientManager closed")
        return True
