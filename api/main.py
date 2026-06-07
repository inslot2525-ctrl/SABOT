from fastapi import FastAPI

from api.routes import router
from api.upload import (
    router as upload_router
)
from api.build_index import (
    router as build_router
)

app = FastAPI(
    title="SalesMind AI"
)

app.include_router(router)

app.include_router(
    upload_router
)

app.include_router(
    build_router
)


@app.get("/")
def root():

    return {
        "message":
        "SalesMind AI Running"
    }