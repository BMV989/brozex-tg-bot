import asyncio
import logging
import sys
import config as cfg
from aiogram import Bot, Dispatcher
from handlers.user_router import rt as user_router


def bot_and_dp_setup() -> tuple[Bot, Dispatcher]:
    bot = Bot(token=cfg.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(user_router)
    return bot, dp


def webhook_setup() -> None:
    pass


async def log_polling_setup() -> None:
    bot, dp = bot_and_dp_setup()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(log_polling_setup())
