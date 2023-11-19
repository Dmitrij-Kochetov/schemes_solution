from motor.motor_asyncio import AsyncIOMotorClient


def get_mongo_session(mongo_path: str) -> AsyncIOMotorClient:
    return AsyncIOMotorClient(mongo_path)
