import pytest

BASE_URL = "http://localhost:8080"

def test_01_view_flights(authenticated_session):
    """Verify flight listings page."""
    response = authenticated_session.get(f"{BASE_URL}/flights")
    assert response.status_code == 200

def test_02_add_to_cart(authenticated_session):
    """Verify seat addition to cart."""
    payload = {
        "airline": "Air France",
        "seatNumber": "F1"
    }
    response = authenticated_session.post(f"{BASE_URL}/flights", data=payload)
    assert response.status_code in [200, 201, 302]

def test_03_verify_cart_contents(authenticated_session):
    """Verify cart page loaded successfully."""
    response = authenticated_session.get(f"{BASE_URL}/cart")
    assert response.status_code == 200
    
    # Check page rendering structure:
    assert "<!DOCTYPE html>" in response.text
    assert "My Trip Cart" in response.text

def test_04_checkout(authenticated_session):
    """Verify final booking checkout."""
    payload = {"paymentMethod": "Credit Card", "confirm": "true"}
    response = authenticated_session.post(f"{BASE_URL}/checkout", data=payload)
    assert response.status_code in [200, 201, 302]