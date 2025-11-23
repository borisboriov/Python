from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    faculty = Column(String(100), nullable=False)
    course = Column(String(100), nullable=False)
    assessment = Column(Float, nullable=False)
