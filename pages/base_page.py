from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = "http://127.0.0.1/litecart"

    def open_main_page(self):
        self.driver.get(self.base_page)

    def find_element(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Element can't be found by {locator}"
        )

    def find_text_in_element(self, locator: tuple, text: str, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Text {text} can't be fount by {locator}"
        )
