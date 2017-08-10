import pytest

from ..mission import roving


########## Control Class Tests ##########

@pytest.mark.parametrize('file, expected', [
    ('instructions/file1.txt', ['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']),
    ('instructions/file2.txt', ['34 56','7 30 W', 'LMLMLMLMM', '19 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM']),
    ])
def test_file_open(file, expected):
    control = roving.Control(file)
    assert control.opener(file) == expected

@pytest.mark.parametrize('file, expected', [
    ('instructions/file1.txt', ['1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']),
    ('instructions/file2.txt', ['7 30 W', 'LMLMLMLMM', '19 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM']),
    ])
def test_mission_parse(file, expected):
    control = roving.Control(file)
    assert control.mission == expected


@pytest.mark.parametrize('file, expected', [
    ('instructions/file1.txt', '5 5'),
    ('instructions/file2.txt', '34 56'),
    ])
def test_grid_parse(file, expected):
    control = roving.Control(file)
    assert control.grid == expected


@pytest.mark.parametrize('file, expected', [
    ('instructions/file1.txt', roving.Rover),
    ('instructions/file2.txt', roving.Rover),
    ])
def test_rover_parse(file, expected):
    control = roving.Control(file)
    rovlist = control.makerovers()
    for rov in rovlist:
        assert isinstance(rov, expected)

@pytest.mark.parametrize('file, expected', [
    ('instructions/file1.txt', roving.Plateau),
    ('instructions/file2.txt', roving.Plateau),
])
def test_plateau_parse(file, expected):
    control = roving.Control(file)
    plateau = control.makegrid()
    assert isinstance(plateau, expected)
