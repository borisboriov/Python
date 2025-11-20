from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+pymysql://root:admin@localhost:3307/PUBLIC"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    faculty = Column(String(100))
    course = Column(String(100))
    assessment = Column(Float)


# 1️⃣ Список студентов по названию факультета
def get_students_by_faculty(faculty_name):
    session = Session()
    students = session.query(Student).filter(Student.faculty == faculty_name).all()
    for s in students:
        print(f"{s.first_name} {s.last_name} - {s.faculty}")
    session.close()
    return students


# 2️⃣ Список уникальных курсов
def get_unique_courses():
    session = Session()
    courses = session.query(Student.course).distinct().all()
    for course in courses:
        print(course[0])
    session.close()
    return courses


# 3️⃣ Средний балл по факультету
def get_avg_assessment_by_faculty(faculty_name):
    session = Session()
    avg = session.query(func.avg(Student.assessment)).filter(
        Student.faculty == faculty_name
    ).scalar()
    print(f"Средний балл {faculty_name}: {avg:.2f}")
    session.close()
    return avg


# 4️⃣ Студенты по курсу с оценкой < 30
def get_students_by_course_low_assessment(course_name):
    session = Session()
    students = session.query(Student).filter(
        (Student.course == course_name) & (Student.assessment < 30)
    ).all()
    for s in students:
        print(f"{s.first_name} {s.last_name} - {s.course} - {s.assessment}")
    session.close()
    return students


if __name__ == "__main__":
    print("=== Студенты факультета АВТФ ===")
    get_students_by_faculty("АВТФ")

    print("\n=== Уникальные курсы ===")
    get_unique_courses()

    print("\n=== Средний балл по факультетам ===")
    get_avg_assessment_by_faculty("АВТФ")
    get_avg_assessment_by_faculty("ФТФ")

    print("\n=== Студенты с низкой оценкой (< 30) по курсу Мат. Анализ ===")
    get_students_by_course_low_assessment("Мат. Анализ")