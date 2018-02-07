import unittest

class TestMethods(unittest.TestCase):

    def test_givenSShouldReturnBackward(self):
        rover = Rover()
        rover.setDirection('s')
        self.assertEqual(rover.getDirection(), "Down")

    def test_givenAShouldReturnLeft(self):
        rover = Rover()
        rover.setDirection('a')
        self.assertEqual(rover.getDirection(), "Left")

    def test_givenWShouldReturnUp(self):
        rover = Rover()
        rover.setDirection('w')
        self.assertEqual(rover.getDirection(), "Up")

    def test_givenDShouldReturnRight(self):
        rover = Rover()
        rover.setDirection('d')
        self.assertEqual(rover.getDirection(), "Right")

    def test_givenNothingShouldReturnCoord(self):
        rover = Rover()
        coord = [2,8]
        rover.setCoord(2,8)
        self.assertEqual(rover.getCoord(), coord)

    def test_givenForwardShouldReturnIncrementForwardVariable(self):
        rover = Rover()
        x = rover.getXCoord()
        rover.goForward()
        self.assertEqual(rover.getXCoord(),x+1)

#    def test_givenForwardShouldReturnIncrementBackwardVariable(self):
#        rover = Rover()
#        y = rover.getYCoord()
#        rover.goBackward()
#        self.assertEqual(rover.getYCoord(),y+1)

class Rover:

    def __init__(self):
        self.direction = "Forward"
        self.coord = [0,0]
    def setDirection(self, c):
        if c == 'a':
            self.direction = "Left"
        elif c == 'w':
            self.direction = "Up"
        elif c == 'd':
            self.direction = "Right"
        elif c == 's':
            self.direction = "Down"
        else:
            self.direction = "Up"

    def getDirection(self):
        return self.direction

    def setCoord(self,i,j):
        self.coord = [i,j]


    def getCoord(self):
        return self.coord

    def getXCoord(self):
        return self.getCoord()[0]

    def goForward (self):
        self.setCoord(self.getXCoord()+1,0)