from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    MASTER_DB: str = r"data/MasterDHH"
    TEMP_DB: str = r"data/TempDb"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    DEBUG: bool = False
    SECRET_KEY: str = "default-secret-key"

    class Config:
        env_file = ".env"


settings = Settings()

master_db = settings.MASTER_DB

