import asyncio
import logging
import os
from re import A

from src.application.common.exceptions import ApplicationException

from src.app import Application

logger = logging.getLogger(__name__)


async def run() -> None:
    settings_path = os.getenv("SETTINGS")
    if settings_path is None:
        raise ApplicationException("Settings env not specified")

    app = await Application.from_config(settings_path)
    try:
        await app.start()
    finally:
        await app.dispose


def main() -> None:
    try:
        asyncio.run(run())
        exit(0)
    except SystemExit:
        exit(0)
    except ApplicationException:
        exit(70)
    except BaseException:
        logger.exception("Unexpected error occured")
        exit(70)


if __name__ == "__main__":
    main()
