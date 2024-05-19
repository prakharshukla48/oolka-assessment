class Event:
    def __init__(self, id: int, name: str, date: str, location: str, total_tickets: int,
                 available_tickets: int, price_per_ticket: float):
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.total_tickets = total_tickets
        self.available_tickets = available_tickets
        self.price_per_ticket = price_per_ticket
