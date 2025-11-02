from typing import List

from core.transport import DoubleTicket, Ticket, TransportType


class Board:
    def __init__(self, board_data_filePath):
        """
        For black transport type, only the paths of boat are mapped. Whereas in ticket transport type black is
        interpreted to be unknown type including boat.
        """
        self.__transport_adjacency: dict[TransportType, List[List[int]]] = \
            self.__create_transport_adjacency_lists(board_data_filePath)

    @property
    def transport_adjacency(self):
        return self.__transport_adjacency

    def is_valid_destination(self, current_position: int, ticket: Ticket) -> bool:
        possible_destinations = self.get_possible_destinations(current_position, ticket)
        return ticket.destination_position in possible_destinations

    def get_possible_destinations(self, current_position: int, ticket: Ticket) -> List[int]:
        #TODO: For black ticket take union of all other transport type as well.
        if type(ticket) is DoubleTicket:
            possible_destinations = []
            for first_stop in self.__get_neighbours(current_position, ticket.transport_type):
                # TODO: Fix: appending to list will lead to duplication.
                possible_destinations.extend(self.__get_neighbours(first_stop, ticket.transport_type))
            return possible_destinations
        else:
            return self.__get_neighbours(current_position, ticket.transport_type)

    def __get_neighbours(self, current_position: int, transport_type: TransportType) -> List[int]:
        return self.__transport_adjacency[transport_type][current_position]

    def __create_transport_adjacency_lists(self, fileName: str) -> dict[TransportType, List[List[int]]]:
        transport_adjacency: dict[TransportType, List[List[int]]] = {}
        # Inilialize list to max number of lines.
        with open(fileName, 'r') as file:
            num_lines = sum(1 for _ in file)
            for t in TransportType:
                # TODO: Ideally should be +1. Temporary +2 because board data has 1 line less than the max node number.
                transport_adjacency[t] = [[] for _ in range(num_lines + 2)]

        # Read each line and fill data.
        with open(fileName, 'r') as file:
            for line in file:
                node_transport_list = [m.strip() for m in line.split("|")]
                node = int(node_transport_list[0])

                if len(node_transport_list) > 1 and node_transport_list[1] != '':
                    transport_adjacency[TransportType.TAXI][node] = \
                        [int(n.strip()) for n in node_transport_list[1].split(' ')]

                if len(node_transport_list) > 2 and node_transport_list[2] != '':
                    transport_adjacency[TransportType.BUS][node] = \
                        [int(n.strip()) for n in node_transport_list[2].split(' ')]

                if len(node_transport_list) > 3 and node_transport_list[3] != '':
                    transport_adjacency[TransportType.UNDERGROUND][node] = \
                        [int(n.strip()) for n in node_transport_list[3].split(' ')]

                if len(node_transport_list) > 4 and node_transport_list[4] != '':
                    transport_adjacency[TransportType.BLACK][node] = \
                        [int(n.strip()) for n in node_transport_list[4].split(' ')]

                if len(node_transport_list) <= 1 or len(node_transport_list) > 5:
                    raise ValueError(f"Unexpected data in the file {fileName} and line [{line}]. " +
                        "Cannot create adjacency list.")

        return transport_adjacency
