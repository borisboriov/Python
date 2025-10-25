from library import Library
from book import Book
from user import User
from bookNotAvailable import BookNotAvailableException

if __name__ == '__main__':
    # Создание данных
    book1 = Book(title="Python Programming", author="John Smith", year=2020,
                 available=True, categories=["Programming"])
    book2 = Book(title="Data Science", author="Jane Doe", year=2021,
                 available=False, categories=["Data"])

    user1 = User(name="Борис", email="boris@example.com", membership_id="001")

    library = Library(books=[book1, book2], users=[user1])

    # Тесты
    print("=== Тест 1: Количество книг ===")
    library.total_books()

    print("\n=== Тест 2: Поиск книги ===")
    library.find_book("Python Programming", "John Smith", 2020)

    print("\n=== Тест 3: Доступность (доступна) ===")
    try:
        print(f"Книга доступна: {library.is_book_borrow(book1)}")
    except BookNotAvailableException as e:
        print(f"Ошибка: {e}")

    print("\n=== Тест 4: Доступность (недоступна) ===")
    try:
        library.is_book_borrow(book2)
    except BookNotAvailableException as e:
        print(f"Ошибка: {e}")

    print("\n=== Тест 5: Возврат книги ===")
    library.return_book(book2)
    print(f"Книга доступна после возврата: {library.is_book_borrow(book2)}")

    print("\n=== Тест 6: Валидация email ===")
    try:
        User(name="Test", email="invalid", membership_id="002")
    except Exception as e:
        print(f"Ошибка: {e}")
