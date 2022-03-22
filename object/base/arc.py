from cord import Cord

class Arc:
    def __init__(self, center: Cord, radius: float, startAngle: float, endAngle: float, isCCW: bool = True) -> None:
        self.center = center
        self.radius = radius
        self.startAngle = startAngle
        self.endAngle = endAngle
        self.isCCW = isCCW
       

class Circle:
     def __init__(self, center: Cord, radius: float) -> None:
        self.center = center
        self.radius = radius
        
