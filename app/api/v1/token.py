from fastapi import APIRouter, HTTPException
from app.schemas.token import TokenRequest, TokenResponse
from app.services.token_service import TokenService, TokenExchangeError

router = APIRouter()


@router.post("/token", response_model=TokenResponse)
def exchange_token(payload: TokenRequest):
    try:
        new_token = TokenService.change_token(
            app_id=payload.appid,
            access_token=payload.token,
        )

        return TokenResponse(
            status="success",
            token=new_token,
        )
    except TokenExchangeError as exc:
        raise HTTPException(status_code=400, detail=str(exc))