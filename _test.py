import pytest

import roving

filelist = ['instructions/file1.txt', 'instructions/file2.txt']

@pytest.fixture(params=filelist)
def files(request):
    yield request.param


def test_file_becomes_list(files):
    assert type(roving.opener(files)) == list

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
