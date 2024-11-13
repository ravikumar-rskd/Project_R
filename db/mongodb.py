from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings  # Assuming your settings are correctly imported

client = AsyncIOMotorClient(settings.MONGODB_URL)
database = client[settings.DATABASE_NAME]
