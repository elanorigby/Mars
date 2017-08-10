import pytest
import sys
import os

# so that the tests can find the modules they need
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import mission.control as control
import mission.rover as rover
import mission.plateau as plateau
import mission.report as report

@pytest.mark.parametrize('start, moves, grid, expected', [
    ('3 3 E', 'MM', '14 14', True),
    ('34 12 N', 'MM', '45 10', False)
    ])
def test_ongrid(start, moves, grid, expected):
    plat = plateau.Plateau(grid)
    rov = rover.Rover(start, moves)
    rep = report.Report(plat, rov)
    assert rep.ongrid() == expected


@pytest.mark.parametrize('start, moves, grid, expected', [
    ('3 3 E', 'MM', '14 14', (3, 3, 'E')),
    ('34 12 N', 'MM', '45 10', "Woops! This rover fell off the plateau. Nice driving, NASA.")
    ])
def test_report(start, moves, grid, expected):
    plat = plateau.Plateau(grid)
    rov = rover.Rover(start, moves)
    rep = report.Report(plat, rov)
    assert rep.message() == expected


@pytest.mark.parametrize('file, expected', [
    ('instructions/file1.txt', [(1, 3, 'N'), (5, 1, 'E')]),
    ('instructions/file2.txt', [(6, 30, 'W'), (21, 21, 'E'), (33, 26, 'E'), (10, 17, 'E')]),
    ('instructions/file3.txt', ['Woops! This rover fell off the plateau. Nice driving, NASA.', (3, 8, 'S')]),
    ])
def test_total(file, expected):
    con = control.Control(file)
    plat = con.makeplateau()
    roverlist = con.makerovers()
    reportlist = []
    for rov in roverlist:
        rov.makeitso()
        rep = report.Report(plat, rov)
        reportlist.append(rep.message())
    assert reportlist == expected
