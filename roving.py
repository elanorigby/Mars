def opener(file):
        with open(file) as f:
            misson = f.readlines()
            return misson

def plateau(mission):
    grid = mission[0]
    return grid
