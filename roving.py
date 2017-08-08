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

