class Ball:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.size = (50, 50)

    def paint(self):
        pass

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)