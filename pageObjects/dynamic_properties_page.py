import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
class DynamicPropertiesPage(BasePage):
    def go_to(self):
        self.driver.get("https://demoqa.com/dynamic-properties")

    def wait_for_visible_button(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "visibleAfter"))
            )
            return True
        except TimeoutException:
            return False

    def detect_color_change(self):
        button = self.driver.find_element(By.ID, "colorChange")
        initial_color = button.value_of_css_property("color")
        time.sleep(6) # Wait to allow color change
        updated_color = button.value_of_css_property("color")
        return initial_color != updated_color
