from typing import Union

import pytdbot


class FileBoundMethods:
    def __init__(self):
        self._client: pytdbot.Client

    async def download(
        self,
        priority: int = 1,
        offset: int = 0,
        limit: int = 0,
        synchronous: bool = True,
    ) -> Union["pytdbot.types.Error", "pytdbot.types.File"]:
        r"""Downloads a file. Shortcut for :meth:`~pytdbot.Client.downloadFile`"""

        file_id = None
        if isinstance(self, pytdbot.types.RemoteFile):
            file_info = await self._client.getRemoteFile(self.id)
            if not file_info:
                return file_info

            file_id = file_info.id
        elif isinstance(self, pytdbot.types.File):
            file_id = self.id

        if file_id:
            return await self._client.downloadFile(
                file_id=file_id,
                priority=priority,
                offset=offset,
                limit=limit,
                synchronous=synchronous,
            )

    async def delete(self) -> Union["pytdbot.types.Error", "pytdbot.types.Ok"]:
        r"""Deletes a file from the TDLib file cache. Shortcut for :meth:`~pytdbot.Client.deleteFile`"""

        file_id = None
        if isinstance(self, pytdbot.types.RemoteFile):
            file_info = await self._client.getRemoteFile(self.id)
            if not file_info:
                return file_info

            file_id = file_info.id
        elif isinstance(self, pytdbot.types.File):
            file_id = self.id

        if file_id:
            return await self._client.deleteFile(file_id=file_id)
