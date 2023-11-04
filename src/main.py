import asyncio

from aiogram import (
    Bot,
    Dispatcher
)

from src import get_dispatcher
from src.core import get_default_settings
from src.core.container import Container


settings = get_default_settings()


async def main() -> None:
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    dispatcher: Dispatcher = get_dispatcher()
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    Container()
    asyncio.run(main())
