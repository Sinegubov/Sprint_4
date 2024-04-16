import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(scope='session')
    def books(self):
        return BooksCollector()

    def test_add_new_book_add_two_books(self, books):
        books.add_new_book("Горе от ума")
        books.add_new_book("Евгений Онегин")
        assert len(books.get_books_genre()) == 2

    def test_add_new_book(self, books):
        book_name = "Peppa the pig"
        books.add_new_book(book_name)
        assert book_name in books.books_genre

    def test_add_new_book_empty_genre(self, books):
        book_name = "10 негритят"
        books.add_new_book(book_name)
        assert books.get_book_genre(book_name) == ''

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

    @pytest.mark.parametrize('book_name, genre', [
        ('StarTrack', 'Научная фантастика'),
        ('Алгебра', 'Учебники'),
        ('Железный человек', 'Комиксы'),
        ]
                             )
    def test_set_book_genre_not_valid_genre(self, books, book_name, genre):
        books.add_new_book(book_name)
        books.set_book_genre(book_name, genre)
        assert not books.get_book_genre(book_name) == genre
