import pygame

class Ball:
    def __init__(self, color, position, radius):
        self.color = color
        self.position = position
        self.radius = radius

    def paint(self, screen, rgbcolors):
        pygame.draw.circle(screen, rgbcolors[self.color], self.position, self.radius)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)