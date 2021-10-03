from petstore_api.steps_petstore_api import Petstore
import allure


@allure.feature("Check GET, POST, PUT user data")
def test_api_petstore(api_data):
    with allure.step("Check user can be created"):
        api = Petstore()
        api.create_user(api_data)
    with allure.step("Get the user data"):
        api.get_user_data(api_data)
    with allure.step("Change the username"):
        api.change_username(api_data)
    with allure.step("Check the username was changed"):
        api.check_username(api_data)
