import pytest

from ..mission import roving


########## Report Class Tests ##########

@pytest.mark.parametrize('start, moves, grid, expected', [
    ('3 3 E', 'MM', '14 14', (3, 3, 'E')),
    ('34 12 N', 'MM', '45 10', "Woops! This rover fell off the plateau. Nice driving, NASA.")
    ])
def test_report(start, moves, grid, expected):
    plateau = roving.Plateau(grid)
    rover = roving.Rover(start, moves)
    report = roving.Report(plateau, rover)
    assert report.message() == expected


@pytest.mark.parametrize('file, expected', [
    ('instructions/file1.txt', [(1, 3, 'N'), (5, 1, 'E')]),
    ('instructions/file2.txt', [(6, 30, 'W'), (21, 21, 'E'), (33, 26, 'E'), (10, 17, 'E')]),
    ('instructions/file3.txt', ['Woops! This rover fell off the plateau. Nice driving, NASA.', (3, 8, 'S')]),
    ])
def test_total(file, expected):
    control = roving.Control(file)
    plateau = control.makegrid()
    roverlist = control.makerovers()
    reportlist = []
    for rover in roverlist:
        rover.makeitso()
        report = roving.Report(plateau, rover)
        reportlist.append(report.message())
    assert reportlist == expected
