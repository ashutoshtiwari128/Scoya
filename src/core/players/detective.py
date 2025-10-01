from core.players.player import Player
from config import DETECTIVE_INITIAL_TICKETS

class Detective(Player):
    """
    Class of a detective player. The goal of detective is to catch Mr. X by making valide moves on each turn.
    """
    def __self__(self, name: str, initial_position: int):
        super().__init__(name=name, initial_position=initial_position, initial_tickets=DETECTIVE_INITIAL_TICKETS)