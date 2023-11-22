from fastapi import FastAPI, Depends, APIRouter

from src.presentation.routers.services.scheme_searcher.v1 import scheme_searcher


def setup_routers(app: FastAPI, prefix: str) -> None:
    app.include_router(router=scheme_searcher, prefix=prefix)
    
