AQA Yandex 4 sprint
1. test_add_new_book_name_too_long_empty_books_genre - Негативный тест на неуспешное добавление в список книг, книги 
с  именем больше 41 символа и пустым именем.
2. test_add_new_book_add_two_books - Проверка, что добавленные 2 книги увеличивают словарь books_genre.
3. test_add_new_book_valid_name  - Проверка добавления книг с валидными именами в словарь books_genre.
4. test_add_new_book_empty_genre - Проверка что добавление книги без жанра не попадает в список жанров.
5. test_set_book_genre - Проверка добавления книги и жанра в словарь books_genre.
6. test_set_book_genre_not_valid_genre_empty_genre - Негативная проверка на добавление книги с не поддерживаемым жанром.
7. test_get_books_with_specific_genre - Проверка вывода книг по соответствующему жанру.
8. test_get_books_with_specific_genre_not_valid_genre_empty_genre - Негативная проверка, что книга с неподдерживаемым 
жанром не попадает в список книг с определенным жанром. 
9. test_get_books_for_children - Проверка добавления книги с детским жанром в список детских книг. 
10. test_get_books_for_children_not_valid_genre - Проверка того, что книги для взрослых не попадают в список детских 
книг.
11. delete_book_from_favorites_empty_favorites - Проверка, что при удалении добавленной книги в Избранное, список будет 
пустым.
12. test_get_list_of_favorites_books_not_empty_favorites - Проверка, что при добавлении книги в Избранное, список книг 
в Избранном не пустой.
13. test_add_book_in_favorites_name_contained_in_favorites_true - Проверка добавления книг в Избранное.