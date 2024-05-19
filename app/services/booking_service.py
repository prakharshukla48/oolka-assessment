from typing import Optional
from ..models.booking import Booking
from ..models.event import Event
from ..schemas.booking import BookingCreate
from ..services import location_service
from ..services import payment_service

class BookingService:
    def __init__(self, events):
        self.bookings = []
        self.events = events
        self.counter = 0

    def book_tickets(self, booking: BookingCreate) -> Optional[Booking]:
        print(f"events, {self.events}")

        event = next((e for e in self.events if e.id == booking.event_id), None)
        if not event or event.available_tickets < booking.number_of_tickets:
            print("Failing due to no event or tickets not available")
            return None

        total_price = event.price_per_ticket * booking.number_of_tickets
        # location_service  can be integrated here, assuming integration working as expected
        # event_location = location_service.LocationService().get_location(event.location)
        self.counter += 1
        new_booking = Booking(id=self.counter, total_price=total_price, **booking.model_dump())
        # payment service can be implemented here. for now we are assuming it is working as expected
        event.available_tickets -= booking.number_of_tickets
        self.bookings.append(new_booking)
        return new_booking

    def __repr__(self):
        print(f" This is Booking service class, there are {len(self.bookings)} bookings ")

