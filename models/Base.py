from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Any, Dict, List, Optional, Type, TypeVar

T = TypeVar('T', bound='BaseModel')

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid object ID')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

class Base(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias='_id')

    class Config:
        json_encoders = {
            ObjectId: str,
        }

    @classmethod
    def __get_pydantic_json_schema__(cls, *, by_alias: bool = True) -> Dict[str, Any]:
        schema = super().__get_pydantic_json_schema__(by_alias=by_alias)
        schema['title'] = cls.__name__
        schema['properties']['id'] = {'type': 'string', 'format': 'ObjectId'}
        return schema

    @classmethod
    def get_collection(cls, db) -> Any:
        return db[cls.__name__.lower()]

    @classmethod
    async def find_one(cls: Type[T], db, query: dict) -> Optional[T]:
        document = await cls.get_collection(db).find_one(query)
        if document:
            return cls(**document)
        return None

    @classmethod
    async def find_all(cls: Type[T], db, query: dict) -> List[T]:
        cursor = cls.get_collection(db).find(query)
        documents = await cursor.to_list(None)
        return [cls(**doc) for doc in documents]

    async def insert(self, db) -> T:
        self.id = await self.get_collection(db).insert_one(self.dict(by_alias=True)).inserted_id
        return self

    async def update(self, db) -> T:
        await self.get_collection(db).replace_one({"_id": self.id}, self.dict(by_alias=True))
        return self

    @classmethod
    async def delete(cls, db, query: dict) -> int:
        result = await cls.get_collection(db).delete_one(query)
        return result.deleted_count
