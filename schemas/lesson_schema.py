from pydantic import BaseModel
from typing import List, Optional

class Subtopic(BaseModel):
    title: str
    contentType: str  # 'pdf' in this case
    content: str  # URL to the PDF

class LessonBase(BaseModel):
    lessonTitle: str
    subtopics: List[Subtopic]

class LessonCreate(LessonBase):
    pass

class LessonResponse(LessonBase):
    id: Optional[str]

    class Config:
        orm_mode = True
