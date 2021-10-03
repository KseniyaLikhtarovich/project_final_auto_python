from selenium.webdriver.common.by import By


class SubcategoryPageLocators:

    LOCATOR_SUBCATEGORY = (By.XPATH, "//div[@id='box-product']/div/h1")

    LOCATOR_ADD_TO_CART_BUTTON = (By.NAME, "add_cart_product")
    LOCATOR_PRODUCT_ADDED = (By.XPATH, "//div[@id='cart']/a[2]/span")

    LOCATOR_CART_BUTTON = (By.XPATH, "//div[@id='cart']/a[3]")
