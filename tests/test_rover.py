import pytest

from ..mission import roving


########## Rover Class Tests ##########

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

@pytest.mark.parametrize('start, moves, expected', [
    ('1 2 N', 'LMLMLMLMM', (1, 3, 'N')),
    ('3 3 E', 'MMRMMRMRRM', (4., 3, 'E')),
    ('31 34 S', 'MMMMMMRLMMLMM', (31, 33, 'S')),
    ('7 30 W', 'LMLMLRMLMMR', (6, 30, 'W')),
    ])
def test_go(start, moves, expected):
    rov = roving.Rover(start, moves)
    assert rov.go() == expected

@pytest.mark.parametrize('start, moves, move, expected', [
    ('1 2 N', 'LMLMLMLMM', 'M', (1, 3, 'N')),
    ('3 3 E', 'MMRMMRMRRM', 'M', (4., 3, 'E')),
    ('31 34 S', 'MMMMMMRLMMLMM', 'M', (31, 33, 'S')),
    ('7 30 W', 'LMLMLRMLMMR', 'M', (6, 30, 'W')),
    ('1 2 N', 'LMLMLMLMM', 'R', (1, 2, 'E')),
    ('3 3 E', 'MMRMMRMRRM', 'L', (3, 3, 'N')),
    ('31 34 S', 'MMMMMMRLMMLMM', 'R', (31, 34, 'W')),
    ('7 30 W', 'LMLMLRMLMMR', 'L', (7, 30, 'S')),
    ])
def test_drive(start, moves, move, expected):
    rov = roving.Rover(start, moves)
    assert rov.drive(move) == expected

@pytest.mark.parametrize('start, moves, move', [
    ('3 3 E', 'MMRMMRMRRM', 'G')
    ])
def test_drive_move_wrong(start, moves, move):
    rov = roving.Rover(start, moves)
    with pytest.raises(ValueError):
        assert rov.drive(move)

@pytest.mark.parametrize('start, moves, expected', [
    ('1 2 N', 'LMLMLMLMM', (1, 3, 'N')),
    ('3 3 E', 'MMRMMRMRRM', (5, 1, 'E')),
    ])
def test_makeitso(start, moves, expected):
    rov = roving.Rover(start, moves)
    rov.makeitso()
    assert (rov.x, rov.y, rov.facing) == expected
