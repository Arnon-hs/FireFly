from motor.motor_asyncio import AsyncIOMotorClient
from data.config import (MONGO_NAME, MONGO_URL)

class Mongo:
    client: AsyncIOMotorClient = None

db = Mongo()

async def get_database():
    return db.client[MONGO_NAME]  # Укажите название вашей базы данных

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(MONGO_URL)  # Укажите URL вашего MongoDB сервера

async def close_mongo_connection():
    db.client.close()
