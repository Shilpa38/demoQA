import requests

def get_books_from_api():
    response = requests.get("https://demoqa.com/BookStore/v1/Books")
    data = response.json()["books"]
    return [{"title": book["title"], "author": book["author"]} for book in data]