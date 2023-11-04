from aiogram import Dispatcher

from src.handler import routers


def get_dispatcher() -> Dispatcher:
    dp = Dispatcher()

    for router in routers:
        dp.include_router(router)

    return dp


__all__ = [
    'get_dispatcher'
]
