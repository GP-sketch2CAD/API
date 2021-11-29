import math

class Cord:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '({},{})'.format(self.x, self.y)

    def __eq__(self, o: object) -> bool:
        return (self.__class__ == o.__class__) and (self.x == o.x) and (self.y == o.y)

    def move(self, x = 0., y= 0.) -> None:
        """
        move cord by given x,y
        """
        self.x += x
        self.y += y

    def rotate(self, degree: float, x = 0., y = 0.) -> None:
        """
        cw rotate as degree

        reference
        ----------
        https://java.elex.pe.kr/2016/05/transform-rotation.html
        """
        sinD = math.sin(math.radians(degree))
        cosD = math.cos(math.radians(degree))
        bx = self.x
        by = self.y
        
        ax = (bx-x)*cosD + (by-y)*sinD
        ay = (by-y)*cosD - (bx-x)*sinD  

        self.x = round(ax,2)
        self.y = round(ay,2)
        

    def toTuple(self) -> tuple:
        return (self.x, self.y)

class CordFunction:
    @staticmethod
    def list2cord(xy: list or tuple)-> Cord:
        return Cord(xy[0], xy[1])