from core.transport import TransportType, Ticket, DoubleTicket
from typing import List

class Board:
    def __init__(self, transport_adjacency: dict[TransportType, List[List[int]]]):
        self.__transport_adjacency: dict[TransportType, List[List[int]]] = transport_adjacency

    @property
    def transport_adjacency(self):
        return self.__transport_adjacency

    def get_possible_destinations(self, current_position: int, ticket: Ticket) -> List[int]:
        if type(ticket) is DoubleTicket:
            possible_destinations = []
            for first_stop in self.__get_neighbours(current_position, ticket):
                possible_destinations.extend(self.__get_neighbours(first_stop, ticket))
            return possible_destinations
        else:
            return self.__get_neighbours(current_position, ticket)

    def is_valid_destination(self, current_position: int, ticket: Ticket) -> bool:
        possible_destinations = self.get_possible_destinations(current_position, ticket)
        return ticket.destination_position in possible_destinations

    def __get_neighbours(self, current_position: int, ticket: Ticket) -> List[int]:
        return self.__transport_adjacency[ticket.transport_type][current_position]
