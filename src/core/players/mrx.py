from core.config import INITIAL_NUMBER_OF_2X_TICKETS, MRX_INITIAL_TICKETS
from core.exceptions import *
from core.players.player import Player
from core.transport import DoubleTicket, Ticket


class MrX(Player):
    """
    Class of the Mr. X player. The goal of Mr. X is to evade the detectives by making valide moves until the end of
    the game.
    """
    def __self__(self, name: str, initial_position: int):
        super().__init__(name=name, initial_position=initial_position, initial_tickets=MRX_INITIAL_TICKETS)

        self.__number_of_2x_tickets = INITIAL_NUMBER_OF_2X_TICKETS

    @property
    def number_of_2x_tickets(self):
        return self.__number_of_2x_tickets

    def move(self, ticket: Ticket) -> None:
        self.__validate_move_inputs(ticket)

        self._position = ticket.destination_position
        self._tickets[ticket.transport_type] -= 1
        if type(ticket) is DoubleTicket:
            self.__number_of_2x_tickets -= 1

    def __validate_move_inputs(self, ticket: Ticket):
        if self.tickets[ticket.transport_type] <= 0:
            raise InsufficientTickets(ticket)
        if type(ticket) is DoubleTicket and self.__number_of_2x_tickets <= 0:
            raise InsufficientDoubleTickets

        self._validate_move_inputs_common(ticket)
