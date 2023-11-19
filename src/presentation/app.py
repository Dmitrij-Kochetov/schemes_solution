from fastapi import FastAPI, Depends, APIRouter

from src.presentation.routers.schemes.v1 import schemes


def setup_routers(app: FastAPI, prefix: str) -> None:
    app.include_router(router=schemes, prefix=prefix)
