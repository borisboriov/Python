from pydantic import BaseModel
from user import User
from book import Book
from bookNotAvailable import BookNotAvailableException


class Library(BaseModel):
    books: list[Book]
    users: list[User]

    def total_books(self) -> None:
        print(f"Total amount of books in library is: {len(self.books)}")

    def add_book(self, book: Book) -> None:
        book.available = True
        self.books.append(book)

    def find_book(self, title: str, author: str, year: int) -> Book | None:
        for book in self.books:
            if book.title == title and book.author == author and book.year == year and book.available:
                print(f"Found book: {book}")
                return book
        print(f"No book found with title: {title}, author: {author}, year: {year}")
        return None

    def is_book_borrow(self, book: Book) -> bool:
        if book not in self.books:
            raise BookNotAvailableException(f"Book '{book.title}' not in library")

        if not book.available:
            raise BookNotAvailableException(f"Book '{book.title}' is not available")

        return True

    def return_book(self, book: Book) -> None:
        if book in self.books:
            book.available = True
            print(f"Book '{book.title}' returned successfully")
        else:
            raise BookNotAvailableException(f"Book '{book.title}' not in library")
