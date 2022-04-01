from typing import Tuple
from object.base.cord import Cord

def getCCW(a: Cord, b: Cord, c: Cord) -> int:
        return (b.x-a.x)*(c.y-a.y) -(b.y-a.y)*(c.x-a.x)

def getCrossPoint(x1,y1,x2,y2,x3,y3,x4,y4) -> Tuple:
    m = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    x = (x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)
    x /= m
    y = (x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)
    y /= m

    return (x,y)

class Line:
    def __init__(self, start: Cord, end: Cord):
        if start == end: return
        else:
            self.setLine([start, end])
        
    def __str__(self) -> str:
        return 'Line: [{}, {}]'.format(self.cords[0], self.cords[1])  
    
    def setLine(self, cords: list) -> None:
        self.cords = cords

    def move(self, x = 0., y = 0.) -> None:
        """
        move the line by the given x,y 
        """
        for c in self.cords:
            c.move(x,y)

    def rotate(self, degree: float, dx = 0., dy= 0.) -> None:
        """
        clockwise rotate as degree 
        """
        for c in self.cords:
            c.rotate(degree,dx,dy)
    
    def connect(self, other) -> bool:
        """
        connect self and other line if two lines are in a straight
        if two lines are not in a staright return false
        """
        if not isinstance(other, Line):
            return False
        elif self.getStraight() != other.getStraight():
            return False

        for oc in other.cords:
            self.cords.append(oc)

        self.cords.sort(key = lambda x: (x[0], x[1]))
        self.cords = [self.cords[0], self.cords[-1]]
        return True

    def getStraight(self) -> tuple:
        """
        to get self's straight information by tuple
        the format of the tuple is (a,b,c) that means ax+by+c = 0
        """
        if self.cords[0].x == self.cords[1].x:
            return (-1,0,self.cords[0].x) 
        else:
            a = (self.cords[0].y - self.cords[1].y) / (self.cords[0].x - self.cords[1].x)
            c = self.cords[1].y - a*self.cords[1].x
            return (a,-1,c)
    
    def isCross(self, other) -> bool:
        
        # exception handling
        if not isinstance(other, Line): 
            return False
        elif self.getStraight() == other.getStraight():
            return False
        for sc in self.cords:
            for oc in other.cords:
                if sc == oc: return False

        # claclulste ccw
        so = getCCW(self.cords[0],self.cords[1],other.cords[0]) * getCCW(self.cords[0],self.cords[1],other.cords[1])
        os = getCCW(other.cords[0],other.cords[1],self.cords[0]) * getCCW(other.cords[0],other.cords[1],self.cords[1])

        if so <= 0 and os <= 0: return True
        return False
    
    def getCrossPoint(self, other) -> Cord:
        x, y = getCrossPoint(self.cords[0].x,self.cords[0].y,
                            self.cords[1].x,self.cords[1].y,
                            other.cords[0].x,other.cords[0].y,
                            other.cords[1].x,other.cords[1].y)
        return Cord(x,y)
        
    def getRelOnStraight(self, other) -> str:
        """
        return relationship with other lines
        type of relationships are [None, connect, be included, include, overlap, not meet]
        """
        if not isinstance(other, Line): 
            return None
        elif self.getStraight() == other.getStraight():
            temp = self.cords + other.cords
            temp.sort(key= lambda x:(x.x, x.y))
            
            if temp[1] == temp[2]: 
                return 'connect'
            elif temp[1] in self.cords and temp[2] in self.cords:
                return 'be included'
            elif temp[0] in self.cords and temp[3] in self.cords:
                return 'include'
            elif temp[0] in self.cords or temp[1] in self.cords:
                return 'overlap'
            else: 
                return 'not meet'
