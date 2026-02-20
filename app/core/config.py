from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FacebookTokenExchange"
    API_V1_PREFIX: str = "/api/v1"
    FACEBOOK_SESSION_URL: str = "https://api.facebook.com/method/auth.getSessionforApp"
    FACEBOOK_PERMISSION_URL: str = "https://graph.facebook.com/me/permissions"

    class Config:
        env_file = ".env"


settings = Settings()