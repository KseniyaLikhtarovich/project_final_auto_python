from selenium.webdriver.common.by import By


class CartPageLocators:

    LOCATOR_CART = (By.XPATH, "//div[@id='box-checkout-summary']/h2")

    LOCATOR_QUANTITY = (By.NAME, "quantity")
    LOCATOR_UPDATE_BUTTON = (By.NAME, "update_cart_item")
    LOCATOR_UPDATE_QUANTITY = (By.XPATH, "//table[@class='dataTable rounded-corners']/tbody/tr[2]/td")
    LOCATOR_UPDATE_PAYMENT_DUE = (By.XPATH,"//table[@class='dataTable rounded-corners']/tbody/tr[6]/td[2]")

    LOCATOR_REMOVE_BUTTON = (By.NAME, "remove_cart_item")
    LOCATOR_EMPTY_CART = (By.XPATH, "//div[@id='checkout-cart-wrapper']/p/em")
