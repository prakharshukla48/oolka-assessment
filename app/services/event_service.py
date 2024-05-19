from typing import List, Optional
from ..models.event import Event
from ..schemas.event import EventCreate

class EventService:
    def __init__(self):
        self.events = []
        self.counter = 0

    def get_events(self) -> List[Event]:
        return self.events

    def get_event(self, event_id: int) -> Optional[Event]:
        return next((event for event in self.events if event.id == event_id), None)

    def create_event(self, event: EventCreate) -> Event:
        self.counter += 1
        new_event = Event(id=self.counter, **event.model_dump())
        self.events.append(new_event)
        return new_event

    def __repr__(self):
        print (f"Object for Event Service, There are total {len(self.events)} events")
