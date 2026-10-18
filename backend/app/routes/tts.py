from fastapi import APIRouter
from pydantic import BaseModel

from app.services.tts_service import (
    generate_multilingual_audio
)


router = APIRouter(
    prefix="/api/tts",
    tags=["Text to Speech"]
)


class TTSRequest(BaseModel):
    text: str


@router.post("/")
async def generate_audio(request: TTSRequest):

    if not request.text.strip():

        return {
            "success": False,
            "message": "Text cannot be empty."
        }

    filename = generate_multilingual_audio(
        request.text
    )

    return {
        "success": True,
        "message": "Audio generated successfully.",
        "filename": filename,
        "audio_url": f"/audio/{filename}"
    }