import unittest
from src.main import BallSortGame

class TestCompletion:
    def test_completionOk(self):
        colors = 'bbbbkkkkggggyyyy'
        ballSortGame = BallSortGame(colors)
        self.assertTrue(ballSortGame.checkForCompletion())

if __name__ == "__main__":
    unittest.main()