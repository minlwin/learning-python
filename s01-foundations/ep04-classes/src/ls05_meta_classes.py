from dataclasses import dataclass, field
from uuid import UUID, uuid4

class SingleInstanceMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

@dataclass(frozen=True)
class Book():
    title: str
    author: str
    year: int
    id: UUID = field(default_factory=uuid4)

class BookRepository(metaclass=SingleInstanceMeta):
    def __init__(self):
        self.books:dict[UUID, Book] = {}

    def add_book(self, title:str, author:str, year:int) -> UUID:
        book = Book(title=title, author=author, year=year)
        self.books[book.id] = book
        return book.id

    def get_books(self) -> list[Book]:
        return list(self.books.values())
    
    def get_book_by_id(self, book_id: UUID) -> Book | None:
        return self.books.get(book_id)
    
    def remove_book(self, book_id: UUID) -> bool:
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False