import pygame
from objects.ball import Ball
from collections import Iterable

class Vial:
    def __init__(self, ballColors, position):
        if len(ballColors) not in [0, 4]:
            raise ValueError
        self.position = position
        self.size = (50, 200)
        self.createBalls(ballColors)

    def paint(self, screen, rgbcolors):
        rect = self.position + self.size
        pygame.draw.rect(screen, rgbcolors['k'], rect, 1)
        for ball in self.balls:
            ball.paint(screen, rgbcolors)
    
    def createBalls(self, ballColors):
        self.balls = []
        for i, color in enumerate(ballColors):
            position = (self.position[0]+25, 50*(4-i)+25)
            self.balls.append(Ball(color, position, 24))

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

    def addBall(self, ball):
        if len(self.balls) > 3:
            return
        else:
            newPosition = (self.position[0]+25, 50*(4-len(self.balls))+25)
            ball.updatePosition(newPosition)
            self.balls.append(ball)

    def popLastBall(self):
        if len(self.balls) > 0:
            return self.balls.pop()
        return None

    def getLastBall(self):
        return self.balls[-1]

    def __len__(self):
        return len(self.balls)

    def getColorList(self):
        return [ball.color for ball in self.balls]
