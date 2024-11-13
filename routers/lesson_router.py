from fastapi import APIRouter, HTTPException, status
from app.schemas.lesson_schema import LessonCreate, LessonResponse
from app.services import lesson_service

router = APIRouter()

@router.get("/", response_model=list[LessonResponse])
async def read_lessons():
    return await lesson_service.get_all_lessons()

@router.get("/{lesson_id}", response_model=LessonResponse)
async def read_lesson(lesson_id: str):
    lesson = await lesson_service.get_lesson(lesson_id)
    if lesson is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    return lesson

@router.post("/", response_model=LessonResponse, status_code=status.HTTP_201_CREATED)
async def create_lesson(lesson: LessonCreate):
    return await lesson_service.create_lesson(lesson)

@router.put("/{lesson_id}", response_model=LessonResponse)
async def update_lesson(lesson_id: str, lesson: LessonCreate):
    updated_lesson = await lesson_service.update_lesson(lesson_id, lesson)
    if updated_lesson is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    return updated_lesson

@router.delete("/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lesson(lesson_id: str):
    success = await lesson_service.delete_lesson(lesson_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
