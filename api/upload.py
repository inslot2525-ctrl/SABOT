from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from pathlib import Path
from typing import List

router = APIRouter()

UPLOAD_DIR = "uploads"

Path(
    UPLOAD_DIR
).mkdir(
    parents=True,
    exist_ok=True
)


@router.post("/upload")
async def upload_files(
    files: List[UploadFile] = File(...)
):

    uploaded_files = []

    for file in files:

        filepath = (
            Path(UPLOAD_DIR)
            / file.filename
        )

        content = await file.read()

        with open(
            filepath,
            "wb"
        ) as f:

            f.write(content)

        uploaded_files.append(
            file.filename
        )

    return {
        "message": "Upload successful",
        "files": uploaded_files
    }