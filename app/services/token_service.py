import requests
import json
from requests import RequestException
from app.core.config import settings


class TokenExchangeError(Exception):
    """Custom exception for token exchange errors."""


class TokenService:

    @staticmethod
    def change_token(app_id, access_token: str) -> str:
        try:
            response = requests.post(
                settings.FACEBOOK_SESSION_URL,
                data={
                    "access_token": access_token,
                    "format": "json",
                    "new_app_id": app_id.value,
                    "generate_session_cookies": "0",
                },
                timeout=30,
            )

            data = response.json() if response.text else {}
        except RequestException as exc:
            raise TokenExchangeError(f"Network error: {str(exc)}") from exc
        
        if isinstance(data, dict) and data.get("access_token"):
            new_token = data["access_token"]

            try:
                requests.get(
                    settings.FACEBOOK_PERMISSION_URL,
                    params={"method": "DELETE", "access_token": access_token},
                    timeout=15,
                )
            except RequestException:
                pass
            
            return new_token
        
        raise TokenExchangeError(
            f"Unable to change token. Response: {json.dumps(data, ensure_ascii=False)}"
        )