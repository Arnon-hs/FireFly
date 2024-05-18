from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorCollection
from .Mongo import get_database

class ChatStats:
    def __init__(self, chat_title, total_messages_count=0, users=None):
        self.chat_title = chat_title
        self.total_messages_count = total_messages_count
        self.users = users if users else {}

    @classmethod
    async def get_collection(cls):
        db = await get_database()
        return db['chat_stats']

    @classmethod
    async def get_or_create(cls, chat_title):
        collection = await cls.get_collection()
        chat_stats_data = await collection.find_one({"chat_title": chat_title})
        if chat_stats_data:
            return cls(**chat_stats_data)
        else:
            chat_stats = cls(chat_title)
            await collection.insert_one(chat_stats.__dict__)
            return chat_stats

    async def update_user_message_count(self, user_id, message_date):
        if user_id in self.users:
            self.users[user_id]['message_count'] = self.users[user_id].get('message_count', 0) + 1
            self.users[user_id]['last_message_date'] = message_date
        else:
            self.users[user_id] = {'message_count': 1, 'last_message_date': message_date}
        self.total_messages_count += 1
        collection = await self.get_collection()
        await collection.update_one({"chat_title": self.chat_title}, {"$set": self.__dict__})
