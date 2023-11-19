from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.requests import Request
from fastapi.responses import Response
from motor.motor_asyncio import AsyncIOMotorCollection

from src.presentation.routers.dependencies import get_schemes_db



schemes = APIRouter(prefix="/schemes", tags=["schemes"])


@schemes.post(path="get_form")
def get_form(req: Request, session: Annotated[AsyncIOMotorCollection, Depends(get_schemes_db)]):
    fields = dict(req.query_params)
