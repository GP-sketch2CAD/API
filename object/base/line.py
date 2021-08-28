from object.base.cord import Cord
import math

class Line:
    def __init__(self, start: Cord, end: Cord) -> None:
        swap = False

        if start.x == end.x:
            if start.y == end.y: return None
            if start.y > end.y: swap = True
        elif start.x > end.x : swap = True

        if swap:
            self.start = end
            self.end = start
        else:
            self.start = start
            self.end = end

        self.straight = Straight(start, end)
        pass

    def __str__(self) -> str:
        return '[{}, {}]'.format(self.start, self.end)
    
    def __add__(self, o: object) -> object:
        if self.__class__ != o.__class__: return None
        if LineFunction.isMeet(self, o) == False: return None

        if self.start.x > o.start.x: self.start = o.start
        elif self.straight.b == 0 and self.start.y > o.start.y: self.start = o.start

        if self.end.x < o.end.x: self.end = o.end
        elif self.straight.b == 0 and self.end.y < o.end.y: self.end = o.end

        return self
        

    def __sub__(self, o: object) -> object:
        if self.__class__ != o.__class__: return None
        if LineFunction.isMeet(self, o) == False: return None
        if LineFunction.isPcontainQ(p = o, q = self):
            self.delete()
            return None
        
        if o.start.x <= self.start.x and  self.start.x < o.end.x: self.start = o.end
        elif self.straight.b == 0 and o.start.y <= self.start.y and self.start.y < o.end.y: self.start = o.end

        if  o.start.x < self.end.x and self.end.x <= o.end.x: self.end = o.start
        elif self.straight.b == 0 and  o.start.y < self.end.y and self.end.y <= o.end.y: self.end = o.start
        
        return self
        
    def delete(self):
        self.straight = None
        self.end = None
        self.start = None
    
    def moveXY(self, x = 0., y = 0.) -> None:
        """
        move the line by the given x,y 
        """
        self.straight.move(x,y)
        self.start.move(x,y)
        self.end.move(x,y)
        pass

    def movePal(self, distance: float) -> None:
        if self.straight.b == 0:
            self.c += distance
        else: 
            self.c = distance * (self.straight.a**2 +1)**0.5
        pass

        
class Straight:
    """
    ax + by + c = 0
    """
    def __init__(self, start: Cord, end: Cord) -> None:
        if start.x == end.x:
            self.a = -1
            self.b = 0
            self.c = start.x
        else:
            self.a = (end.y - start.y) / (end.x - start.x)
            self.b = -1
            self.c = start.y - self.a*start.x
    
    def __str__(self) -> str:
        return '{}x + {}y + {}'.format(self.a, self.b, self.c)
    
    def __eq__(self, o: object) -> bool:
        if self.__class__ == o.__class__:
            if (self.a == o.a) and (self.b == o.b) and (self.c == o.c):
                return True
        return False
        
    def move(self, x = 0., y = 0.) -> None:
        """
        move the straight by the given x,y 
        """
        self.c -= self.a*x + self.b*y
        pass

    def moveTo(self, cord: Cord) -> None:
        """
        move the straight the given cord
        """
        self.c = - (self.a*cord.x + self.b*cord.y)
              

class LineFunction:
    @staticmethod
    def isCCW(line: Line, cord: Cord) -> bool:
        ccw = line.start.x*line.end.y + line.end.x*cord.y + cord.x*line.start.y - (line.end.x*line.start.y + cord.x*line.end.y + line.start.x*cord.y)
        if ccw > 0: return True
        else: return False

    @staticmethod
    def isCross(p: Line, q: Line) -> bool:
        if p.straight == q.straight: return False
        if LineFunction.isCCW(p.start, p.end, q.start) ^ LineFunction.isCCW(p.start, p.end, q.end):
            if LineFunction.isCCW(q.start, q.end, p.start) ^ LineFunction.isCCW(q.start, q.end, p.end):
                return True
        return False

    @staticmethod
    def isPcontainQ(p: Line, q: Line) -> bool:
        if p.straight == q.straight: 
            if (p.start.x <= q.start.x and p.end.x >= q.end.x and 
                p.start.y <= q.start.y and p.end.y >= q.end.y):
                return True
        return False

    @staticmethod
    def isLcontainC(p: Line, c: Cord) -> bool:
        if p.straight.a * c.x + p.straight.b * c.y + p.straight.c == 0:
            if (p.end.x - c.x) * (c.x - p.start.x) >= 0:
                if (p.end.y - c.y) * (c.y - p.start.y) >= 0:
                    return True
        return False
    
    @staticmethod
    def isMeet(p: Line, q: Line) -> bool:
        if p.straight == q.straight:
            if (LineFunction.isLcontainC(p, q.start) or LineFunction.isLcontainC(p, q.end) or 
                    LineFunction.isLcontainC(q, p.start) or LineFunction.isLcontainC(q, p.end)):
                return True
        else: return False

    
    @staticmethod
    def getBetweenAngle(p: Line, q: Line) -> float:
        """
        get the angle between two lines
        reference
        -----
        https://darkpgmr.tistory.com/121
        """
        if p.start == q.start:
            a = (p.end.x-p.start.x, p.end.y - p.start.y)
            b = (q.end.x-p.start.x, q.end.y - p.start.y)
        elif p.start == q.end:
            a = (p.end.x-p.start.x, p.end.y - p.start.y)
            b = (q.start.x-p.start.x, q.start.y - p.start.y)
        else: 
            return None
        
        son = a[0]*b[1] - a[1]*b[0]
        mom = (a[0]**2 + a[1]**2)**0.5 * (b[0]**2 + b[1]**2)**0.5

        return math.asin(son/mom)  

    