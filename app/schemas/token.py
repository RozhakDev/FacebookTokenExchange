from pydantic import BaseModel, Field, field_validator
from app.core.app_registry import FacebookApp


class TokenRequest(BaseModel):
    appid: FacebookApp = Field(..., description="Target Facebook App ID (e.g., FACEBOOK_ANDROID)")
    token: str = Field(..., description="Original Access Token", min_length=10)

    @field_validator('appid', mode='before')
    @classmethod
    def validate_appid(cls, v):
        if isinstance(v, str):
            try:
                return FacebookApp[v]
            except KeyError:
                raise ValueError(f"Invalid app ID. Must be one of: {', '.join([m.name for m in FacebookApp])}")
        return v

    @field_validator('token')
    @classmethod
    def validate_token(cls, v):
        if not v or v.strip() != v:
            raise ValueError("Token cannot be empty or contain leading/trailing whitespace")
        return v


class TokenResponse(BaseModel):
    status: str
    token: str | None = None
    message: str | None = None