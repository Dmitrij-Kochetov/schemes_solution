from abc import ABC, abstractmethod


class SchemesRepo(ABC):
    async def get_by_fields(self, fields: dict):
        raise NotImplementedError

    async def get_by_name(self, name: str):
        raise NotImplementedError

    async def create(self, fields: dict):
        raise NotImplementedError
