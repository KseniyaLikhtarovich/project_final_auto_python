from pages.main_page import MainPage
from pages.edit_account_page import EditAccountPage
from db.steps_litecart_db import changes_in_db
import allure


@allure.feature("Check the user can login and edit the account")
def test_login_and_edit_account(browser, tc_1_data, cursor):
    with allure.step("Open main page"):
        main_page = MainPage(browser)
        main_page.open_main_page()
    with allure.step("Check the user can login"):
        main_page.login(tc_1_data)
    with allure.step("Open edit account page"):
        main_page.open_edit_account_page()

    with allure.step("Check edit account page is displayed"):
        account_page = EditAccountPage(browser)
        account_page.edit_account_page(tc_1_data)
    with allure.step("Check the user can change name"):
        account_page.change_username(tc_1_data)

    with allure.step("Check the username was changed"):
        changes_in_db(cursor, tc_1_data)
