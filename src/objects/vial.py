from objects.ball import Ball
from collections import Iterable

class Vial:
    def __init__(self, ballColors, position):
        if len(ballColors) not in [0, 4]:
            raise ValueError
        self.position = position
        self.size = (50, 200)
        self.createBalls(ballColors)

    def paint(self):
        pass
    
    def createBalls(self, ballColors):
        self.balls = []
        for i, color in enumerate(ballColors):
            self.balls.append(Ball(color, (self.position[0], 50*(i+1))))

    def __str__(self):
        msg = 'Vial(\t'
        for attribute in self.__dict__:
            if isinstance(self.__dict__[attribute], list):
                msg += f'\n\t{attribute}[\n'
                for item in self.__dict__[attribute]:
                    msg += f'\t\t{item},\n'
                msg += '\t]\n'
            else:
                msg += f'{attribute}: {self.__dict__[attribute]}, '
        msg += ')\n'
        return msg

    def __repr__(self):
        return str(self.__dict__)

    def addBall(self, ballColor):
        if len(self.balls) > 3:
            return
        else:
            self.balls.append(ballColor)

    def popLastBall(self):
        if len(self.balls) > 0:
            return self.balls.pop()
        return None

    def getLastBall(self):
        return self.balls[-1]

    def __len__(self):
        return len(self.balls)