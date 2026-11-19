from __future__ import annotations

import asyncio
import logging

import pytest

from pytdbot import Client, filters
from pytdbot.utils import dict_to_obj

is_active = filters.create(func=lambda _, m: getattr(m, "is_active_chat", False))


class CommandClientStub:
    """A stub carrying the REAL Client methods for command routing,
    so registration + dispatch logic run the shipped code paths.

    Real methods resolve private attrs under Client's mangled names
    (``_Client__…``), so the stub stores its state under those names."""

    add_command = Client.add_command
    remove_command = Client.remove_command
    _remove_command_handler = Client._remove_command_handler
    _update_handlers = Client._update_handlers
    is_coro_filter = Client.is_coro_filter

    # plain aliases so module-level tests can call them without mangling
    dispatch_commands = Client._Client__dispatch_commands

    # the real methods resolve these through Client's name mangling,
    # and __dispatch_commands must stay a staticmethod
    _Client__dispatch_commands = staticmethod(Client._Client__dispatch_commands)
    _Client__ensure_command_dispatcher = Client._Client__ensure_command_dispatcher

    def __init__(self, default_handlers_timeout=None):
        self.default_handlers_timeout = default_handlers_timeout
        self._handlers = {"initializer": [], "finalizer": []}
        self._current_handlers = {}
        self._command_handlers = {}
        self._prefix_handlers = []
        self._current_command_handlers = {}
        self._current_prefix_handlers = ()
        self._Client__command_dispatcher = None
        self.logger = logging.getLogger("stub")
        self._Client__cache = {"is_coro_filter": {}}

    @property
    def dispatcher_handler(self):
        return self._Client__command_dispatcher

    def linear_handlers(self):
        return self._current_handlers.get("updateNewMessage", ())


def make_message(text):
    message = dict_to_obj(
        {
            "@type": "updateNewMessage",
            "message": {
                "@type": "message",
                "id": 1,
                "sender_id": {"@type": "messageSenderUser", "user_id": 42},
                "chat_id": -1001239062182,
                "content": {
                    "@type": "messageText",
                    "text": {
                        "@type": "formattedText",
                        "text": text,
                        "entities": [],
                    },
                },
                "is_outgoing": False,
                "is_channel_post": False,
                "date": 2000000000,
                "edit_date": 0,
            },
        }
    ).message
    message.is_active_chat = True
    return message


async def run_linear(stub, message):
    """Run the updateNewMessage linear list exactly like __run_handlers."""
    from pytdbot.exception import StopHandlers

    for handler in stub.linear_handlers():
        try:
            handler_value = message if handler.inner_object else message
            if handler.filter is not None:
                if not handler.filter.func(stub, handler_value):
                    continue
            await handler(stub, handler_value)
        except StopHandlers:
            raise
        except Exception:
            pass


def test_on_command_class_level_decorator():
    calls = []

    @Client.on_command("start", "go")
    async def start(client, message):
        calls.append(message.text)

    assert start._handler.commands == ("start", "go")
    assert start._handler.prefix is False
    assert start._handler.update_type == "updateNewMessage"
    assert start._handler.inner_object is True


def test_on_command_prefix_decorator():
    @Client.on_command("search", prefix=True)
    async def search(client, message):
        pass

    assert search._handler.commands == ("search",)
    assert search._handler.prefix is True


def test_on_command_first_string_binds_self():
    @Client.on_command("x")
    async def h(client, message):
        pass

    assert h._handler.commands == ("x",)


def test_add_command_validates():
    stub = CommandClientStub()

    async def h(client, message):
        pass

    with pytest.raises(TypeError):
        stub.add_command(h)

    with pytest.raises(TypeError):
        stub.add_command(h, "")

    with pytest.raises(TypeError):
        stub.add_command(lambda: None, "x")

    def sync_h(client, message):
        pass

    with pytest.raises(TypeError):
        stub.add_command(sync_h, "x")


def test_dispatcher_inserted_once_and_position_min():
    stub = CommandClientStub()

    async def h1(client, message):
        pass

    async def h2(client, message):
        pass

    stub.add_command(h1, "a", position=5)
    stub.add_command(h2, "b", position=2)
    assert len(stub.linear_handlers()) == 1, "dispatcher must be a single handler"
    assert stub.dispatcher_handler.position == 2, "smallest position must win"


def test_no_dispatcher_without_commands():
    stub = CommandClientStub()
    assert stub.linear_handlers() == ()


async def test_exact_command_dispatch():
    stub = CommandClientStub()
    calls = []

    async def activate(client, message):
        calls.append(("activate", message.text))

    async def other(client, message):
        calls.append(("other", message.text))

    stub.add_command(activate, "start")
    stub.add_command(other, "disable")

    await stub.dispatch_commands(make_message("start"))
    assert calls == [("activate", "start")]

    await stub.dispatch_commands(make_message("hello there"))
    assert calls == [("activate", "start")], "no match -> nothing runs"


async def test_no_slash_prepended():
    """Commands match message.text as-is: no slash is added for you."""
    stub = CommandClientStub()
    calls = []

    async def start(client, message):
        calls.append(1)

    stub.add_command(start, "start")

    await stub.dispatch_commands(make_message("/start"))
    assert calls == [], "a slash command must not match a bare word registration"

    await stub.dispatch_commands(make_message("start"))
    assert calls == [1]


async def test_prefix_command_dispatch():
    stub = CommandClientStub()
    calls = []

    async def search(client, message):
        calls.append(message.text)

    async def exact(client, message):
        calls.append(("exact", message.text))

    stub.add_command(search, "search", prefix=True)
    stub.add_command(exact, "search")

    await stub.dispatch_commands(make_message("search cute cat videos"))
    assert calls == ["search cute cat videos"]

    calls.clear()
    await stub.dispatch_commands(make_message("search"))
    assert calls == [("exact", "search")], "exact match wins over prefix"


async def test_filter_blocks_command():
    stub = CommandClientStub()
    calls = []

    async def activate(client, message):
        calls.append(1)

    stub.add_command(activate, "start", filters=is_active)

    message = make_message("start")
    message.is_active_chat = False
    await stub.dispatch_commands(message)
    assert calls == []

    message.is_active_chat = True
    await stub.dispatch_commands(message)
    assert calls == [1]


async def test_stop_handlers_propagates():
    from pytdbot.exception import StopHandlers

    stub = CommandClientStub()

    async def stopper(client, message):
        raise StopHandlers

    stub.add_command(stopper, "halt")

    with pytest.raises(StopHandlers):
        await stub.dispatch_commands(make_message("halt"))


async def test_exception_logged_and_continues():
    stub = CommandClientStub()
    calls = []

    async def broken(client, message):
        raise ValueError("boom")

    async def second(client, message):
        calls.append(2)

    stub.add_command(broken, "cmd")
    stub.add_command(second, "cmd")

    await stub.dispatch_commands(make_message("cmd"))
    assert calls == [2], "second handler must still run"


async def test_multiple_handlers_one_command_order():
    stub = CommandClientStub()
    calls = []

    async def first(client, message):
        calls.append("first")

    async def second(client, message):
        calls.append("second")

    stub.add_command(first, "cmd")
    stub.add_command(second, "cmd")
    await stub.dispatch_commands(make_message("cmd"))
    assert calls == ["first", "second"]


async def test_non_text_message_short_circuits():
    stub = CommandClientStub()
    calls = []

    async def activate(client, message):
        calls.append(1)

    stub.add_command(activate, "start")

    photo = dict_to_obj(
        {
            "@type": "updateNewMessage",
            "message": {
                "@type": "message",
                "id": 2,
                "sender_id": {"@type": "messageSenderUser", "user_id": 42},
                "chat_id": -100,
                "content": {
                    "@type": "messagePhoto",
                    "photo": {"@type": "photo", "has_stickers": False, "sizes": []},
                    "caption": {
                        "@type": "formattedText",
                        "text": "start",
                        "entities": [],
                    },
                },
                "is_outgoing": False,
                "is_channel_post": False,
                "date": 2000000000,
                "edit_date": 0,
            },
        }
    ).message
    await stub.dispatch_commands(photo)
    assert calls == [], "caption text must not be routed"


async def test_dispatcher_runs_in_linear_list():
    """End-to-end: dispatcher participates in the normal handler order."""
    stub = CommandClientStub()
    order = []

    async def moderation(client, message):
        order.append("moderation")

    async def activate(client, message):
        order.append("command")

    async def pass_through(client, message):
        order.append("pass-through")

    from pytdbot.handlers.handler import Handler

    stub._handlers["updateNewMessage"] = [
        Handler(moderation, "updateNewMessage", None, 0, True)
    ]
    stub.add_command(activate, "start", position=3)
    stub._handlers["updateNewMessage"].append(
        Handler(pass_through, "updateNewMessage", None, None, True)
    )
    stub._update_handlers()

    await run_linear(stub, make_message("start"))
    assert order == ["moderation", "command", "pass-through"]


async def test_remove_command():
    stub = CommandClientStub()
    calls = []

    async def activate(client, message):
        calls.append(1)

    stub.add_command(activate, "start", "go")
    stub.add_command(activate, "search", prefix=True)

    assert stub.remove_command(activate) is True
    await stub.dispatch_commands(make_message("start"))
    await stub.dispatch_commands(make_message("search x"))
    assert calls == []
    assert stub._command_handlers == {}
    assert stub._prefix_handlers == []


async def test_reload_clears_plugin_commands_only():
    stub = CommandClientStub()
    calls = []

    async def plugin_h(client, message):
        calls.append("plugin")

    async def local_h(client, message):
        calls.append("local")

    stub.add_command(plugin_h, "cmd", is_from_plugin=True)
    stub.add_command(local_h, "cmd2", is_from_plugin=False)

    stub._command_handlers = {
        c: [h for h in hs if not h.is_from_plugin]
        for c, hs in stub._command_handlers.items()
    }
    stub._command_handlers = {c: hs for c, hs in stub._command_handlers.items() if hs}
    stub._prefix_handlers = [
        (p, h) for p, h in stub._prefix_handlers if not h.is_from_plugin
    ]
    stub._update_handlers()

    await stub.dispatch_commands(make_message("cmd"))
    await stub.dispatch_commands(make_message("cmd2"))
    assert calls == ["local"]


async def test_command_handler_timeout():
    stub = CommandClientStub(default_handlers_timeout=0.05)
    calls = []

    async def slow(client, message):
        await asyncio.sleep(1)
        calls.append("never")

    stub.add_command(slow, "slow")
    await stub.dispatch_commands(make_message("slow"))
    assert calls == [], "timeout must cancel the handler"


async def test_default_timeout_none_runs_bare():
    stub = CommandClientStub()
    calls = []

    async def h(client, message):
        calls.append(1)

    stub.add_command(h, "cmd")
    await stub.dispatch_commands(make_message("cmd"))
    assert calls == [1]
