import csv
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

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


# Создаём таблицу
Base.metadata.create_all(engine)

# Читаем CSV и добавляем
session = Session()

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student = Student(
            last_name=row["Фамилия"],
            first_name=row["Имя"],
            faculty=row["Факультет"],
            course=row["Курс"],
            assessment=float(row["Оценка"])
        )
        session.add(student)

session.commit()
print("Все студенты добавлены в БД")
session.close()