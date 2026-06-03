from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="Sales Bot"
)

app.include_router(router)