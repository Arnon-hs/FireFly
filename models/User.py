from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from utils.helpers import generate_referral_code, generate_referral_link
from models.Mongo import get_database

class User:
    def __init__(self, user_id, first_name=None, last_name=None, username=None, referrer_id=None):
        self.id = str(user_id)
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.referrer_id = referrer_id
        self.is_admin = False
        self.is_registered = True
        self.registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.email = ""
        self.referral_code = generate_referral_code()
        self.referral_link = generate_referral_link(self.referral_code)
        self.referral_count = 0
        self.balance = 0
        self.reputation = 0
        self.message_cost = 0.5
        self.improvements = {}
        self.tasks_completed = []
        self.roles = [{
            "role_id": "Newbie",
            "role_name": "Glowworm Apprentice",
            "description": "Ученик Сияющего Червяка - новый участник, только начинающий свой путь в мире криптовалют и чата 'Firefly Crypto'."
        }]

    @classmethod
    async def get_collection(cls):
        db = await get_database()
        return db['users']

    @classmethod
    async def get_by_id(cls, user_id):
        collection = await cls.get_collection()
        user_data = await collection.find_one({"_id": str(user_id)})
        if user_data:
            return cls(**user_data)
        else:
            return None

    @classmethod
    async def get_or_create(cls, user_id):
        collection = await cls.get_collection()
        user_data = await collection.find_one({"_id": str(user_id)})
        if user_data:
            return cls(**user_data)
        else:
            user = cls(user_id)
            await collection.insert_one(user.__dict__)
            return user

    @classmethod
    async def get_by_referral_code(cls, referral_code):
        collection = await cls.get_collection()
        user_data = await collection.find_one({"referral_code": referral_code})
        if user_data:
            return cls(**user_data)
        else:
            return None

    @classmethod
    async def get_top_users(cls, limit):
        collection = await cls.get_collection()
        top_users = await collection.find().sort("balance", -1).limit(limit).to_list(length=limit)
        return [cls(**user) for user in top_users]


    async def add_balance(self, amount):
        self.balance += amount
        collection = await User.get_collection()
        await collection.update_one({"_id": self.id}, {"$set": {"balance": self.balance}})

    async def add_referral_count(self):
        self.referral_count += 1
        collection = await User.get_collection()
        await collection.update_one({"_id": self.id}, {"$set": {"referral_count": self.referral_count}})

    @staticmethod
    async def create_user_profile(bot_user, referrer_id=None):
        user_id = bot_user.user_id
        username = bot_user.username
        first_name = bot_user.first_name
        last_name = bot_user.last_name
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        referral_code = generate_referral_code()
        referral_link = generate_referral_link(referral_code)

        user = User(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            registration_date=registration_date,
            email="",
            referral_code=referral_code,
            referral_link=referral_link,
            referral_count=0,
            balance=0,
            reputation=0,
            message_cost=0.5,
            improvements={},
            tasks_completed=[],
            roles=[{
                "role_id": "Newbie",
                "role_name": "Glowworm Apprentice",
                "description": "Ученик Сияющего Червяка - новый участник, только начинающий свой путь в мире криптовалют и чата 'Firefly Crypto'."
            }]
        )

        if referrer_id:
            user.referrer_id = referrer_id

        user_dict = user.__dict__
        collection = await User.get_collection()
        await collection.insert_one(user_dict)

        return user_dict