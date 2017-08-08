def opener(file):
        with open(file) as f:
            mission = f.read().splitlines()
            return mission

def firstline(mission):
    grid = mission.pop(0)
    return (grid, mission)
