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