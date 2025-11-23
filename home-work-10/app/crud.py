from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
from app import models, schemas

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100, faculty: Optional[str] = None, course: Optional[str] = None):
    query = db.query(models.Student)
    if faculty:
        query = query.filter(models.Student.faculty == faculty)
    if course:
        query = query.filter(models.Student.course == course)
    return query.offset(skip).limit(limit).all()

def get_students_count(db: Session, faculty: Optional[str] = None, course: Optional[str] = None) -> int:
    query = db.query(func.count(models.Student.id))
    if faculty:
        query = query.filter(models.Student.faculty == faculty)
    if course:
        query = query.filter(models.Student.course == course)
    return query.scalar()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student_update: schemas.StudentUpdate):
    db_student = get_student(db, student_id)
    if not db_student:
        return None
    update_data = student_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_student, field, value)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int) -> bool:
    db_student = get_student(db, student_id)
    if not db_student:
        return False
    db.delete(db_student)
    db.commit()
    return True
