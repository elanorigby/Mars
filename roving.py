def opener(file):
        with open(file) as f:
            mission = f.read().splitlines()
            return mission


def firstline(mission):
    grid = mission.pop(0)
    return (grid, mission)


def rovers(mission):
    start, moves = mission[:2]
    del mission[:2]
    return start, moves, mission


def starter(start):
    x, y, direction = start.split()
    return x, y, direction


def turnL(direction):
    if direction == 'N':
        return 'W'
    if direction == 'W':
        return 'S'
    if direction == 'S':
        return 'E'
    if direction == 'E':
        return 'N'


def turnR(direction):
    if direction == 'N':
        return 'E'
    if direction == 'E':
        return 'S'
    if direction == 'S':
        return 'W'
    if direction == 'W':
        return 'N'

def turn(direction, turn):
    if direction not in 'NSEW':
        raise ValueError('{} is not a valid direction'.format(direction))
    if turn == 'L':
        return turnL(direction)
    if turn == 'R':
        return turnR(direction)


def moveN(startY):
    return startY + 1


def moveS(startY):
    return startY - 1


def moveW(startX):
    return startX - 1