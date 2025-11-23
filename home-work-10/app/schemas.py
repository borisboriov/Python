from pydantic import BaseModel, Field
from typing import Optional

class StudentBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    faculty: str = Field(..., min_length=1, max_length=100)
    course: str = Field(..., min_length=1, max_length=100)
    assessment: float = Field(..., ge=0, le=100)

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    faculty: Optional[str] = None
    course: Optional[str] = None
    assessment: Optional[float] = None

class Student(StudentBase):
    id: int
    class Config:
        from_attributes = True

class StudentList(BaseModel):
    total: int
    students: list[Student]

class MessageResponse(BaseModel):
    message: str
