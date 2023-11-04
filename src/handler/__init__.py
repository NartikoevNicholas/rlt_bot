from src.handler.v1 import echo_handler, start_handler

routers = [
    start_handler.router,
    echo_handler.router
]


__all__ = [
    'routers'
]
