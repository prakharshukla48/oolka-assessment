from fastapi import APIRouter, HTTPException, Depends
from .. import schemas, services
from ..services import  booking_service
from ..api.events import event_service
from ..schemas import booking

router = APIRouter()
booking_service = booking_service.BookingService(event_service.get_events())

@router.post("/events/{event_id}/book", response_model=booking.Booking)
def book_tickets(event_id: int, booking: booking.BookingCreate):
    db_booking = booking_service.book_tickets(booking)
    if db_booking is None:
        raise HTTPException(status_code=400, detail="Not enough tickets available")
    return db_booking
