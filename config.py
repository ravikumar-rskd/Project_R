import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGODB_URL = os.getenv("MONGODB_URL")
    DATABASE_NAME = os.getenv("DATABASE_NAME")

settings = Settings()

# Print to verify
print("MONGODB_URL:", settings.MONGODB_URL)
print("DATABASE_NAME:", settings.DATABASE_NAME)
