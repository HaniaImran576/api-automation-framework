import os
import json
import pytest
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_DATA_PATH = os.path.join(BASE_DIR, 'data', 'auth_data.json')

def load_test_data():
    with open(JSON_DATA_PATH, 'r') as file:
        return json.load(file)

@pytest.mark.parametrize("user", load_test_data())
def test_data_driven_login(user):
    url = "https://httpbin.org/post"
    payload = {
        "username": user.get("username"),
        "password": user.get("password")
    }
    
    response = requests.post(url, json=payload)
    
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["json"]["username"] == user.get("username")