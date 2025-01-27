from pydantic import BaseModel
from pydantic.v1 import BaseSettings


class DbSettings(BaseModel):
    url: str = f"postgres://postgres:admin@localhost:5432/vps"
    echo: bool = True


class Settings(BaseSettings):
    api_v4_prefix: str = "/api-v1"

    db: DbSettings = DbSettings()


settings = Settings()