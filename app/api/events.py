from fastapi import APIRouter, HTTPException, Depends
from typing import List
from .. import schemas, services
from ..services import event_service
from ..schemas import event

router = APIRouter()
event_service = event_service.EventService()

@router.get("/events", response_model=List[event.Event])
def read_events():
    return event_service.get_events()

@router.post("/events", response_model=event.Event)
def create_event(event: event.EventCreate):
    return event_service.create_event(event)

@router.get("/events/{event_id}", response_model=event.Event)
def read_event(event_id: int):
    db_event = event_service.get_event(event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
