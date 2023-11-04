from aiogram import (
    Router,
    types as tp
)
from aiogram.filters import CommandStart


router = Router(name='start')


@router.message(CommandStart())
async def command_start_handler(message: tp.Message) -> None:
    await message.answer(f"Hi, {message.from_user.full_name}!")


