from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators
from time import sleep


class CartPage(BasePage):

    def cart_page(self, tc_2_data):
        cart = self.find_element(CartPageLocators.LOCATOR_CART)
        print(cart.text)
        assert cart.text == tc_2_data["output"]["order"]

    def add_products_and_update_order(self, tc_2_data):
        quantity_field = self.find_element(CartPageLocators.LOCATOR_QUANTITY)
        quantity_field.clear()
        quantity_field.send_keys(tc_2_data["input"]["quantity"])

        update_button = self.find_element(CartPageLocators.LOCATOR_UPDATE_BUTTON)
        update_button.click()
        sleep(1)

        updated_quantity = self.find_element(CartPageLocators.LOCATOR_UPDATE_QUANTITY)
        print(updated_quantity.text)
        assert updated_quantity.text == tc_2_data["output"]["order_quantity"]

        updated_payment_due = self.find_element(CartPageLocators.LOCATOR_UPDATE_PAYMENT_DUE)
        print(updated_payment_due.text)
        assert updated_payment_due.text == tc_2_data["output"]["payment_due"]

    def cart_is_empty(self, tc_2_data):
        remove_button = self.find_element(CartPageLocators.LOCATOR_REMOVE_BUTTON)
        remove_button.click()

        empty_cart = self.find_element(CartPageLocators.LOCATOR_EMPTY_CART)
        print(empty_cart.text)
        assert empty_cart.text == tc_2_data["output"]["empty_cart_msg"]
