import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_fantastic(self):
        coll_genre = BooksCollector()
        coll_genre.add_new_book('Гордость и предубеждение и зомби')
        coll_genre.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert coll_genre.get_books_genre()['Гордость и предубеждение и зомби'] == 'Фантастика'

    def test_get_book_genre_detective(self):
        coll_genre_detective = BooksCollector()
        coll_genre_detective.add_new_book('Десять негритят')
        coll_genre_detective.set_book_genre('Десять негритят', 'Детективы')
        assert coll_genre_detective.get_book_genre('Десять негритят') == 'Детективы'

    def test_get_books_with_specific_genre_horrors(self):
        coll_specific_horrors = BooksCollector()
        coll_specific_horrors.add_new_book('Оно')
        coll_specific_horrors.add_new_book('Десять негритят')
        coll_specific_horrors.set_book_genre('Оно', 'Ужасы')
        coll_specific_horrors.set_book_genre('Десять негритят', 'Детективы')
        assert coll_specific_horrors.get_books_with_specific_genre('Ужасы') == ['Оно']

    def test_get_books_genre_two_books(self):
        coll_dictionary = BooksCollector()
        coll_dictionary.add_new_book('Оно')
        coll_dictionary.add_new_book('Десять негритят')
        coll_dictionary.set_book_genre('Оно', 'Ужасы')
        coll_dictionary.set_book_genre('Десять негритят', 'Детективы')
        assert coll_dictionary.get_books_genre() == {'Оно': 'Ужасы', 'Десять негритят': 'Детективы'}

    def test_get_books_for_children_two_books(self):
        collector_children = BooksCollector()
        collector_children.add_new_book('Оно')
        collector_children.add_new_book('Маугли')
        collector_children.set_book_genre('Оно', 'Ужасы')
        collector_children.set_book_genre('Маугли', 'Мультфильмы')
        assert collector_children.get_books_for_children() == ['Маугли']

    @pytest.mark.parametrize('name', ['Десять негритят', 'Оно', 'Маугли', 'Пикник на обочине', 'Незнайка'])
    def test_add_book_in_favorites_one_book(self, name):
        coll_favorite = BooksCollector()
        coll_favorite.add_new_book(name)
        coll_favorite.add_book_in_favorites(name)
        assert coll_favorite.get_list_of_favorites_books() == [name]

    def test_delete_book_from_favorites_two_books(self):
        coll_del_favorite = BooksCollector()
        coll_del_favorite.add_new_book('Оно')
        coll_del_favorite.add_new_book('Десять негритят')
        coll_del_favorite.set_book_genre('Оно', 'Ужасы')
        coll_del_favorite.set_book_genre('Десять негритят', 'Детективы')
        coll_del_favorite.add_book_in_favorites('Оно')
        coll_del_favorite.add_book_in_favorites('Десять негритят')
        coll_del_favorite.delete_book_from_favorites('Оно')
        assert coll_del_favorite.get_list_of_favorites_books() == ['Десять негритят']
