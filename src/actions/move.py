class Move:
    def __init__(self, origin, destination):
        if not isinstance(origin, tuple) or not isinstance(destination, tuple):
            raise ValueError
        self.origin = origin
        self.destination = destination

    def __call__(self, vialList):
        isPossible = self._checkIfPossible(vialList)
        if isPossible:
            self.performMove(vialList)
        return isPossible

    def _checkIfPossible(self, vialList):
        ballcolor = vialList[self.origin]
        if len(vialList[self.destination].balls):
            return True