from pydantic import BaseModel
from typing import Optional

class LessonBase(BaseModel):
    title: str
    content: str

class LessonCreate(LessonBase):
    pass

class LessonResponse(LessonBase):
    id: Optional[str]

    class Config:
        orm_mode = True
