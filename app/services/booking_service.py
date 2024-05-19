from typing import Optional
from ..models.booking import Booking
from ..models.event import Event
from ..schemas.booking import BookingCreate
from ..services import location_service

class BookingService:
    def __init__(self, events):
        self.bookings = []
        self.events = events
        self.counter = 0

    def book_tickets(self, booking: BookingCreate) -> Optional[Booking]:
        print(f"events, {self.events}")
        event = next((e for e in self.events if e.id == booking.event_id), None)
        if not event or event.available_tickets < booking.number_of_tickets:
            print("It came here before failing")
            return None

        total_price = event.price_per_ticket * booking.number_of_tickets
        event_location = location_service.LocationService().get_location(event.location)
        self.counter += 1
        new_booking = Booking(id=self.counter, total_price=total_price, location = event_location **booking.model_dump())
        event.available_tickets -= booking.number_of_tickets
        self.bookings.append(new_booking)
        return new_booking, event_location
