from selenium.webdriver.common.by import By


class MainPageLocators:

    LOCATOR_EMAIL = (By.NAME, "email")
    LOCATOR_PASSWORD = (By.NAME, "password")
    LOCATOR_LOGIN_BUTTON = (By.NAME, "login")
    LOCATOR_ACCOUNT = (By.XPATH, "//div[@id='box-account']/h3")

    LOCATOR_EDIT_ACCOUNT_BUTTON = (By.XPATH, "//div[@id='box-account']//li[3]/a")

    LOCATOR_CATEGORIES_BUTTON = (By.XPATH, "//div[@id='box-category-tree']//li/a")
