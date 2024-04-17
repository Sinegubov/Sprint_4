1. test_add_new_book_name_too_short_empty_books_genre - Негативный тест на неуспешным добавлением в список книг, книги 
с нулевым именем.
2. test_add_new_book_name_too_long_empty_books_genre - Негативный тест на неуспешным добавлением в список книг, книги 
с  именем больше 41 символа.
3. test_add_new_book_add_two_books - Проверка, что добавленные 2 книги увеличивают словарь books_genre.
4. test_add_new_book_valid_name  - Проверка добавления книг с валидными именами в словарь books_genre.
5. test_set_book_genre - Проверка добавления книги и жанра в словарь books_genre.
6. test_set_book_genre_not_valid_genre_empty_genre - Негативная проверка на добавление книги с не поддерживаемым жанром.
7. test_get_books_with_specific_genre - Проверка вывода книг по соответствующему жанру.