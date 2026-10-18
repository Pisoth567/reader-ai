from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import uuid

from app.services.ocr_service import extract_text


router = APIRouter(
    prefix="/api/ocr",
    tags=["OCR"]
)


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/")
async def read_image(file: UploadFile = File(...)):

    allowed_types = {
        "image/jpeg",
        "image/png",
        "image/webp"
    }

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, PNG and WEBP images are supported."
        )

    extension = Path(file.filename).suffix.lower()

    filename = f"{uuid.uuid4()}{extension}"

    file_path = UPLOAD_DIR / filename

    try:

        content = await file.read()

        with open(file_path, "wb") as buffer:
            buffer.write(content)

        extracted_text = extract_text(
            str(file_path)
        )

        return {
            "message": "OCR completed successfully",
            "filename": filename,
            "text": extracted_text
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"OCR failed: {str(error)}"
        )