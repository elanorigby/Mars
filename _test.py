import roving

file1 = 'instructions/file1.txt'

def test_file_opener():
    assert roving.opener(file1) != None


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
