import pytdbot
from asyncio import sleep


class ChatActions:
    def __init__(
        self,
        client: "pytdbot.Client",
        chat_id: int,
        action: str,
        message_thread_id: int = None,
    ) -> None:
        self.client = client
        self.chat_id = chat_id
        self.action = None
        self.__task = None
        self.message_thread_id = message_thread_id or 0

        assert isinstance(self.message_thread_id, int), "message_thread_id must be int"
        self.setAction(action)

    def __await__(self):
        return self.sendAction().__await__()

    async def __aenter__(self):
        await self.sendAction()
        self.__task = self.client.loop.create_task(self.__loop_action())
        return self

    async def __aexit__(self, exc_type, exc, traceback):
        self.__task.cancel()

    async def sendAction(self):
        return await self.client.sendChatAction(
            self.chat_id, self.message_thread_id, {"@type": self.action}
        )

    def setAction(self, action: str):
        if action == "typing" or action == "chatActionTyping":
            self.action = "chatActionTyping"
        elif action == "upload_photo" or action == "chatActionUploadingPhoto":
            self.action = "chatActionUploadingPhoto"
        elif action == "record_video" or action == "chatActionRecordingVideo":
            self.action = "chatActionRecordingVideo"
        elif action == "upload_video" or action == "chatActionUploadingVideo":
            self.action = "chatActionUploadingVideo"
        elif action == "record_voice" or action == "chatActionRecordingVoiceNote":
            self.action = "chatActionRecordingVoiceNote"
        elif action == "upload_voice" or action == "chatActionUploadingVoiceNote":
            self.action = "chatActionUploadingVoiceNote"
        elif action == "upload_document" or action == "chatActionUploadingDocument":
            self.action = "chatActionUploadingDocument"
        elif action == "choose_sticker" or action == "chatActionChoosingSticker":
            self.action = "chatActionChoosingSticker"
        elif action == "find_location" or action == "chatActionChoosingLocation":
            self.action = "chatActionChoosingLocation"
        elif action == "record_video_note" or action == "chatActionRecordingVideoNote":
            self.action = "chatActionRecordingVideoNote"
        elif action == "upload_video_note" or action == "chatActionUploadingVideoNote":
            self.action = "chatActionUploadingVideoNote"
        elif action == "cancel" or action == "chatActionCancel":
            self.action = "chatActionCancel"
        else:
            raise ValueError(f"Unknown action type {action}")

    async def __loop_action(self):
        while True:
            await sleep(4)
            await self.sendAction()

    def stop(self):
        self.setAction("cancel")
        self.__task.cancel()
