import random
from timeUtils import TimeStatisticsCalculator

colorsMap = {
    0: "k",
    1: "g",
    2: "r",
    3: "y",
    4: "b",
    5: "g",
    6: "p",
}

def generateRandomColorSequence(numberOfColors):
    colors = []
    for colorIdx in range(numberOfColors):
        colors += [colorsMap[colorIdx]]*4
    random.shuffle(colors)
    return colors

if __name__ == "__main__":
    import time
    numberOfExecutions = int(1e4)
    tsc = TimeStatisticsCalculator()
    for i in range(numberOfExecutions):
        tsc(generateRandomColorSequence, 5)
    tsc.report()