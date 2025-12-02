"""
Data loading script for populating the students table from CSV
Creates the database schema if it doesn't exist, then loads data
Run this once after starting the database
"""
import csv
from main import Session, Student, engine, Base


def create_tables():
    """Create all tables defined in Base metadata"""
    try:
        Base.metadata.create_all(engine)
        print("✅ Database tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        raise


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
    print("🚀 Starting database setup and data loading...\n")

    print("📋 Creating database tables...")
    create_tables()

    print("\n📂 Loading students from CSV...\n")
    load_students_from_csv()