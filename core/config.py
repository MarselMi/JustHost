from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class DbSettings(BaseModel):
    url: str = os.getenv("DATABASE_URL")
    echo: bool = True


class Settings(BaseSettings):
    api_v4_prefix: str = "/api-v1"

    db: DbSettings = DbSettings()


settings = Settings()