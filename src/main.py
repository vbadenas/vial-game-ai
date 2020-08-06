import time
from actions import Move
from objects import Vial
from visuals import MainScreen
from pprint import pprint

class BallSortGame:
    def __init__(self, colors):
        self._initVials(colors)

    def _initVials(self, colors):
        if len(colors) % 4 != 0:
            raise ValueError("colors must be a multiple of 4")
        numberOfVials = len(colors) // 4 + 2
        self.vials = [Vial(colors[4*i:4*i+4], (100*(i+1), 50)) for i in range(numberOfVials - 2)]
        self.vials.append(Vial([], (100*(numberOfVials-1), 50)))
        self.vials.append(Vial([], (100*(numberOfVials), 50)))

    def __call__(self, *args, **kwargs):
        self.performMove(*args, **kwargs)

    def showVials(self):
        for vial in self.vials:
            print(vial)

    def displayColors(self):
        colors = [vial.getColorList() for vial in self.vials]
        print('\n'.join([f"{i}:\t{vial}" for i, vial in enumerate(map(str, colors))]))

    def performMove(self):
        origin, destination = self._inputValues()
        move = Move(origin, destination)
        move(self.vials)

    def _inputValues(self):
        range_ = range(6)
        message = f"next move in range ({min(range_)}, {max(range_)}): "
        values = []
        while len(values)!=2 or all(value not in range_ for value in values):
            values = input(message)
            values = list(map(int, values.split(',')))
        return values

    def _inputValue(self, range_, message):
        value = None
        message += f" in range ({min(range_)}, {max(range_)}): "
        while value not in range_:
            value = int(input(message))
        return value

    def checkForCompletion(self):
        colors = [vial.getColorList() for vial in self.vials]
        complete = []
        for colorList in colors:
            check = len(colorList) in [0, 4] and len(set(colorList)) == 1
            complete.append(check)
        return all(complete)

if __name__ == "__main__":
    colors = 'bgkyyykkgbbgbykg'
    ballSortGame = BallSortGame(colors)
    ballSortGame.displayColors()
    while not ballSortGame.checkForCompletion():
        ballSortGame.performMove()
        ballSortGame.displayColors()