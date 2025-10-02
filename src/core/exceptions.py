from core.transport import Ticket


class InvalidMove(Exception):
    def __init__(self, message, ticket: Ticket):
        super().__init__(message)
        self.ticket: Ticket = ticket

    def __str__(self):
        return f"{super().__str__()} [There is no possible path to destination with this ticket: {self.ticket}]"

class InsufficientTickets(Exception):
    def __init__(self, message, ticket: Ticket):
        super().__init__(message)
        self.ticket: Ticket = ticket

    def __str__(self):
        return f"{super().__str__()} [Ticket: {self.ticket}]"

class InsufficientDoubleTickets(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"{super().__str__()} There are no more double ticket left."
