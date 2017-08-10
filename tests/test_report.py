import pytest

from ..mission import report
from ..mission import control
from ..mission import rover
from ..mission import plateau

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
    ('../instructions/file1.txt', [(1, 3, 'N'), (5, 1, 'E')]),
    ('../instructions/file2.txt', [(6, 30, 'W'), (21, 21, 'E'), (33, 26, 'E'), (10, 17, 'E')]),
    ('../instructions/file3.txt', ['Woops! This rover fell off the plateau. Nice driving, NASA.', (3, 8, 'S')]),
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
