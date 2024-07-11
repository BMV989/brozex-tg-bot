from aiogram import Router, F
from handlers.user_commands import Commands
from aiogram.filters import CommandStart
from aiogram.types import Message

rt = Router()


@rt.message(CommandStart())
async def handle_start(msg: Message):
    await msg.answer("Hello, world!")
