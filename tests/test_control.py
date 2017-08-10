import pytest

from ..mission import control
from ..mission import rover
from ..mission import plateau

@pytest.mark.parametrize('file, expected', [
    ('../instructions/file1.txt', ['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']),
    ('../instructions/file2.txt', ['34 56','7 30 W', 'LMLMLMLMM', '19 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM']),
    ])
def test_file_open(file, expected):
    con = control.Control(file)
    assert con.opener(file) == expected


@pytest.mark.parametrize('file, mission', [
    ('../instructions/file1.txt', ['5 5', '1 2 N', 'LMLMLMUMM', '3 3 E', 'MMRMMRMRRM'])
    ])
def test_checker(file, mission):
    con = control.Control(file)
    con.mission = mission
    with pytest.raises(ValueError):
        assert con.checker()


@pytest.mark.parametrize('file, expected', [
    ('../instructions/file1.txt', ['1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']),
    ('../instructions/file2.txt', ['7 30 W', 'LMLMLMLMM', '19 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM']),
    ])
def test_firstline(file, expected):
    con = control.Control(file)
    assert con.mission == expected


@pytest.mark.parametrize('file, expected', [
    ('../instructions/file1.txt', '5 5'),
    ('../instructions/file2.txt', '34 56'),
    ])
def test_grid_correct(file, expected):
    con = control.Control(file)
    assert con.grid == expected


@pytest.mark.parametrize('file, expected', [
    ('../instructions/file1.txt', rover.Rover),
    ('../instructions/file2.txt', rover.Rover),
    ])
def test_makerovers(file, expected):
    con = control.Control(file)
    rovlist = con.makerovers()
    for rov in rovlist:
        assert isinstance(rov, expected)


@pytest.mark.parametrize('file, expected', [
    ('../instructions/file1.txt', plateau.Plateau),
    ('../instructions/file2.txt', plateau.Plateau),
])
def test_makeplateau(file, expected):
    con = control.Control(file)
    plat = con.makeplateau()
    assert isinstance(plat, expected)
