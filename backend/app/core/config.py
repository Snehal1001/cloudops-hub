from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    DATABASE_URL: str

    FRONTEND_URL: str

    AZURE_STORAGE_CONNECTION_STRING: str
    AZURE_STORAGE_CONTAINER: str

    model_config =  SettingsConfigDict(
        env_file = ".env",
        # env_file_encoding="utf-8"
    )

settings = Settings()