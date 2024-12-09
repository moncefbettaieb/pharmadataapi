import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

env = os.getenv("ENVIRONMENT", "dev")
load_dotenv(f".env.{env}")
class Settings(BaseSettings):
    PROJECT_NAME: str = "Pharma Data API"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "CHANGE_ME"  # A changer en production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    FRONT_BASE_URL: str = os.getenv("FRONT_BASE_URL")

settings = Settings()
