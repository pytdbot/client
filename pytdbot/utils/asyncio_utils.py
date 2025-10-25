import asyncio


def get_running_loop():
    """Get the current running event loop"""

    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.get_event_loop_policy().get_event_loop()
