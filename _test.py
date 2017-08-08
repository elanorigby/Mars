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
     ('34 56', ['7 30 W', 'LMLMLMLMM', '45 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N',
      'RMMMMLMMRMLLRMMMRM']))
    ])
def test_first_line(tinput, expected):
    assert roving.firstline(tinput) == expected


@pytest.mark.parametrize('tinput, expected', [
    (['1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM'], ('1 2 N', 'LMLMLMLMM', ['3 3 E', 'MMRMMRMRRM'])),
    (['7 30 W', 'LMLMLMLMM', '45 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM'],
     ('7 30 W', 'LMLMLMLMM', ['45 23 E', 'MMRMMRMRRM', '31 34 S', 'MMMMMMRLMMLMM', '4 12 N', 'RMMMMLMMRMLLRMMMRM']))
    ])
def test_rover_parse(tinput, expected):
    start, moves, mission = roving.rovers(tinput)
    assert (start, moves, mission) == expected

@pytest.mark.parametrize('tinput, expected', [
    ('1 2 N', ('1', '2', 'N')),
    ('3 3 E', ('3', '3', 'E')),
    ('31 34 S', ('31', '34', 'S'))
    ])
def test_start_parse(tinput, expected):
    assert roving.starter(tinput) == expected

@pytest.mark.parametrize('tinput, expected', [
    ('N', 'W'),
    ('W', 'S'),
    ('S', 'E'),
    ('E', 'N')
    ])
def test_turn_left(tinput, expected):
    assert roving.turnL(tinput) == expected



@pytest.mark.parametrize('tinput, expected', [
    ('N', 'E'),
    ('E', 'S'),
    ('S', 'W'),
    ('W', 'N')
])
def test_turn_right(tinput, expected):
    assert roving.turnR(tinput) == expected


def test_turn_wrong():
    with pytest.raises(ValueError):
        roving.turn('Q', 'L')


@pytest.mark.parametrize('tinput, expected', [
    (6, 7),
    (32, 33),
])
def test_move_north(tinput, expected):
    assert roving.moveN(tinput) == expected


@pytest.mark.parametrize('tinput, expected', [
    (6, 5),
    (32, 31),
])
def test_move_south(tinput, expected):
    assert roving.moveS(tinput) == expected


#   Are all the characters received expected characters?
#   must be in ('0123456789NSEWLRM ')

#   Did all the rovers land on the plateau?
#       For each rover:
#           roverX between 0 and inputX
#           roverY between 0 and inputY

#   Did all the rovers stay on the plateau?
#       roverX between 0 and inputX
#       roverY between 0 and inputY
#