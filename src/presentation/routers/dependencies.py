from typing import Annotated

from fastapi.requests import Request


async def get_schemes_db(request: Request):
    return request.app.state.mongo.schemes
