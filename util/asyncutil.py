import asyncio


def run_async(f):
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(f())
