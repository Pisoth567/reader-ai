from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes.tts import router as tts_router


app = FastAPI(
    title="AI Multilingual Reader"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount(
    "/audio",
    StaticFiles(directory="audio"),
    name="audio"
)


app.include_router(tts_router)


@app.get("/")
def root():
    return {
        "message": "AI Multilingual Reader API is running"
    }