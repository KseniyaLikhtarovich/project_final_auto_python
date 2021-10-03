from selenium.webdriver.common.by import By


class CategoriesPageLocators:

    LOCATOR_CATEGORIES = (By.XPATH, "//div[@id='box-category']/h1")

    LOCATOR_SUBCATEGORY_LINK = (By.XPATH, "//ul[@class='listing-wrapper products']/li[3]/a")
