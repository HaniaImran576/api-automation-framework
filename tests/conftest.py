import pytest
import requests

BASE_URL = "http://localhost:8080"

@pytest.fixture(scope="session")
def api_session():
    """Shared HTTP Session for managing cookies across requests."""
    session = requests.Session()
    session.headers.update({"User-Agent": "Pytest-Automation"})
    yield session
    session.close()

@pytest.fixture(scope="session")
def authenticated_session(api_session):
    """Executes SignUp and Login once before tests run."""
    # 1. SignUp
    signup_payload = {"email": "testuser@example.com", "password": "Password123"}
    api_session.post(f"{BASE_URL}/signup", data=signup_payload)

    # 2. Login
    login_payload = {"email": "testuser@example.com", "password": "Password123"}
    api_session.post(f"{BASE_URL}/login", data=login_payload)
    
    return api_session