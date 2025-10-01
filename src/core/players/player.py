from abc import ABC
from core.transport import TransportType

class Player(ABC):
    """
    Abstract class for any player.
    """
    # TODO: Take game board as input for making moves
    def __init__(self, name: str, initial_position: int, initial_tickets: dict[TransportType, int]) -> None:
        if initial_position <= 0:
            raise ValueError(f"Position expected to be positive but recieved {initial_position} for {name}")

        self.__name: str = name
        self._position: int = initial_position
        
        # Mapping of TransportType to the remaining tickets for that transport
        self._tickets: dict[TransportType, int] = initial_tickets

    @property
    def name(self) -> str:
        return self.__name

    @property
    def position(self) -> int:
        return self._position
    
    @property
    def tickets(self) -> dict[str, int]:
        return self._tickets
    
    def move(self, next_position: int, transport_type: TransportType) -> None:
        self.__validate_move(next_position, transport_type)
        # TODO: Add logic to update position and tickets.

    # Private methods
    def __validate_move(self, next_position: int, transport_type: TransportType) -> None:
        # TODO: Add validation logic.
        pass