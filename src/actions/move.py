class Move:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def __call__(self, vialList):
        isPossible = self._checkIfPossible(vialList)
        if isPossible:
            self._performMove(vialList)
        return isPossible

    def _checkIfPossible(self, vialList):
        ballcolor = vialList[self.origin].getLastBall().color
        if len(vialList[self.destination]) == 0:
            return True
        if len(vialList[self.destination]) == 4:
            return False
        if vialList[self.destination].getLastBall().color == ballcolor:
            return True
        return False

    def _performMove(self, vialList):
        ball = vialList[self.origin].popLastBall()
        vialList[self.destination].addBall(ball)
