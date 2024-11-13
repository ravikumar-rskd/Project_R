from app.schemas.lesson_schema import LessonCreate, LessonResponse
from app.db.mongodb import database
from bson import ObjectId

async def get_all_lessons():
    lessons = await database["lessons"].find().to_list(100)
    return [LessonResponse(id=str(lesson["_id"]), **lesson) for lesson in lessons]
    
async def get_lesson(lesson_id: str):
    lesson = await database["lessons"].find_one({"_id": ObjectId(lesson_id)})
    if lesson:
        return LessonResponse(id=str(lesson["_id"]), **lesson)
    return None

async def create_lesson(lesson: LessonCreate):
    lesson_data = lesson.dict()
    result = await database["lessons"].insert_one(lesson_data)
    return LessonResponse(id=str(result.inserted_id), **lesson_data)

async def update_lesson(lesson_id: str, lesson: LessonCreate):
    await database["lessons"].update_one(
        {"_id": ObjectId(lesson_id)}, {"$set": lesson.dict()}
    )
    updated_lesson = await database["lessons"].find_one({"_id": ObjectId(lesson_id)})
    return LessonResponse(id=str(updated_lesson["_id"]), **updated_lesson)

async def delete_lesson(lesson_id: str):
    result = await database["lessons"].delete_one({"_id": ObjectId(lesson_id)})
    return result.deleted_count > 0
