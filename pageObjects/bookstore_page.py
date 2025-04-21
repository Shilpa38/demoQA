from selenium.webdriver.common.by import By

from pageObjects.base_page import BasePage
class BookstorePage(BasePage):
    def go_to(self):
        self.driver.get("https://demoqa.com/books")

    def get_books_data(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        books = []
        for row in rows:
            title = row.find_element(By.CSS_SELECTOR, ".rt-td:nth-child(2)").text.strip()
            author = row.find_element(By.CSS_SELECTOR, ".rt-td:nth-child(3)").text.strip()
            if title and author:
                books.append({"author": author, "title": title})
        return books
