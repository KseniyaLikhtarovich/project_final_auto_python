import requests
from time import sleep


class Petstore:

    def create_user(self, api_data):
        response_1 = requests.post(api_data["url"],
                                   json=api_data["post"])
        assert response_1.status_code == 200

    def get_user_data(self, api_data):
        get_url_1 = api_data["url"] + f"/{api_data['username_1']}"

        while True:
            response_2 = requests.get(get_url_1)
            if response_2.status_code == 404:
                sleep(1)
            else:
                break

        print(response_2.json())
        assert response_2.status_code == 200

    def change_username(self, api_data):
        get_url_1 = api_data["url"] + f"/{api_data['username_1']}"

        response_3 = requests.put(get_url_1, json=api_data["put"])
        assert response_3.status_code == 200

    def check_username(self, api_data):
        get_url_2 = api_data["url"] + f"/{api_data['username_2']}"

        while True:
            response_4 = requests.get(get_url_2)
            if response_4.status_code == 404:
                sleep(1)
            else:
                break

        print(response_4.json())
        assert response_4.status_code == 200
