from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_book_tickets():
    event_response = client.post("/events", json={
        "name": "Test Event",
        "date": "2023-01-01",
        "location": "Test Location",
        "total_tickets": 100,
        "available_tickets": 100,
        "price_per_ticket": 50.0
    })
    event_id = event_response.json()["id"]

    booking_response = client.post(f"/events/{event_id}/book", json={
        "event_id": event_id,
        "user_id": 1,
        "number_of_tickets": 2
    })
    assert booking_response.status_code == 200
    assert booking_response.json()["total_price"] == 100.0
