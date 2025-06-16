from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application configuration loaded from environment or defaults."""
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/ptdb"
    submissions_file: str = "submissions.json"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
