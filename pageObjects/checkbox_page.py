import time

from selenium.webdriver.common.by import By

from pageObjects.base_page import BasePage
class CheckboxPage(BasePage):
    def go_to(self):
        self.driver.get("https://demoqa.com/checkbox")

    def expand_all(self, driver):
        expand_all_btn = driver.find_element(By.CSS_SELECTOR, 'button[title="Expand all"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", expand_all_btn)

        # Hide ad iframe
        driver.execute_script("""
            let adFrame = document.getElementById("google_ads_iframe_/21849154601,22343295815/Ad.Plus-Anchor_0");
            if (adFrame) {
                adFrame.style.display = 'none';
            }
        """)

        time.sleep(0.5)  # wait a bit for layout update
        expand_all_btn.click()
        # self.driver.find_element(By.XPATH, "//*[@id='tree-node']/div/button[1]").click()

    def select_parent(self, label):
        self.driver.find_element(By.XPATH, f"//span[text()='{label}']/preceding-sibling::span[@class='rct-checkbox']").click()

    def are_nested_checkboxes_selected(self, label):
        node = self.driver.find_element(By.XPATH, f"//span[text()='{label}']")
        icons = node.find_elements(By.XPATH, ".//ancestor::li//span[@class='rct-icon rct-icon-check']")
        return all(icon.is_displayed() for icon in icons)
