import math

class Cord:
    def __init__(self, x : float = 0, y: float = 0) -> None:
        self.setCord([x,y])

    def __str__(self) -> str:
        return 'Cord: ({},{})'.format(self.x, self.y)

    def __eq__(self, o: object) -> bool:
        return (self.__class__ == o.__class__) and (self.x == o.x) and (self.y == o.y)

    def setCord(self, xy) -> None:
        """
        set cord to given xy
        """
        self.x = xy[0]
        self.y = xy[1]

    def move(self, x = 0., y= 0.) -> None:
        """
        move cord by given x,y
        """
        self.x += x
        self.y += y

    def rotate(self, degree: float, dx = 0., dy = 0.) -> None:
        """
        clockwise rotate as degree

        reference
        ----------
        https://java.elex.pe.kr/2016/05/transform-rotation.html
        """
        sinD = math.sin(math.radians(degree))
        cosD = math.cos(math.radians(degree))
        bx = self.x
        by = self.y
        
        ax = (bx-dx)*cosD + (by-dy)*sinD
        ay = (by-dy)*cosD - (bx-dx)*sinD  

        self.x = round(ax,2)
        self.y = round(ay,2)
        

    def getTuple(self) -> tuple:
        """
        return (x,y)
        """
        return (self.x, self.y)
