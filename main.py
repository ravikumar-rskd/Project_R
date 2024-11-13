from fastapi import FastAPI
from app.routers import lesson_router

app = FastAPI()

app.include_router(lesson_router.router, prefix="/lessons", tags=["Lessons"])

# Run the app with: uvicorn app.main:app --reload
