"""
Data loading script for populating the students table from CSV
Run this once after creating the database schema
"""
import csv
from main import Session, Student


def load_students_from_csv(csv_file='students.csv'):
    session = Session()

    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            # Skip header if your CSV has one
            next(csv_reader, None)

            count = 0
            for row in csv_reader:
                student = Student(
                    first_name=row[0],
                    last_name=row[1],
                    faculty=row[2],
                    course=row[3],
                    assessment=float(row[4])
                )
                session.add(student)
                count += 1

                if count % 10 == 0:
                    print(f"Loaded {count} students...")

            session.commit()
            print(f"\n✅ Successfully loaded {count} students into database!")

            # Show summary
            total = session.query(Student).count()
            print(f"📊 Total students in database: {total}")

    except FileNotFoundError:
        print(f"❌ Error: '{csv_file}' not found in current directory")
    except Exception as e:
        session.rollback()
        print(f"❌ Error loading data: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    print("🚀 Loading students from CSV...\n")
    load_students_from_csv()