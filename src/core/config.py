from .transport import TransportType

MAXIMUM_MOVES = 22

INITIAL_NUMBER_OF_2X_TICKETS = 2

DETECTIVE_INITIAL_TICKETS: dict[TransportType, int] = {
    TransportType.TAXI: 10,
    TransportType.BUS: 8,
    TransportType.UNDERGROUND: 4
}

MRX_INITIAL_TICKETS: dict[TransportType, int] = {
    TransportType.BLACK: 5,
    TransportType.TAXI: MAXIMUM_MOVES,
    TransportType.BUS: MAXIMUM_MOVES,
    TransportType.UNDERGROUND: MAXIMUM_MOVES
}
