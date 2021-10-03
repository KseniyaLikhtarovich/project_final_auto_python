from pages.base_page import BasePage
from locators.subcategory_page_locators import SubcategoryPageLocators


class SubcategoryPage(BasePage):

    def subcategory_page(self, tc_2_data):
        subcategory = self.find_element(SubcategoryPageLocators.LOCATOR_SUBCATEGORY)
        print(subcategory.text)
        assert subcategory.text == tc_2_data["output"]["duck"]

    def add_to_cart(self, tc_2_data):
        add_to_cart = self.find_element(SubcategoryPageLocators.LOCATOR_ADD_TO_CART_BUTTON)
        add_to_cart.click()

        product_added = self.find_element(SubcategoryPageLocators.LOCATOR_PRODUCT_ADDED)
        self.find_text_in_element(SubcategoryPageLocators.LOCATOR_PRODUCT_ADDED, tc_2_data["output"]["product"])
        print(product_added.text)
        assert product_added.text == tc_2_data["output"]["product"]

    def open_cart_page(self):
        cart = self.find_element(SubcategoryPageLocators.LOCATOR_CART_BUTTON)
        cart.click()
