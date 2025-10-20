from asyncio import sleep
from typing import Literal

import pytdbot


class ChatActions:
    def __init__(
        self,
        client: "pytdbot.Client",
        chat_id: int,
        action: Literal[
            "typing",
            "upload_photo",
            "record_video",
            "upload_video",
            "record_voice",
            "upload_voice",
            "upload_document",
            "choose_sticker",
            "find_location",
            "record_video_note",
            "upload_video_note",
            "cancel",
        ],
        topic_id: "pytdbot.types.MessageTopic" = None,
    ) -> None:
        self.client = client
        self.chat_id = chat_id
        self.action = None
        self.__task = None
        self.topic_id = topic_id

        if topic_id and not isinstance(self.topic_id, pytdbot.types.MessageTopic):
            raise ValueError("topic_id must be an instnace of MessageTopic")
        self.setAction(action)

    def __await__(self):
        return self.sendAction().__await__()

    async def __aenter__(self):
        await self.sendAction()
        self.__task = self.client.loop.create_task(self.__loop_action())
        return self

    async def __aexit__(self, exc_type, exc, traceback):
        await self.stop()

    async def sendAction(self):
        return await self.client.sendChatAction(
            chat_id=self.chat_id,
            topic_id=self.topic_id,
            action=self.action,
        )

    def setAction(
        self,
        action: Literal[
            "typing",
            "upload_photo",
            "record_video",
            "upload_video",
            "record_voice",
            "upload_voice",
            "upload_document",
            "choose_sticker",
            "find_location",
            "record_video_note",
            "upload_video_note",
            "cancel",
        ],
    ):
        if action == "typing" or action == "chatActionTyping":
            self.action = pytdbot.types.ChatActionTyping()
        elif action == "upload_photo" or action == "chatActionUploadingPhoto":
            self.action = pytdbot.types.ChatActionUploadingPhoto()
        elif action == "record_video" or action == "chatActionRecordingVideo":
            self.action = pytdbot.types.ChatActionRecordingVideo()
        elif action == "upload_video" or action == "chatActionUploadingVideo":
            self.action = pytdbot.types.ChatActionUploadingVideo()
        elif action == "record_voice" or action == "chatActionRecordingVoiceNote":
            self.action = pytdbot.types.ChatActionRecordingVoiceNote()
        elif action == "upload_voice" or action == "chatActionUploadingVoiceNote":
            self.action = pytdbot.types.ChatActionUploadingVoiceNote()
        elif action == "upload_document" or action == "chatActionUploadingDocument":
            self.action = pytdbot.types.ChatActionUploadingDocument()
        elif action == "choose_sticker" or action == "chatActionChoosingSticker":
            self.action = pytdbot.types.ChatActionChoosingSticker()
        elif action == "find_location" or action == "chatActionChoosingLocation":
            self.action = pytdbot.types.ChatActionChoosingLocation()
        elif action == "record_video_note" or action == "chatActionRecordingVideoNote":
            self.action = pytdbot.types.ChatActionRecordingVideoNote()
        elif action == "upload_video_note" or action == "chatActionUploadingVideoNote":
            self.action = pytdbot.types.ChatActionUploadingVideoNote()
        elif action == "cancel" or action == "chatActionCancel":
            self.action = pytdbot.types.ChatActionCancel()
        else:
            raise ValueError(f"Unknown action type {action}")

    async def __loop_action(self):
        while True:
            await sleep(4)
            await self.sendAction()

    async def stop(self):
        self.setAction("cancel")
        self.__task.cancel()
        await self.sendAction()
