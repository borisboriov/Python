from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Optional
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/", response_model=schemas.StudentList)
def list_students(skip: int = 0, limit: int = 100, faculty: Optional[str] = None, 
                  course: Optional[str] = None, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit, faculty=faculty, course=course)
    total = crud.get_students_count(db, faculty=faculty, course=course)
    return {"total": total, "students": students}

@router.get("/{student_id}", response_model=schemas.Student)
def get_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.post("/", response_model=schemas.Student, status_code=201)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.put("/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id, student)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.delete("/{student_id}", response_model=schemas.MessageResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    if not crud.delete_student(db, student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted"}
