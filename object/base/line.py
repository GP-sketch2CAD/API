from numpy import isin
from cord import Cord

class Line:
    def __init__(self, start: Cord, end: Cord) -> bool:
        if start == end: return False
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
        # TODO: ... 추후개발
        if not isinstance(other, Line): 
            return False
    
    def getRelOnStraight(self, other) -> str:
        if not isinstance(other, Line): 
            return None
        elif self.getStraight() == other.getStraight():
            temp = self.cords + other.cords
            temp.sort(key= lambda x:(x[0], x[1]))
            
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
        

# class LineFunction:
#     @staticmethod
#     def isCCW(line: Line, cord: Cord) -> bool:
#         ccw = line.start.x*line.end.y + line.end.x*cord.y + cord.x*line.start.y - (line.end.x*line.start.y + cord.x*line.end.y + line.start.x*cord.y)
#         if ccw > 0: return True
#         else: return False

#     @staticmethod
#     def isCross(p: Line, q: Line) -> bool:
#         if p.straight == q.straight: return False
#         if LineFunction.isCCW(p.start, p.end, q.start) ^ LineFunction.isCCW(p.start, p.end, q.end):
#             if LineFunction.isCCW(q.start, q.end, p.start) ^ LineFunction.isCCW(q.start, q.end, p.end):
#                 return True
#         return False

#     @staticmethod
#     def isPcontainQ(p: Line, q: Line) -> bool:
#         if p.straight == q.straight: 
#             if (p.start.x <= q.start.x and p.end.x >= q.end.x and 
#                 p.start.y <= q.start.y and p.end.y >= q.end.y):
#                 return True
#         return False

#     @staticmethod
#     def isLcontainC(p: Line, c: Cord) -> bool:
#         if p.straight.a * c.x + p.straight.b * c.y + p.straight.c == 0:
#             if (p.end.x - c.x) * (c.x - p.start.x) >= 0:
#                 if (p.end.y - c.y) * (c.y - p.start.y) >= 0:
#                     return True
#         return False
    
#     @staticmethod
#     def isMeet(p: Line, q: Line) -> bool:
#         if p.straight == q.straight:
#             if (LineFunction.isLcontainC(p, q.start) or LineFunction.isLcontainC(p, q.end) or 
#                     LineFunction.isLcontainC(q, p.start) or LineFunction.isLcontainC(q, p.end)):
#                 return True
#         else: return False

#     @staticmethod
#     def isOnePointMeet(p: Line, q: Line) -> bool:
#         if p.straight == q.straight:
#             if p.start == q.end or p.end == q.start: return True
#         else: return False

#     @staticmethod
#     def getBetweenAngle(p: Line, q: Line) -> float:
#         """
#         get the angle between two lines
#         reference
#         -----
#         https://darkpgmr.tistory.com/121
#         """
#         if p.start == q.start:
#             a = (p.end.x-p.start.x, p.end.y - p.start.y)
#             b = (q.end.x-p.start.x, q.end.y - p.start.y)
#         elif p.start == q.end:
#             a = (p.end.x-p.start.x, p.end.y - p.start.y)
#             b = (q.start.x-p.start.x, q.start.y - p.start.y)
#         else: 
#             return None
        
#         son = a[0]*b[1] - a[1]*b[0]
#         mom = (a[0]**2 + a[1]**2)**0.5 * (b[0]**2 + b[1]**2)**0.5

#         return math.asin(son/mom)

 