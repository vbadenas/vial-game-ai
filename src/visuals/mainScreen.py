import pygame

class MainScreen:
    def __init__(self, size):
        self.initColors()
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Vial-game")
        self.clock = pygame.time.Clock()
        self.running = True

    def initColors(self):
        self.rgbColors = {
            "k": (0, 0, 0),
            "w": (255, 255, 255),
            "g": (0, 255, 0),
            "r": (255, 0, 0),
            "y": (255, 255, 0),
            "b": (0, 0, 255),
            "p": (127, 0, 255)
        }

    def paint(self, vialsList):
        self.clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
        self.screen.fill(self.rgbColors['w'])
        for vial in vialsList:
            self.__drawVial(vial)
        pygame.display.update()

    def __drawVial(self, vial):
        vial.paint(self.screen, self.rgbColors)

    def exit(self):
        self.running = False
        pygame.quit()

if __name__ == "__main__":
    class Vial:
        def __init__(self, colors, position):
            self.size = (10, 10)
            self.position = position
            self.colors = colors
    vials = [Vial('gbkr', (0, 0))]
    ms = MainScreen((400, 300))
    while ms.running:
        ms.paint(vials)