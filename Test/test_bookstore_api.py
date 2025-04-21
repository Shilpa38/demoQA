from utils.api_utils import get_books_from_api

def test_books_data_matches_api(driver, bookstore_page):
    bookstore_page.go_to()
    ui_books = bookstore_page.get_books_data()
    api_books = get_books_from_api()
    assert ui_books == api_books
