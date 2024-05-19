import unittest
from unittest.mock import MagicMock
from app.services.event_service import EventService
from app.schemas.event import EventCreate

class TestEventService(unittest.TestCase):
    def setUp(self):
        self.event_service = EventService()

    def test_create_event(self):
        event_data = EventCreate(name="Event 1", date="2024-05-20", available_tickets=100,
                                 price_per_ticket=50, location="Location A", total_tickets=100)
        event = self.event_service.create_event(event_data)
        self.assertIsNotNone(event)
        self.assertEqual(event.id, 1)
        self.assertEqual(len(self.event_service.events), 1)

    def test_get_event_success(self):
        event_data = EventCreate(name="Event 1", date="2024-05-20", available_tickets=100,
                                 price_per_ticket=50, location="Location A", total_tickets=100)
        self.event_service.create_event(event_data)
        event = self.event_service.get_event(1)
        self.assertIsNotNone(event)
        self.assertEqual(event.id, 1)

    def test_get_event_failure(self):
        event = self.event_service.get_event(1)
        self.assertIsNone(event)
