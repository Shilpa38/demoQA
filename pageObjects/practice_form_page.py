from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
class PracticeFormPage(BasePage):
    def go_to(self):
        self.driver.get("https://demoqa.com/automation-practice-form")

    def submit_empty_form(self, driver):
        self.driver = driver
        submit_btn = driver.find_element(By.ID, "submit")
        actions = ActionChains(driver)
        actions.move_to_element(submit_btn).click().perform()

    def is_validation_displayed(self, field_name):
        if field_name == "First Name":
            return self.driver.execute_script("""
                    return document.getElementById('firstName').checkValidity() === false;
                """)