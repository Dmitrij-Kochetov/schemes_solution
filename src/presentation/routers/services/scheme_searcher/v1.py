from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.requests import Request
from fastapi.responses import Response
from motor.motor_asyncio import AsyncIOMotorClient

from src.presentation.routers.dependencies import get_schemes_db
from src.application.services.schemes_searcher.schemes_searcher import SchemesSearcher
from src.infrastracture.mongo.repos.schemes_repo.schemes_repo import SchemeMongoRepo


scheme_searcher = APIRouter(prefix="/scheme_searcher", tags=["scheme_searcher"])


@scheme_searcher.post(path="/get_form")
async def get_form(
    fields: dict[str, str], db: Annotated[AsyncIOMotorClient, Depends(get_schemes_db)]
):
    repo = SchemeMongoRepo(client=db.schemes)
    schemes = SchemesSearcher(repo)
    result = await schemes.search_fields(fields)
    return result
