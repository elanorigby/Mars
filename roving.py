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
    x, y, facing = start.split()
    x, y = int(x), int(y)
    return x, y, facing


def turnL(facing):
    if facing == 'N':
        return 'W'
    if facing == 'W':
        return 'S'
    if facing == 'S':
        return 'E'
    if facing == 'E':
        return 'N'


def turnR(facing):
    if facing == 'N':
        return 'E'
    if facing == 'E':
        return 'S'
    if facing == 'S':
        return 'W'
    if facing == 'W':
        return 'N'

def turn(facing, turn):
    if facing not in 'NSEW':
        raise ValueError('{} is not a valid facing'.format(facing))
    if turn == 'L':
        return turnL(facing)
    if turn == 'R':
        return turnR(facing)


def goN(y):
    return y + 1


def goS(y):
    return y - 1


def goE(x):
    return x + 1


def goW(x):
    return x - 1


def go(x, y, facing):
    if facing not in 'NSEW':
        raise ValueError('{} is not a valid facing'.format(facing))
    if facing == 'N':
        return x, goN(y)
    if facing == 'S':
        return x, goS(y)
    if facing == 'W':
        return goW(x), y
    if facing == 'E':
        return goE(x), y

