from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators
from time import sleep


class CartPage(BasePage):

    def cart_page(self, test_case_2_data):
        cart = self.find_element(CartPageLocators.LOCATOR_CART)
        assert cart.text == test_case_2_data["output"]["order"]

    def add_products_and_update_order(self, test_case_2_data):
        quantity_field = self.find_element(CartPageLocators.LOCATOR_QUANTITY)
        quantity_field.clear()
        quantity_field.send_keys(test_case_2_data["input"]["quantity"])

        update_button = self.find_element(CartPageLocators.LOCATOR_UPDATE_BUTTON)
        update_button.click()
        sleep(1)

        updated_quantity = self.find_element(CartPageLocators.LOCATOR_UPDATE_QUANTITY)
        assert updated_quantity.text == test_case_2_data["output"]["order_quantity"]

        updated_payment_due = self.find_element(CartPageLocators.LOCATOR_UPDATE_PAYMENT_DUE)
        assert updated_payment_due.text == test_case_2_data["output"]["payment_due"]

    def cart_is_empty(self, test_case_2_data):
        remove_button = self.find_element(CartPageLocators.LOCATOR_REMOVE_BUTTON)
        remove_button.click()

        empty_cart = self.find_element(CartPageLocators.LOCATOR_EMPTY_CART)
        assert empty_cart.text == test_case_2_data["output"]["empty_cart_msg"]
