from object.base import cord
from object.base.cord import Cord
from object.base.line import Line

class Blank:
    def __init__(self, cords: list) -> None:
        self.cords = cords
        

    def __str__(self) -> str:
        result = '['
        for cord in self.cords:
            result = result + str(cord) + ', '
        result +=  str(self.cords[0]) + ']'
        return result

    def toLines(self) -> list:
        lines = []
        for i in range(0, len(self.cords)-1):
            lines.append(Line(self.cords[i], self.cords[i+1]))
        lines.append(Line(self.cords[len(self.cords)-1], self.cords[0]))
        return lines


class BlankFunction:
    def nemo(leftBot: Cord, rightTop: Cord) -> Blank:
        leftTop = Cord(leftBot.x, rightTop.y)
        rightBot = Cord(rightTop.x, leftBot.y)
        return Blank([leftBot, leftTop, rightTop, rightBot])