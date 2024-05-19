import unittest
from app.services.event_service import EventService
from app.services.booking_service import BookingService
from app.schemas.event import EventCreate
from app.schemas.booking import BookingCreate

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Set up EventService and BookingService instances
        self.event_service = EventService()
        self.booking_service = BookingService(self.event_service.events)

    def test_create_event_and_book_tickets(self):
        # Create an event
        event_data = EventCreate(name="Test Event", date="2024-05-20", available_tickets=100,
                                 price_per_ticket=50, location="Test Location", total_tickets=100)
        event = self.event_service.create_event(event_data)

        # Book tickets for the created event
        booking_data = BookingCreate(event_id=event.id, user_id=1, number_of_tickets=5)
        booking = self.booking_service.book_tickets(booking_data)

        # Assertions
        self.assertIsNotNone(event)
        self.assertIsNotNone(booking)
        self.assertEqual(len(self.event_service.events), 1)
        self.assertEqual(len(self.booking_service.bookings), 1)
        self.assertEqual(booking.event_id, event.id)

if __name__ == '__main__':
    unittest.main()
