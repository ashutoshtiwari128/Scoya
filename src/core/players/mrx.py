from player import Player
from config import MRX_INITIAL_TICKETS, NUMBER_OF_2X_TICKETS
from transport_type import TransportType

class MrX(Player):
    """
    Class of the Mr. X player. The goal of Mr. X is to evade the detectives until the end of the game.
    """
    def __self__(self, name: str, initial_position: int):
        super().__init__(name=name, initial_position=initial_position, initial_tickets=MRX_INITIAL_TICKETS)

        self.number_of_2x_tickets = NUMBER_OF_2X_TICKETS

    def move(self, next_position: int, transport_type: TransportType, is_2x_move: bool) -> None:
        if is_2x_move:
            self.__validate_2x_move(next_position, transport_type)
            # TODO: Add logic to update position and tickets.
            pass
        else:
            super().move(next_position, transport_type)

    # Private methods
    def __validate_2x_move(self, next_position: int, transport_type: TransportType) -> None:
        # TODO: Add validation logic.
        pass