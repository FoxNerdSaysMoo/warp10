"""An alternative to Sanic's builtin signals, because we want to be able to change them during runtime"""
from asyncio import coroutine

signals = {}


def add_signal(signal_name: str, coro: coroutine, *args):
    signals[signal_name] = signals.get(signal_name, []) + [coro]


async def dispatch(signal_name: str, *args):
    print("[DEBUG] Dispatching", signal_name, signals.get(signal_name, []))
    for signal in signals.get(signal_name, []):
        await signal(*args)
