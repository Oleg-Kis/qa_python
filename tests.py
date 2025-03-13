import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, book):
        # создаем экземпляр (объект) класса BooksCollector
                # добавляем две книги
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(book.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_fantastic(self, book):
        book.add_new_book('Гордость и предубеждение и зомби')
        book.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert book.get_books_genre()['Гордость и предубеждение и зомби'] == 'Фантастика'

    def test_get_book_genre_detective(self, book):
        book.add_new_book('Десять негритят')
        book.set_book_genre('Десять негритят', 'Детективы')
        assert book.get_book_genre('Десять негритят') == 'Детективы'

    def test_get_books_with_specific_genre_horrors(self, book):
        book.add_new_book('Оно')
        book.add_new_book('Десять негритят')
        book.set_book_genre('Оно', 'Ужасы')
        book.set_book_genre('Десять негритят', 'Детективы')
        assert book.get_books_with_specific_genre('Ужасы') == ['Оно']

    def test_get_books_genre_two_books(self, book):
        book.add_new_book('Оно')
        book.add_new_book('Десять негритят')
        book.set_book_genre('Оно', 'Ужасы')
        book.set_book_genre('Десять негритят', 'Детективы')
        assert book.get_books_genre() == {'Оно': 'Ужасы', 'Десять негритят': 'Детективы'}

    def test_get_books_for_children_two_books(self, book):
        book.add_new_book('Оно')
        book.add_new_book('Маугли')
        book.set_book_genre('Оно', 'Ужасы')
        book.set_book_genre('Маугли', 'Мультфильмы')
        assert book.get_books_for_children() == ['Маугли']

    @pytest.mark.parametrize('name', ['Десять негритят', 'Оно', 'Маугли', 'Пикник на обочине', 'Незнайка'])
    def test_add_book_in_favorites_one_book(self, name):
        coll_favorite = BooksCollector()
        coll_favorite.add_new_book(name)
        coll_favorite.add_book_in_favorites(name)
        assert coll_favorite.get_list_of_favorites_books() == [name]

    def test_delete_book_from_favorites_two_books(self, book):
        book.add_new_book('Оно')
        book.add_new_book('Десять негритят')
        book.add_book_in_favorites('Оно')
        book.add_book_in_favorites('Десять негритят')
        book.delete_book_from_favorites('Оно')
        assert book.get_list_of_favorites_books() == ['Десять негритят']

    def test_get_list_of_favorites_books_two_books(self, book):
        book.add_new_book('Оно')
        book.add_new_book('Десять негритят')
        book.add_book_in_favorites('Оно')
        book.add_book_in_favorites('Десять негритят')
        assert len(book.get_list_of_favorites_books()) == 2