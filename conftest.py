import pytest
from main import BooksCollector


@pytest.fixture(scope='session')
def books():
    books = BooksCollector()
    return books
