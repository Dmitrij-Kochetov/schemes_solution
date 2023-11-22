from src.application.schemes.interfaces import SchemesRepo
from src.application.services.schemes_searcher.validators import validator


class SchemesSearcher:
    @staticmethod
    async def search_fields(fields: dict[str, str], repo: SchemesRepo) -> str | dict[str, str]:
        for field in fields:
            fields[field] = validator.validate(fields[field]).value

        result = await repo.get_by_fields(fields=fields) 

        if result is None:
            return fields

        return result["name"]       
    