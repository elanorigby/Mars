def opener(file):
        with open(file) as f:
            misson = f.read().splitlines()
            return misson

def firstline(mission):
    return mission[0]
