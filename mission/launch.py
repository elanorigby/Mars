import sys

import mission.control
import mission.report


if __name__ == '__main__':
    file = sys.argv[1]
    control = mission.control.Control(file)
    plateau = control.makeplateau()
    roverlist = control.makerovers()
    for rover in roverlist:
        rover.makeitso()
        report = mission.report.Report(plateau, rover)
        print(report.message())
