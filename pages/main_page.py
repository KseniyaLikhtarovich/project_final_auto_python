from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def login(self, test_case_1_data):
        email_field = self.find_element(MainPageLocators.LOCATOR_EMAIL)
        email_field.send_keys(test_case_1_data["input"]["email"])

        password_field = self.find_element(MainPageLocators.LOCATOR_PASSWORD)
        password_field.send_keys(test_case_1_data["input"]["password"])

        button = self.find_element(MainPageLocators.LOCATOR_LOGIN_BUTTON)
        button.click()

        log_in = self.find_element(MainPageLocators.LOCATOR_ACCOUNT)
        assert log_in.text == test_case_1_data["output"]["account"]

    def open_edit_account_page(self):
        edit_link = self.find_element(MainPageLocators.LOCATOR_EDIT_ACCOUNT_BUTTON)
        edit_link.click()

    def open_categories_page(self):
        categories_link = self.find_element(MainPageLocators.LOCATOR_CATEGORIES_BUTTON)
        categories_link.click()
