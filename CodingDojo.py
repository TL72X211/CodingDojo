import unittest

class TestMethods(unittest.TestCase):

    def test_givenWShouldReturnForward(self):
        rover = Rover()
        self.assertEqual(rover.getDirection(), "Forward")

    def test_givenSShouldReturnBackward(self):
        rover = Rover()
        rover.setDirection('s')
        self.assertEqual(rover.getDirection(), "Backward")

    def test_givenAShouldReturnLeft(self):
        rover = Rover()
        rover.setDirection('a')
        self.assertEqual(rover.getDirection(), "Left")

    def test_givenDShouldReturnUp(self):
        rover = Rover()
        rover.setDirection('z')
        self.assertEqual(rover.getDirection(), "Up")





class Rover:

    def __init__(self):
        self.direction = "Forward"

    def setDirection(self, c):
        if c == 'a':
            self.direction = "Left"
        else:
            self.direction = "Backward"

    def getDirection(self):
        return self.direction