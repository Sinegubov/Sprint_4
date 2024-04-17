import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(scope='session')
    def books(self):
        return BooksCollector()

    def test_add_new_book_name_too_short_empty_books_genre(self, books):
        book_name = ""
        books.add_new_book(book_name)
        assert len(books.get_books_genre()) == 0

    def test_add_new_book_name_too_long_empty_books_genre(self, books):
        book_name = "a" * 42
        books.add_new_book(book_name)
        assert len(books.get_books_genre()) == 0

    def test_add_new_book_add_two_books(self, books):
        books.add_new_book("Горе от ума")
        books.add_new_book("Евгений Онегин")
        assert len(books.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name', [
        'Тихий Дон',
        'Макс Фрай',
        'Учебник по химии'
    ]
                             )
    def test_add_new_book_valid_name(self, books, book_name):
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
        ('20 тысяч лье под водой', 'Фантастика')
        ]
                             )
    def test_set_book_genre(self, books, book_name, genre):
        books.add_new_book(book_name)
        books.set_book_genre(book_name, genre)
        assert books.get_book_genre(book_name) == genre

    def test_set_book_genre_not_valid_genre_empty_genre(self, books):
        book_name = 'Человек Паук'
        genre = 'Комиксы'
        books.add_new_book(book_name)
        books.set_book_genre(book_name, genre)
        assert not books.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self, books):
        books.add_new_book("Хоббит")
        books.add_new_book("Дюна")
        books.set_book_genre("Хоббит", "Фантастика")
        books.set_book_genre("Дюна", "Фантастика")
        assert books.get_books_with_specific_genre("Фантастика") == ["Хоббит", "Дюна"]

    @pytest.mark.parametrize('book_name, genre', [
        ('Буратино', 'Мультфильмы'),])
    def test_get_books_with_specific_genre_2(self, books, book_name, genre):
        books.add_new_book(book_name)
        books.set_book_genre(book_name, genre)
        assert genre in books.genre

    def test_get_books_with_specific_genre_missing_book(self, books):
        assert len(books.get_books_with_specific_genre('Приключения')) == 0

    def test_get_books_for_children(self, books):
        books.add_new_book("Book6")
        books.set_book_genre("Book6", "Мультфильмы")
        assert "Book6" in books.get_books_for_children()
    @staticmethod
    def delete_book_from_favorites_true(books):
        book_name = "Сборник стихов"
        books.add_new_book(book_name)
        books.add_book_in_favorites(book_name)
        books.delete_book_from_favorites(book_name)
        assert books.get_list_of_favorites_books() == []

    @pytest.mark.parametrize("book_name", ["Гарри Поттер", "Каштанка", "Звездные войны"])
    def test_add_book_in_favorites_name_contained_in_favorites_true(self, books, book_name):
        books.add_new_book(book_name)
        books.add_book_in_favorites(book_name)
        favorites = books.get_list_of_favorites_books()
        assert book_name in favorites