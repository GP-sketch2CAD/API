from object.base.cord import Cord
from object.base.arc import Circle
from object.base.blank import Blank, BlankFunction

class SquareColumn:
    def __init__(self, leftBot:Cord, rigthTop:Cord) -> None:
        self.lines = BlankFunction.nemo(leftBot, rigthTop).toLines()
        
class CicleColumn:
    def __init__(self, center: Cord, radius: float) -> None:
        self.column = Circle(center, radius)
        