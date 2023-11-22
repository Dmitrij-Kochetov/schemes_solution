from re import A
import pytest
from unittest.mock import AsyncMock
from unittest import TestCase

from src.application.services.schemes_searcher.schemes_searcher import SchemesSearcher


@pytest.mark.asyncio
async def test_exsisting_scheme() -> None:
    mock_repo = AsyncMock()
    mock_repo.get_by_fields.return_value = {"name": "myform"}

    ss = SchemesSearcher(mock_repo)
    result = await ss.search_fields(
        {"phone": "+7 910 543 78 11", "email": "foo@bar.com"}
    )

    assert result == "myform"


@pytest.mark.asyncio
async def test_not_existing_scheme() -> None:
    mock_repo = AsyncMock()
    mock_repo.get_by_fields.return_value = None

    ss = SchemesSearcher(mock_repo)
    result = await ss.search_fields(
        {"phone": "+7 910 543 78 11", "email": "foo@bar.com"}
    )

    assert result == {"phone": "phone", "email": "email"}
