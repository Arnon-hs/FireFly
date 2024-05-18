from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from models.Mongo import get_database

class Command:
    def __init__(self, command_name, command_description):
        self.name = command_name
        self.description = command_description

    @classmethod
    async def get_collection(cls):
        db = await get_database()
        return db['commands']

    @classmethod
    async def create(cls, command_name, command_description):
        command = cls(command_name, command_description)
        collection = await cls.get_collection()
        await collection.insert_one(command.__dict__)
        return command

    @classmethod
    async def find_by_name(cls, command_name):
        collection = await cls.get_collection()
        command_data = await collection.find_one({"name": command_name})
        if command_data:
            return cls(**command_data)
        else:
            return None

    @classmethod
    async def find_all(cls):
        collection = await cls.get_collection()
        commands_data = await collection.find({}).to_list(None)
        commands = [cls(**command_data) for command_data in commands_data]
        return commands

    async def save(self):
        collection = await self.get_collection()
        await collection.update_one({"name": self.name}, {"$set": self.__dict__}, upsert=True)

    async def delete(self):
        collection = await self.get_collection()
        await collection.delete_one({"name": self.name})
