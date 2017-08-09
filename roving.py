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

class Rover:
    def __init__(self, start, moves):
        self.start = start
        self.moves = moves
        self.x, self.y, self.facing = self.starter()

    def starter(self):
        x, y, facing = self.start.split()
        x, y = int(x), int(y)
        return x, y, facing

    def turnL(self):
        if self.facing == 'N':
            return 'W'
        if self.facing == 'W':
            return 'S'
        if self.facing == 'S':
            return 'E'
        if self.facing == 'E':
            return 'N'

    def turnR(self):
        if self.facing == 'N':
            return 'E'
        if self.facing == 'E':
            return 'S'
        if self.facing == 'S':
            return 'W'
        if self.facing == 'W':
            return 'N'

    def turn(self, turn):
        """ returns new facing direction"""
        if turn == 'L':
            return self.turnL()
        if turn == 'R':
            return self.turnR()


def goN(y):
    return y + 1


def goS(y):
    return y - 1


def goE(x):
    return x + 1


def goW(x):
    return x - 1


def go(x, y, facing):
    """ returns adjusted x, y, & facing"""
    if facing == 'N':
        return x, goN(y), facing
    if facing == 'S':
        return x, goS(y), facing
    if facing == 'W':
        return goW(x), y, facing
    if facing == 'E':
        return goE(x), y, facing


def drive(x, y, facing, move):
    """ returns x, y, facing"""
    if facing not in 'NSEW':
        raise ValueError('{} is not a valid facing'.format(facing))

    if move not in 'RLM':
        raise ValueError('{} is not a legit move'.format(move))

    if move in 'RL':
        return x, y, turn(facing, move)

    if move == 'M':
        return go(x, y, facing)


def ongrid(roverx, rovery, gridx, gridy):
    return 0 <= roverx <= gridx and 0 <= rovery <= gridy

