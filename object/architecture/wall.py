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
        cords: 벽 내부의 꼭지점들 
        """
        self.lines = lines
        pass

    def addCurveWall(self, arcs: list) -> None:
        self.arcs = arcs
        pass

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
                if LineFunction.isOnePointMeet(one, two):
                    one + two
                    w2.lines.remove(two)
                elif LineFunction.isMeet(one, two):
                    beforeOne = copy.deepcopy(one)
                    if (one - two) == True:
                        popone.append(one)
                    if (two - beforeOne) == True:
                        poptwo.append(two)
                    
        
        for p in popone:
            w1.lines.remove(p)
        for p in poptwo:
            w2.lines.remove(p)
    
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

        


        

    
    