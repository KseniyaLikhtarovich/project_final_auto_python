from selenium import webdriver
import pytest
import mysql.connector as mysql


# Драйвер
@pytest.fixture(scope="module")
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# База данных
@pytest.fixture()
def db():
    db = mysql.connect(host="127.0.0.1",
                       user="root",
                       passwd="",
                       database="litecart")
    yield db
    db.close()


@pytest.fixture()
def cursor(db):
    cursor = db.cursor()
    yield cursor
    db.rollback()


# Данные
@pytest.fixture()
def tc_1_data():
    tc_1_data = {
        "input": {
            "email": "test@test.com",
            "password": "pwd1user",
            "name": "Casey3"
        },
        "output": {
            "account": "Account",
            "edit_account": "Edit Account",
            "changes": "Changes saved successfully."
        }
    }
    return tc_1_data


@pytest.fixture()
def tc_2_data():
    tc_2_data = {
        "input": {
            "quantity": "3"
        },
        "output": {
            "categories": "Rubber Ducks",
            "duck": "Green Duck",
            "product": "1",
            "order": "Order Summary",
            "order_quantity": "3",
            "payment_due": "$60.00",
            "empty_cart_msg": "There are no items in your cart."
        }
    }
    return tc_2_data


@pytest.fixture(scope="class")
def api_data():
    api_data = {
        "url": "https://petstore.swagger.io/v2/user",
        "post": {
            "id": 1000,
            "username": "Casey_Li",
            "firstName": "Casey",
            "lastName": "Li",
            "email": "test@test.com",
            "password": "test123",
            "phone": "+375332343565",
            "userStatus": 0
        },
        "username_1": "Casey_Li",
        "put": {
            "id": 1000,
            "username": "Casey_Li123",
            "firstName": "Casey",
            "lastName": "Li",
            "email": "test@test.com",
            "password": "test123",
            "phone": "+375332343565",
            "userStatus": 0
        },
        "username_2": "Casey_Li123"
    }
    return api_data
