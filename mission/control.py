from . import rover
from . import plateau

class Control:
    def __init__(self, file):
        self.mission = self.opener(file)
        self.checker()
        self.grid, self.mission = self.firstline()
        self.rovlist = []

    @staticmethod
    def opener(file):
        with open(file) as f:
            mission = f.read().splitlines()
            return mission

    def checker(self):
        for string in self.mission:
            for char in string:
                if char not in 'NSWERLM 0123456789':
                    raise ValueError('{} is not valid input'.format(char))

    def firstline(self):
        grid = self.mission.pop(0)
        return grid, self.mission

    def makeplateau(self):
        return plateau.Plateau(self.grid)

    def makerovers(self):
        while self.mission:
            start, moves = self.mission[:2]
            self.rovlist.append(rover.Rover(start, moves))
            del self.mission[:2]
        return self.rovlist
