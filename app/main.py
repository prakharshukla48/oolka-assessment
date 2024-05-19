from fastapi import FastAPI
from .api import events, bookings

app = FastAPI()

app.include_router(events.router)
app.include_router(bookings.router)
