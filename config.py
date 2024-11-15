import os
from dotenv import load_dotenv


# Change the working directory to the 'app' directory
os.chdir("C:/Users/isdx/OneDrive/Desktop/Project-R_data/Project_R/app") #specify path of your config.py file
print("Current working directory:", os.getcwd())
# Load environment variables from the .env file
load_dotenv()

class Settings:
    MONGODB_URL = os.getenv("MONGODB_URL")  # Fetch from environment variable
    DATABASE_NAME = os.getenv("DATABASE_NAME")  # Fetch from environment variable

settings = Settings()

# Print to verify
print("MONGODB_URL:", settings.MONGODB_URL)
print("DATABASE_NAME:", settings.DATABASE_NAME)
