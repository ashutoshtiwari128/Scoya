from abc import ABC, abstractmethod
from core.transport import TransportType, Ticket, DoubleTicket
from core.board import Board
from core.exceptions import InvalidMove

class Player(ABC):
    """
    Abstract class for any player.
    """
    @abstractmethod
    def __init__(
            self,
            name: str,
            initial_position: int,
            initial_tickets: dict[TransportType, int],
            game_board: Board) -> None:

        if initial_position <= 0:
            raise ValueError(f"Position expected to be positive but recieved {initial_position} for {name}")

        self.__name: str = name
        self._position: int = initial_position
        self._tickets: dict[TransportType, int] = initial_tickets
        self._game_board: Board = game_board

    @property
    def name(self) -> str:
        return self.__name

    @property
    def position(self) -> int:
        return self._position

    @property
    def tickets(self) -> dict[str, int]:
        return self._tickets

    @abstractmethod
    def move(self, ticket: Ticket) -> None:
        pass

    def _validate_move_inputs_common(self, ticket: Ticket):
        if ticket is None:
            raise TypeError("Null ticket.")

        if ticket.destination_position <= 0:
            raise ValueError(f"Invalid destination position {ticket.destination_position}")

        if not self._game_board.is_valid_destination(self._position, ticket):
            raise InvalidMove(ticket)