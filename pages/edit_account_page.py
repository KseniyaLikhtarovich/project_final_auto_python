from pages.base_page import BasePage
from locators.edit_account_page_locators import EditAccountPageLocators


class EditAccountPage(BasePage):

    def edit_account_page(self, test_case_1_data):
        account_page = self.find_element(EditAccountPageLocators.LOCATOR_EDIT_ACCOUNT)
        assert account_page.text == test_case_1_data["output"]["edit_account"]

    def change_username(self, test_case_1_data):
        name_locator = self.find_element(EditAccountPageLocators.LOCATOR_FIRSTNAME)
        name_locator.clear()
        name_locator.send_keys(test_case_1_data["input"]["name"])

        save_changes = self.find_element(EditAccountPageLocators.LOCATOR_SAVE_BUTTON)
        save_changes.click()

        new_username = self.find_element(EditAccountPageLocators.LOCATOR_CHANGE_NAME)
        assert new_username.text == test_case_1_data["output"]["changes"]
