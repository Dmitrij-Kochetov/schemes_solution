import os
import asyncio
import logging
from motor.metaprogramming import AsyncCommand

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dynaconf import Dynaconf
from motor.motor_asyncio import AsyncIOMotorClient
from src.exceptions import DisposeException, StartServerException

from src.infrastracture.mongo.session import get_mongo_session
from src.presentation.app import setup_routers

logger = logging.getLogger(__name__)


class Application:
    def __init__(
        self,
        config: Dynaconf,
        app: FastAPI,
        mongo: AsyncIOMotorClient,
    ) -> None:
        self._config = config
        self._app = app
        self._mongo = mongo

    @classmethod
    async def from_config(cls, settings_path: str) -> "Application":
        config = Dynaconf(
            root_path=settings_path,
            envvar_prefix="DYNACONF",
            settings_files=["settings.toml", ".secrets.toml"],
        )
        print(config)
        logging.basicConfig(
            level=config.log.level,
            format=config.log.format,
        )
        logger.info("Initializing mongo session")
        mongo = get_mongo_session(config.mongo.mongo_path)
        logger.info("Initializing application")

        app = FastAPI(
            title=config.api.project_name,
            docs_url=config.api.prefix + "/docs",
        )

        app.state.mongo = mongo

        logger.info("Initializing middlewares")
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in config.api.backend_cors_origins],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        logger.info("Initializing routes")
        setup_routers(app, config.api.prefix)

        logger.info("Creating application")
        application = Application(
            config=config,
            app=app,
            mongo=mongo,
        )

        logger.info("Initializing application finished")
        return application

    async def start(self) -> None:
        logger.info("HTTP server is starting")

        try:
            server = uvicorn.Server(
                config=uvicorn.Config(
                    app=self._app,
                    host=self._config.api.host,
                    port=int(self._config.api.port),
                )
            )
            await server.serve()

        except asyncio.CancelledError:
            logger.info("HTTP server has been interrupted")
        except BaseException as unexpected_error:
            logger.exception("HTTP server failed to start")

            raise StartServerException from unexpected_error

    async def dispose(self) -> None:
        logger.info("Application is shutting down...")

        dispose_errors = []
        try:
            self._mongo.close()
        except Exception as unexpected_error:
            dispose_errors.append(unexpected_error)
            logger.exception("Failed to close mongo client")
        else:
            logger.info("Mongo client has been disposed")

        if len(dispose_errors) != 0:
            logger.error("Application has been shut down with errors")
            raise DisposeException(
                "Application has shut down with errors, see logs above"
            )

        logger.info("Application has successfully shut down")
