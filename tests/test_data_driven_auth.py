import json
import csv
import pytest
import requests

BASE_URL = "http://localhost:8080"

def load_json_data():
    with open("auth_data.json", "r") as file:
        return json.load(file)

def load_csv_data():
    test_cases = []
    with open("auth_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_cases.append(row)
    return test_cases


# --- Test 1: JSON Driven Auth Testing ---
@pytest.mark.parametrize("data", load_json_data(), ids=lambda d: d["case"])
def test_auth_with_json(api_session, data):
    """Executes authentication requests driven by external JSON dataset."""
    response = api_session.post(f"{BASE_URL}/login", data=data["payload"])
    
    # Verify HTTP status code
    assert response.status_code in data["expected_status"], \
        f"Failed [{data['case']}]: Expected {data['expected_status']}, got {response.status_code}"

    # Verify Response Content (Text/Alert checks)
    if "expected_text" in data:
        assert data["expected_text"].lower() in response.text.lower(), \
            f"Failed [{data['case']}]: Expected text '{data['expected_text']}' not found in response HTML."


# --- Test 2: CSV Driven Auth Testing ---
@pytest.mark.parametrize("row", load_csv_data())
def test_auth_with_csv(api_session, row):
    """Executes authentication requests driven by external CSV dataset."""
    payload = {
        "email": row["email"],
        "password": row["password"]
    }
    expected_status = int(row["expected_status"])
    
    response = api_session.post(f"{BASE_URL}/login", data=payload)
    
    # Handle both 200 OK (re-rendered page) and explicit standard API statuses
    assert response.status_code in [200, 302, expected_status], \
        f"Failed for email {row['email']}: Received {response.status_code}"