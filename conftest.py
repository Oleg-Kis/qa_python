import pytest

from main import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book


#@pytest.fixture
#def get_books():
    #get_books = ({'Оно': 'Ужасы', 'Маугли': 'Мультфильмы'})
    #return get_books