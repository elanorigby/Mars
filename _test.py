import pytest

import roving

filelist = ['instructions/file1.txt', 'instructions/file2.txt']


@pytest.fixture(params=filelist)
def files(request):
    yield request.param


def test_file_becomes_list(files):
    assert type(roving.opener(files)) == list


@pytest.mark.parametrize('tinput, expected', [
    (['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM'], ('5 5', ['1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM'])),
    (['34 56', '7 30 W', 'LMLMLMLMM', '45 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM'],
        ('34 56', ['7 30 W', 'LMLMLMLMM', '45 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM'])),
    ])
def test_first_line(tinput, expected):
    assert roving.firstline(tinput) == expected


@pytest.mark.parametrize('tinput, expected', [
    (['1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM'], ('1 2 N', 'LMLMLMLMM', ['3 3 E', 'MMRMMRMRRM'])),
    (['7 30 W', 'LMLMLMLMM', '45 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM'],
     ('7 30 W', 'LMLMLMLMM', ['45 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM'])),
    ])
def test_rover_parse(tinput, expected):
    start, moves, mission = roving.rovers(tinput)
    assert (start, moves, mission) == expected


@pytest.mark.parametrize('start, moves, expected', [
    ('1 2 N','LMLMLMLMM', (1, 2, 'N')),
    ('3 3 E', 'MMRMMRMRRM', (3, 3, 'E')),
    ('31 34 S', 'MMMMMMRLMMLMM', (31, 34, 'S')),
    ])
def test_start_parse(start, moves, expected):
    rov = roving.Rover(start, moves)
    assert rov.starter() == expected


@pytest.mark.parametrize('start, moves, tinput, expected', [
    ('1 2 N', 'LMLMLMLMM', 'N', 'W'),
    ('3 3 E', 'MMRMMRMRRM', 'W', 'S'),
    ('31 34 S', 'MMMMMMRLMMLMM', 'S', 'E'),
    ('7 30 W', 'LMLMLRMLMMR', 'E', 'N'),
    ])
def test_turn_left(start, moves, tinput, expected):
    rov = roving.Rover(start, moves)
    rov.facing = tinput
    assert rov.turnL() == expected


@pytest.mark.parametrize('start, moves, tinput, expected', [
    ('1 2 N', 'LMLMLMLMM', 'N', 'E'),
    ('3 3 E', 'MMRMMRMRRM', 'E', 'S'),
    ('31 34 S', 'MMMMMMRLMMLMM', 'S', 'W'),
    ('7 30 W', 'LMLMLRMLMMR', 'W', 'N'),
    ])
def test_turn_right(start, moves, tinput, expected):
    rov = roving.Rover(start, moves)
    rov.facing = tinput
    assert rov.turnR() == expected


@pytest.mark.parametrize('start, moves, tinput, expected', [
    ('1 2 N', 'LMLMLMLMM', 'R', 'E'),
    ('3 3 E', 'MMRMMRMRRM', 'L', 'N'),
    ('31 34 S', 'MMMMMMRLMMLMM', 'R', 'W'),
    ('7 30 W', 'LMLMLRMLMMR', 'L', 'S'),
    ])
def test_turn_switch(start, moves, tinput, expected):
    rov = roving.Rover(start, moves)
    assert rov.turn(tinput) == expected


@pytest.mark.parametrize('start, moves, expected', [
    ('1 2 N', 'LMLMLMLMM', 3),
    ])
def test_go_north(start, moves, expected):
    rov = roving.Rover(start, moves)
    assert rov.goN() == expected


@pytest.mark.parametrize('start, moves, expected', [
    ('31 34 S', 'MMMMMMRLMMLMM', 33),
    ])
def test_go_south(start, moves, expected):
    rov = roving.Rover(start, moves)
    assert rov.goS() == expected


@pytest.mark.parametrize('start, moves, expected', [
    ('3 3 E', 'MMRMMRMRRM', 4),
    ])
def test_go_east(start, moves, expected):
    rov = roving.Rover(start, moves)
    assert rov.goE() == expected


@pytest.mark.parametrize('start, moves, expected', [
    ('7 30 W', 'LMLMLRMLMMR', 6),
    ])
def test_go_west(start, moves, expected):
    rov = roving.Rover(start, moves)
    assert rov.goW() == expected


@pytest.mark.parametrize('x, y, facing, expected', [
    (6, 44, 'N', (6, 45, 'N')),
    (32, 11, 'W', (31, 11, 'W')),
    ])
def test_go(x, y, facing, expected):
    assert roving.go(x, y, facing) == expected


def test_go_wrong():
    with pytest.raises(ValueError):
        roving.go(4, 17, 'Q')


@pytest.mark.parametrize('x, y, facing, move, expected', [
    (3, 6, 'E', 'L', (3, 6, 'N')),
    (12, 33, 'S', 'M', (12, 32, 'S'))
    ])
def test_drive(x, y, facing, move, expected):
    assert roving.drive(x, y, facing, move) == expected


@pytest.mark.parametrize('roverx, rovery, gridx, gridy, expected', [
    (23, 2, 43, 16, True),
    (17, 56, 13, 60, False)
    ])
def test_rover_on_grid(roverx, rovery, gridx, gridy, expected):
    assert roving.ongrid(roverx, rovery, gridx, gridy) == expected
