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
    mission = tinput
    assert roving.firstline(mission) == expected


def test_rover_parse():
    mission = ['1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']
    start, moves, mission = roving.rovers(mission)
    assert start == '1 2 N' and moves == 'LMLMLMLMM' and mission == ['3 3 E', 'MMRMMRMRRM']

#   Are all the characters received expected characters?
#       must be in ('0123456789NSEWLRM ')

#   Did all the rovers land on the plateau?
#       For each rover:
#           roverX between 0 and inputX
#           roverY between 0 and inputY
#   turnR(direction) -> correct new direction
#   turnL(direction) -> correct new direction
#   move(direction, coords) -> correct new coords

#   Did all the rovers stay on the plateau?
#       roverX between 0 and inputX
#       roverY between 0 and inputY
#