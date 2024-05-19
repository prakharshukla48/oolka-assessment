from pydantic import BaseModel

class BookingBase(BaseModel):
    event_id: int
    user_id: int
    number_of_tickets: int

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    total_price: float

    class Config:
        orm_mode = True
