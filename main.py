import asyncio
import logging
import sys
import config as cfg


def webhook_setup():
    pass


async def log_polling_setup():
    pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(log_polling_setup())
