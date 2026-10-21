"""
Library Management System.

Demonstrates association between Book, Member, and Library classes.
"""


class Book:
    """Represents an individual book in catalog."""

    def __init__(self, isbn: str, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_checked_out = False

    def __repr__(self) -> str:
        return f"Book('{self.title}' by {self.author}, ISBN: {self.isbn})"


class Library:
    """Manages collection of books and checkout logic."""

    def __init__(self, name: str):
        self.name = name
        self.catalog: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        self.catalog[book.isbn] = book

    def checkout_book(self, isbn: str) -> Book:
        book = self.catalog.get(isbn)
        if not book:
            raise KeyError(f"Book with ISBN {isbn} not found.")
        if book.is_checked_out:
            raise ValueError(f"'{book.title}' is currently checked out.")
        book.is_checked_out = True
        return book

    def return_book(self, isbn: str) -> None:
        book = self.catalog.get(isbn)
        if book:
            book.is_checked_out = False


if __name__ == "__main__":
    print("=== Library Management System ===")
    lib = Library("City Central Library")
    b1 = Book("978-0132350884", "Clean Code", "Robert C. Martin")
    b2 = Book("978-0134685991", "Effective Java", "Joshua Bloch")

    lib.add_book(b1)
    lib.add_book(b2)

    borrowed = lib.checkout_book("978-0132350884")
    print(f"Checked out: {borrowed.title}")
    lib.return_book("978-0132350884")
    print(f"Returned successfully. Is checked out? {b1.is_checked_out}")
