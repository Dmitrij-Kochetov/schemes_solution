from src.application.schemes.interfaces import SchemesRepo
from src.application.services.schemes_searcher.validators import validator


class SchemesSearcher:
    def __init__(self, repo: SchemesRepo):
        self.repo = repo

    async def search_fields(self, fields: dict[str, str]) -> str | dict[str, str]:
        for field in fields:
            fields[field] = validator.validate(fields[field]).value

        result = await self.repo.get_by_fields(fields=fields)

        if result is None:
            return fields

        return result["name"]
