from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import credit_card, login


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(login.login_router)
    app.include_router(credit_card.router)
    return app


app = get_app()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
