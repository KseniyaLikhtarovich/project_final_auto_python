from pages.main_page import MainPage
from pages.categories_page import CategoriesPage
from pages.subcategory_page import SubcategoryPage
from pages.cart_page import CartPage
import allure


@allure.feature("Check the user can add products to cart and remove them")
def test_add_products_to_cart_and_remove_them(browser, tc_2_data):
     with allure.step("Open main page"):
        main_page = MainPage(browser)
        main_page.open_main_page()
     with allure.step("Open categories page"):
        main_page.open_categories_page()

     with allure.step("Check categories page is displayed"):
        categories_page = CategoriesPage(browser)
        categories_page.categories_page(tc_2_data)
     with allure.step("Open subcategory_page"):
        categories_page.open_subcategory_page()

     with allure.step("Check subcategory page is displayed"):
        subcategory_page = SubcategoryPage(browser)
        subcategory_page.subcategory_page(tc_2_data)
     with allure.step("Check the user can add a product to cart"):
        subcategory_page.add_to_cart(tc_2_data)
     with allure.step("Open cart page"):
        subcategory_page.open_cart_page()

     with allure.step("Check cart page is displayed"):
        cart_page = CartPage(browser)
        cart_page.cart_page(tc_2_data)
     with allure.step("Check the user can add products and update the order"):
        cart_page.add_products_and_update_order(tc_2_data)
     with allure.step("Check the user can remove products from the cart"):
        cart_page.cart_is_empty(tc_2_data)
