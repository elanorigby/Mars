class Report:
    """ output rover positions """
    def __init__(self, plateau, rover):
        self.plateau = plateau
        self.rover = rover
        self.errormessage = "Woops! This rover fell off the plateau. Nice driving, NASA."

    def message(self):
        if not self.ongrid():
            return self.errormessage
        else:
            return self.rover.x, self.rover.y, self.rover.facing

    def ongrid(self):
        return 0 <= self.rover.x <= self.plateau.x and 0 <= self.rover.y <= self.plateau.y

