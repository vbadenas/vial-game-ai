import sys
import unittest
sys.path.append("./src")
from main import *

class TestCompletion(unittest.TestCase):
    def test_completionOk(self):
        colors = 'bbbbkkkkggggyyyy'
        ballSortGame = BallSortGame(colors)
        self.assertTrue(ballSortGame.checkForCompletion())

    def test_completionNOk(self):
        colors = 'bgkyyykkgbbgbykg'
        ballSortGame = BallSortGame(colors)
        self.assertFalse(ballSortGame.checkForCompletion())

if __name__ == "__main__":
    unittest.main()