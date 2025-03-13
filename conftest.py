import pytest

from main import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book


@pytest.fixture
def get_books(book):
    book.add_new_book('Оно')
    book.add_new_book('Маугли')
    book.set_book_genre('Оно', 'Ужасы')
    book.set_book_genre('Маугли', 'Мультфильмы')
    return get_books