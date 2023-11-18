from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.requests import Request
from fastapi.responses import Response


schemes = APIRouter(prefix="/schemes", tags=["schemes"])


@schemes.post(path="get_form")
def get_form():
    pass