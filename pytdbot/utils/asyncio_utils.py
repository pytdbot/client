import asyncio


def get_running_loop():
    """Get the current running event loop, or create a new one if none is running"""

    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.new_event_loop()
