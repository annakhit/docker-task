import os

class Settings:
    """Конфигурация приложения"""

    USERNAME: str = os.getenv("USERNAME", "cori")

    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "kubsu")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "kubsu")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "kubsu")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    TESTING: bool = os.getenv("TESTING", "false").lower() == "true"

    @property
    def DATABASE_URL_FOR_TEST(self) -> str:
        return f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    PORT: int = int(os.getenv("PORT", 58529))

    def get_database_url(self) -> str:
        if self.TESTING:
            return self.DATABASE_URL_FOR_TEST
        return self.DATABASE_URL

settings = Settings()
