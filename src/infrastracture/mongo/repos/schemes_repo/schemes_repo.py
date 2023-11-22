from motor.motor_asyncio import AsyncIOMotorClient
from src.application.schemes.interfaces import SchemesRepo


class SchemeMongoRepo(SchemesRepo):
    def __init__(self, client: AsyncIOMotorClient) -> None:
        self.client = client

    async def get_by_fields(self, fields: dict[str, str]):
        result = await self.client.schemes.find_one(fields)
        return result

    async def get_by_name(self, name: str):
        result = await self.client.schemes.find_one({"name": name})
        if result is not None:
            result["_id"] = str(result["_id"])
        return result

    async def create(self, fields: dict):
        await self.client.schemes.insert_one(fields)
