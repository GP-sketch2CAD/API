from object.base.cord import Cord
from object.base.line import Line, LineFunction
from object.base.blank import Blank, BlankFunction
from object.base.arc import Arc
import copy

class Wall:
    def __init__(self, lines: list) -> None:
        """
        param
        -------

        """
        self.lines = lines
        
    
    
    def addCurveWall(self, arcs: list) -> None:
        self.arcs = arcs
        

    def __add__(self, other):
        if isinstance(other, Wall):
            WallFunction.combineWall(self, other)
            return self.lines + other.lines

    def __str__(self) -> str:
        return str(self.lines)

class WallFunction:
    def blank2Wall(blank: Blank) -> Wall:
        lines = []
        cords = blank.cords
        a = lines.append
        for i in range(0, len(cords)-1):
            a(Line(cords[i], cords[i+1]))
        a(Line(cords[len(cords)-1], cords[0]))

        return Wall(lines=lines)
    
    def nemoRoom(leftBot: Cord, rightTop: Cord, thickness: float) -> Wall:
        b1 = BlankFunction.nemo(leftBot, rightTop)

        outLB = Cord(leftBot.x - thickness, leftBot.y - thickness)
        outRT = Cord(rightTop.x + thickness, rightTop.y + thickness)
        b2 = BlankFunction.nemo(outLB, outRT)

        lines = b1.toLines() + b2.toLines()
        
        return Wall(lines=lines)

    def combineWall(w1: Wall, w2: Wall):
        popone = []
        poptwo = []
        for one in w1.lines:
            for two in w2.lines:
                # 한 점에서 만나는 경우
                if LineFunction.isOnePointMeet(one, two):
                    one + two
                    w2.lines.remove(two)
                # 선이 겹치는 경우
                elif LineFunction.isMeet(one, two):
                    if LineFunction.isPcontainQ(one, two):
                        w2.lines.remove(two)
                    elif LineFunction.isPcontainQ(two, one):
                        w1.lines.remove(one)
                    else:
                        one - two
                        one + two
                        w2.lines.remove(two)
                # 선이 크로스되는 경우
    

    # 라인 빼고 더하는 부분 수정해야함
    def makeBlank(wall: Wall, blank: Blank):
        for bl in blank.toLines():
            isChange = False
            poplist = []
            for wl in wall.lines:
                if LineFunction.isPcontainQ(wl,bl):
                    isChange = True
                    if wl.start == bl.start or wl.end == bl.end: 
                        if wl - bl == True:
                            poplist.append(wl)
                    else:
                        wall.lines.append(Line(bl.end, wl.end))
                        wl.end = bl.start
                        
                elif LineFunction.isMeet(bl, wl):
                    isChange = True
                    wl - bl
            for pl in poplist:
                wall.lines.remove(pl)
            if isChange == False:
                wall.lines.append(bl)

        


        

    
    