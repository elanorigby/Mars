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
        if move in 'RL':
            return self.x, self.y, self.turn(move)
        if move == 'M':
            return self.go()

    def makeitso(self):
        for move in self.moves:
            self.x, self.y, self.facing = self.drive(move)
