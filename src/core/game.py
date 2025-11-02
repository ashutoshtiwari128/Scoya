import random

from core.board import Board
from core.players.detective import Detective
from core.players.mrx import MrX


class Game:
    # TODO: Complete logic and game interface.
    def __init__(self, detectives_name: list[str], mrx_name: str):
        # Initialize game board.
        board = Board(board_data_filePath="core//data//board.txt")

        possible_initial_positions = []
        with open("src\core\data\initial_positions.txt", 'r') as file:
            possible_initial_positions = [int(line.strip()) for line in file]

        random_positions = random.sample(possible_initial_positions, len(detectives_name) + 1)

        # Initialize detectives.
        detectives: list[Detective] = []
        for i, name in enumerate(detectives_name):
            detectives.append(Detective(name, random_positions[i], board))

        # Initialize Mr.X.
        mrx: MrX = MrX(mrx_name, random_positions[-1], board)

    def play(self):
        is_mrx_turn: bool
        game_result: int = 0
        while(True):
            if is_mrx_turn:
                pass
            else:
                pass

            game_result = self.__game_result()

            if game_result == 1 or game_result == -1:
                # Game complete.
                break

        print(f"Winner: {game_result}")

    def __game_result(self):
        '''
        Returns the state of game:
        1 : Game complete and detectives won.
        0 : Game not complete.
        -1 : Game complete and Mr. X won.
        '''
        pass