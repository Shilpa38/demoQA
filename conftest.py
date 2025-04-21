import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.checkbox_page import CheckboxPage
from pageObjects.dynamic_properties_page import DynamicPropertiesPage
from pageObjects.practice_form_page import PracticeFormPage
from pageObjects.bookstore_page import BookstorePage


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    # options.add_argument("--headless")  # Uncomment if running in CI

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@pytest.fixture
def checkbox_page(driver):
    return CheckboxPage(driver)


@pytest.fixture
def dynamic_props_page(driver):
    return DynamicPropertiesPage(driver)


@pytest.fixture
def practice_form_page(driver):
    return PracticeFormPage(driver)


@pytest.fixture
def bookstore_page(driver):
    return BookstorePage(driver)
