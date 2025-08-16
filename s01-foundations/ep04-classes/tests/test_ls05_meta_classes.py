from uuid import UUID
from src.ls05_meta_classes import Book, BookRepository

book_repository = BookRepository()

def test_add_book():
    book_id = book_repository.add_book("1984", "George Orwell", 1949)
    assert book_id is not None
    assert isinstance(book_id, UUID)

def test_get_books():
    book_repository.add_book("Brave New World", "Aldous Huxley", 1932)
    books = book_repository.get_books()
    assert len(books) > 0
    assert all(isinstance(book, Book) for book in books)

def test_get_book_by_id():
    book_id = book_repository.add_book("Fahrenheit 451", "Ray Bradbury", 1953)
    book = book_repository.get_book_by_id(book_id)
    assert book is not None
    assert isinstance(book, Book)
    assert book.id == book_id

def test_remove_book():
    book_id = book_repository.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    result = book_repository.remove_book(book_id)
    assert result is True
    assert book_repository.get_book_by_id(book_id) is None