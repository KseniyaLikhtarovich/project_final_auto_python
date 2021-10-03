from selenium.webdriver.common.by import By


class EditAccountPageLocators:

    LOCATOR_EDIT_ACCOUNT = (By.XPATH, "//div[@id='edit-account']/h1")

    LOCATOR_FIRSTNAME = (By.NAME, "firstname")
    LOCATOR_SAVE_BUTTON = (By.NAME, "save")
    LOCATOR_CHANGE_NAME = (By.CSS_SELECTOR, "#notices > div")
