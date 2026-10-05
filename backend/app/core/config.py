from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str = "MovieVerse API"
    app_env: str = "development"
    debug: bool = True

    # Database
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "movieverse"
    db_user: str = "movieverse_user"
    db_pass: str = "movieverse_pass"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://"
            f"{self.db_user}:{self.db_pass}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()