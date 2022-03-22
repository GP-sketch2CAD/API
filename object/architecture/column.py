from tables import Col
from object.base.cord import Cord
from object.base.arc import Circle
from object.base.blank import Blank, NemoBlank

class Column:
    def __init__(self) -> None:
        pass

class SquareColumn(Column):
    def __init__(self, leftBot:Cord, rigthTop:Cord) -> None:
        self.lines = NemoBlank(leftBot, rigthTop).toLines()
        
class CicleColumn(Column):
    def __init__(self, center: Cord, radius: float) -> None:
        self.column = Circle(center, radius)
        