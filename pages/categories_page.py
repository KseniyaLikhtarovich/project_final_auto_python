from pages.base_page import BasePage
from locators.categories_page_locators import CategoriesPageLocators


class CategoriesPage(BasePage):

    def categories_page(self, test_case_2_data):
        categories = self.find_element(CategoriesPageLocators.LOCATOR_CATEGORIES)
        assert categories.text == test_case_2_data["output"]["categories"]

    def open_subcategory_page(self):
        duck_link = self.find_element(CategoriesPageLocators.LOCATOR_SUBCATEGORY_LINK)
        duck_link.click()
