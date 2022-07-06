import json
import jsonpath
import pytest
import config
import requests

url = "https://api.platform.intelinair.dev/admin/api/login"
file = open("config.json", "r")
json_input = file.read()
request_json = json.loads(json_input)

class Test_login:

    def test_successfully_login(self):

        valid_date = request_json["valid_login"]
        response = requests.post(url, json=valid_date)
        response.close()


        print(response)
        assert response.status_code == 200

    def test_invalid_wrong_email(self):

        invalid_date = request_json["wrong_username"]
        response = requests.post(url, json=invalid_date)
        response.close()

        print(response)
        assert response.status_code == 401

    def test_invalid_wrong_password(self):

        invalid_pass = request_json["wrong_password"]
        response = requests.post(url, json = invalid_pass)
        response.close()

        print(response)
        assert response.status_code == 401

    def test_empty_email(self):

        empty_username = request_json["empty_username"]
        response = requests.post(url, json = empty_username)
        response.close()

        print(response)
        assert response.status_code == 400

    def test_empty_password(self):

        empty_pass = request_json["empty_password"]
        response = requests.post(url, json = empty_pass)
        response.close()

        print(response)
        assert response.status_code == 400





