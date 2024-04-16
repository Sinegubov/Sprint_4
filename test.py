import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def books(self):
        return BooksCollector()

    @pytest.mark.parametrize("book_name", ["Буратино", "10 негритят", "Дракула"])
    def test_add_new_book(self, books, book_name):
        books.add_new_book(book_name)
        assert book_name in books.books_genre

    @pytest.mark.parametrize('book_name, genre', [
        ('Буратино', 'Мультфильмы'),
        ('10 негритят', 'Детективы'),
        ('Дракула', 'Ужасы'),
        ('12 Стульев', 'Комедии'),
        ('Властелин колец', 'Фантастика')
        ]
                             )
    def test_set_book_genre(self, books, book_name, genre):
        books.add_new_book(book_name)
        books.set_book_genre(book_name, genre)
        assert books.get_book_genre(book_name) == genre
