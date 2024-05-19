class Booking:
    def __init__(self, id: int, event_id: int, user_id: int, number_of_tickets: int, total_price: float, location: str):
        self.id = id
        self.event_id = event_id
        self.user_id = user_id
        self.number_of_tickets = number_of_tickets
        self.total_price = total_price
        self.location = location