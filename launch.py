from mission.control import Control
from mission.report import Report

import sys


if __name__ == '__main__':
    file = sys.argv[1]
    con = Control(file)
    plat = con.makeplateau()
    roverlist = con.makerovers()
    for rov in roverlist:
        rov.makeitso()
        rep = Report(plat, rov)
        print(rep.message())
