from enum import Enum


class TransportType(Enum):
    """
    Enumeration of all the transport types.
    """
    TAXI = "Taxi"
    BUS = "Bus"
    UNDERGROUND = "Underground"
    BLACK = "Black"

class Ticket:
    """
    Class of a ticket for moving to destination position using the transport type.
    """
    def __init__(self, destination_position: int, transport_type: TransportType):
        if destination_position <= 0:
            raise ValueError(f"Destination position expected to be positive but recieved {destination_position}.")

        self.__transport_type: TransportType = transport_type
        self.__destination_position: int = destination_position

    @property
    def transport_type(self):
        return self.__transport_type

    @property
    def destination_position(self):
        return self.__destination_position

    def __str__(self):
        return (
            f"Ticket type: {type(self).__name__}, destination position: {self.destination_position}, "
            f"transport type: {self.transport_type}.")

class DoubleTicket(Ticket):
    """
    Class of a special ticket which allows to move 2 stops of the transport type to reach the destination position.
    """
    def __init__(self, destination_position, transport_type):
        super().__init__(destination_position, transport_type)
        pass
