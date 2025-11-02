from core.board import Board
from core.config import DETECTIVE_INITIAL_TICKETS
from core.exceptions import *
from core.players.player import Player
from core.transport import DoubleTicket, Ticket, TransportType


class Detective(Player):
    """
    Class of a detective player. The goal of detective is to catch Mr. X by making valide moves on each turn.
    """
    def __self__(self, name: str, initial_position: int, game_board: Board):
        super().__init__(
            name=name,
            initial_position=initial_position,
            game_board=game_board,
            initial_tickets=DETECTIVE_INITIAL_TICKETS)

    def move(self, ticket: Ticket) -> None:
        self.__validate_move_inputs(ticket)

        self._position = ticket.destination_position
        self._tickets[ticket.transport_type] -= 1

    def __validate_move_inputs(self, ticket: Ticket):
        if type(ticket) is DoubleTicket:
            raise TypeError(f"Detective cannot use a double ticket.")

        if ticket.transport_type == TransportType.BLACK:
            raise ValueError(f"Detective cannot use black ticket.")

        self._validate_move_inputs_common(ticket)
