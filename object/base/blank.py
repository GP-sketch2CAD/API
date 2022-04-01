from object.base.cord import Cord
from object.base.line import Line

class Blank:
    def __init__(self, cords: list) -> None:
        self.cords = cords
        
    def __str__(self) -> str:
        return 'Blank: [' + ', '.join(map(str, self.cords)) + ', ' + str(self.cords[0]) +']'

    def toLines(self) -> list:
        length = len(self.cords)
        return [Line(self.cords[i], self.cords[(i+1)% length]) for i in range(0, length)]

    def rotate(self, degree: float):
        for c in self.cords:
            c.rotate(degree)
    
    def move(self, dx, dy):
        for c in self.cords:
            c.move(dx, dy)


class NemoBlank(Blank):
    def __init__(self, leftBot: Cord, rightTop: Cord) -> None:
        leftTop = Cord(leftBot.x, rightTop.y)
        rightBot = Cord(rightTop.x, leftBot.y)
        super().__init__([leftBot, leftTop, rightTop, rightBot])



