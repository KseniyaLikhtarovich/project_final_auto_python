from pages.base_page import BasePage
from locators.subcategory_page_locators import SubcategoryPageLocators


class SubcategoryPage(BasePage):

    def subcategory_page(self, test_case_2_data):
        subcategory = self.find_element(SubcategoryPageLocators.LOCATOR_SUBCATEGORY)
        assert subcategory.text == test_case_2_data["output"]["duck"]

    def add_to_cart(self, test_case_2_data):
        add_to_cart = self.find_element(SubcategoryPageLocators.LOCATOR_ADD_TO_CART_BUTTON)
        add_to_cart.click()

        product_added = self.find_element(SubcategoryPageLocators.LOCATOR_PRODUCT_ADDED)
        self.find_text_in_element(SubcategoryPageLocators.LOCATOR_PRODUCT_ADDED, test_case_2_data["output"]["product"])
        assert product_added.text == test_case_2_data["output"]["product"]

    def open_cart_page(self):
        cart = self.find_element(SubcategoryPageLocators.LOCATOR_CART_BUTTON)
        cart.click()
