from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def type_text(self, locator, text, clear_first=True):
        element = self.wait_for_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def is_displayed(self, locator):
        try:
            return self.wait_for_element(locator).is_displayed()
        except:
            return False

