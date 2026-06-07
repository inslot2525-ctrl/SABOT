from fastapi import APIRouter

from ingestion.ingest import (
    build_index
)

router = APIRouter()


@router.post(
    "/build-index"
)
def create_index():

    build_index()

    return {
        "message":
        "Knowledge base created successfully"
    }