import unittest
from unittest.mock import MagicMock
from app.services import booking_service, event_service
from app.schemas.booking import BookingCreate

class TestBookingService(unittest.TestCase):
    def setUp(self):
        self.events = [
            event_service.Event(id=1, available_tickets=10, price_per_ticket=100,
                                location="Location A", name="test1", date="2024-05-24",total_tickets=10),
            event_service.Event(id=2, available_tickets=5, price_per_ticket=200,
                                location="Location B", name="test2", date="2024-05-25",total_tickets=5)
        ]
        self.booking_service = booking_service.BookingService(self.events)

    def test_book_tickets_success(self):
        booking_data = BookingCreate(event_id=1, number_of_tickets=5, user_id=1)
        booking = self.booking_service.book_tickets(booking_data)
        self.assertIsNotNone(booking)
        self.assertEqual(booking.total_price, 500)
        self.assertEqual(len(self.booking_service.bookings), 1)

    def test_book_tickets_failure_invalid_event(self):
        booking_data = BookingCreate(event_id=3, number_of_tickets=5, user_id=2)  # Event with ID 3 doesn't exist
        booking = self.booking_service.book_tickets(booking_data)
        self.assertIsNone(booking)
        self.assertEqual(len(self.booking_service.bookings), 0)

    def test_book_tickets_failure_insufficient_tickets(self):
        booking_data = BookingCreate(event_id=2, number_of_tickets=10, user_id=3)  # Only 5 tickets available
        booking = self.booking_service.book_tickets(booking_data)
        self.assertIsNone(booking)
        self.assertEqual(len(self.booking_service.bookings), 0)
