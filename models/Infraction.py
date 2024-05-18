from typing import Optional
from datetime import datetime
from .Base import Base
from bson import ObjectId

class Infraction(Base):
    user_id: ObjectId
    admin_id: ObjectId
    chat_id: ObjectId
    reason: str
    timestamp: datetime

    @classmethod
    async def find_by_user_id(cls, db, user_id: str) -> Optional['Infraction']:
        return await cls.find_all(db, {"user_id": ObjectId(user_id)})
