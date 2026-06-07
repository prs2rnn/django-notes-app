from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")
    SECRET_KEY: str = "very-secret-key"
    DEBUG: bool = True
    ALLOWED_HOSTS: str = "127.0.0.1,localhost"
    CSRF_TRUSTED_ORIGINS: str = "http://your_domain"
    HTTPS_ENABLED: bool = False

    DB_ENGINE: str = "sqlite"
    DB_NAME: str = "db.sqlite3"
    DB_USER: str = ""
    DB_PASSWORD: str = ""
    DB_HOST: str = ""
    DB_PORT: str = ""


setting = Setting()
