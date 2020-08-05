import time
from actions import Move
from objects import Vial
from visuals import MainScreen
from pprint import pprint

class Main:
    def __init__(self, colors):
        self._initVials(colors)

    def _initVials(self, colors):
        if len(colors) % 4 != 0:
            raise ValueError("colors must be a multiple of 4")
        numberOfVials = len(colors) // 4 + 2
        print(f"{numberOfVials} will be used in this level")
        self.vials = [None]*numberOfVials
        for i in range(numberOfVials - 2):
            self.vials[i] = Vial(colors[4*i:4*i+4], (100*(i+1), 50))
        self.vials[-2] = Vial([], (100*(numberOfVials-1), 50))
        self.vials[-1] = Vial([], (100*(numberOfVials), 50))

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)

    def showVials(self):
        for vial in self.vials:
            print(vial)

    def run(self):
        pass

if __name__ == "__main__":
    colors = 'bgkyyykkgbbgbykg'
    main = Main(colors)
    main.showVials()