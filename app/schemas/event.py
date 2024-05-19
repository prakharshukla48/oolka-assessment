from pydantic import BaseModel
from typing import Optional

class EventBase(BaseModel):
    name: str
    date: str
    location: str
    total_tickets: int
    available_tickets: int
    price_per_ticket: float

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
