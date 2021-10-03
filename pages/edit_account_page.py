from pages.base_page import BasePage
from locators.edit_account_page_locators import EditAccountPageLocators


class EditAccountPage(BasePage):

    def edit_account_page(self, tc_1_data):
        account_page = self.find_element(EditAccountPageLocators.LOCATOR_EDIT_ACCOUNT)
        print(account_page.text)
        assert account_page.text == tc_1_data["output"]["edit_account"]

    def change_username(self, tc_1_data):
        name_locator = self.find_element(EditAccountPageLocators.LOCATOR_FIRSTNAME)
        name_locator.clear()
        name_locator.send_keys(tc_1_data["input"]["name"])

        save_changes = self.find_element(EditAccountPageLocators.LOCATOR_SAVE_BUTTON)
        save_changes.click()

        new_username = self.find_element(EditAccountPageLocators.LOCATOR_CHANGE_NAME)
        print(new_username.text)
        assert new_username.text == tc_1_data["output"]["changes"]
