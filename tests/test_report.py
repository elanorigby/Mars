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