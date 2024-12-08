from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.session import database

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, servers=[
        {"url": "https://myapp-383194447870.europe-west9.run.app", "description": "Production server"}
    ])
app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # vous pouvez spécifier "*" pour tout autoriser
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(api_router, prefix=settings.API_V1_STR)