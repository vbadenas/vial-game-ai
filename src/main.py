import time
from actions import Move
from objects import Vial
from visuals import MainScreen
from pprint import pprint
from utils.data import generateRandomColorSequence

class BallSortGame:
    def __init__(self, colors):
        self._initVials(colors)
        self.screen = MainScreen(((len(self.vials)*100 + 50), 300))
        self.running = True

    def _initVials(self, colors):
        if len(colors) % 4 != 0:
            raise ValueError("colors must be a multiple of 4")
        numberOfVials = len(colors) // 4 + 2
        self.vials = [Vial(colors[4*i:4*i+4], (100*i+50, 50)) for i in range(numberOfVials - 2)]
        self.vials.append(Vial([], (100*(numberOfVials-2) + 50, 50)))
        self.vials.append(Vial([], (100*(numberOfVials-1) + 50, 50)))

    def __call__(self, *args, **kwargs):
        self.performMove(*args, **kwargs)

    def showVials(self):
        for vial in self.vials:
            print(vial)

    def displayColorsInTerminal(self):
        colors = [vial.getColorList() for vial in self.vials]
        print('\n'.join([f"{i}:\t{vial}" for i, vial in enumerate(map(str, colors))]))

    def performMove(self):
        origin, destination = self._inputValues()
        if origin is None and destination is None:
            return
        move = Move(origin, destination)
        move(self.vials)

    def _inputValues(self):
        range_ = range(6)
        message = f"next move in range ({min(range_)}, {max(range_)}): "
        values = []
        while len(values)!=2 or all(value not in range_ for value in values):
            values = input(message)
            if values.lower() == "exit":
                self.exit()
                return None, None
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
            check = (len(colorList) == 4 and len(set(colorList)) == 1) or len(colorList) == 0
            complete.append(check)
        return all(complete)

    def paint(self):
        self.screen.paint(self.vials)

    def exit(self):
        self.screen.exit()
        self.running = False

if __name__ == "__main__":
    colors = generateRandomColorSequence(4)
    ballSortGame = BallSortGame(colors)
    ballSortGame.paint()
    while not ballSortGame.checkForCompletion() and ballSortGame.running:
        ballSortGame.showVials()
        ballSortGame.displayColorsInTerminal()
        ballSortGame.paint()
        ballSortGame.performMove()
        ballSortGame.paint()
    if ballSortGame.checkForCompletion():
        print("Congratulations, you solved the game")
        while ballSortGame.screen.running:
            ballSortGame.paint()