class Control:
    def __init__(self, file):
        self.mission = self.opener(file)
        self.grid, self.mission = self.firstline()

    def opener(self, file):
            with open(file) as f:
                mission = f.read().splitlines()
                return mission

    def firstline(self):
        grid = self.mission.pop(0)
        return grid, self.mission

    def makegrid(self):
        return Plateau(self.grid)

    def makerovers(self):
        self.rovlist = []
        while self.mission:
            start, moves = self.mission[:2]
            self.rovlist.append(Rover(start, moves))
            del self.mission[:2]
        print(self.rovlist)
        return self.rovlist


class Plateau:
    def __init__(self, grid):
        self.x, self.x = grid.split()


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


    def drive(self, move):
        """ returns x, y, facing"""
        if self.facing not in 'NSEW':
            raise ValueError('{} is not a valid direction to face'.format(self.facing))
        if move not in 'RLM':
            raise ValueError('{} is not a legit move'.format(move))

        if move in 'RL':
            return self.x, self.y, self.turn(move)
        if move == 'M':
            return self.go()



def ongrid(roverx, rovery, gridx, gridy):
    return 0 <= roverx <= gridx and 0 <= rovery <= gridy
