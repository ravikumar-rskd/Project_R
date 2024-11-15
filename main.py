from fastapi import FastAPI
from app.routers import lesson_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Allow CORS for all domains
origins = ["http://localhost:3000"]  # You can replace "*" with a list of allowed origins like ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins or specify the frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(lesson_router.router, prefix="/lessons", tags=["Lessons"])

# Run the app with: uvicorn app.main:app --reload
