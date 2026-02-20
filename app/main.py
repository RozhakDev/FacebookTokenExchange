from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.token import router as token_router


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)

    app.include_router(
        token_router,
        prefix=settings.API_V1_PREFIX,
        tags=["Token"],
    )

    return app

app = create_app()