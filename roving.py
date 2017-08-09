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


    def goN(self):
        return self.y + 1


    def goS(self):
        return self.y - 1


    def goE(self):
        return self.x + 1


    def goW(self):
        return self.x - 1


    def go(self):
        """ returns adjusted x, y, & facing"""
        if self.facing == 'N':
            return self.x, self.goN(), self.facing
        if self.facing == 'S':
            return self.x, self.goS(), self.facing
        if self.facing == 'W':
            return self.goW(), self.y, self.facing
        if self.facing == 'E':
            return self.goE(), self.y, self.facing


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

