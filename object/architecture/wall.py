from object.base.cord import Cord
from object.base.line import Line, LineFunction
from object.base.blank import Blank
from object.base.arc import Arc

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
        leftTop = Cord(leftBot.x, rightTop.y)
        rightBot = Cord(rightTop.x, leftBot.y)
        
        inner = [leftBot, rightBot, rightTop, leftTop, leftBot]
        lines = []
        for i in range(0,4):
            lines.append(Line(inner[i], inner[i+1]))
        
        t = thickness
        outer = [leftBot.move(-t,-t), rightBot.move(t,-t), rightTop.move(t,t), leftTop.move(-t,t), leftBot.move(-t,-t)]
        for i in range(0,4):
            lines.append(Line(outer[i], outer[i+1]))
        
        return Wall(lines=lines)

    def combineWall(w1: Wall, w2: Wall):
        for one in w1.lines:
            for two in w2.lines:
                if LineFunction.isMeet(one, two):
                    one - two
                    two - one
    
    def makeBlank(wall: Wall, blank: Blank):
        for bl in blank.toLines():
            for wl in wall.lines:
                if LineFunction.isPcontainQ(wl,bl):
                    if wl.start == bl.start and wl.end != bl.end: 
                        wl - bl
                    else: 
                        wl.end = bl.start
                        wall.lines.append(Line(bl.end, wl.end))
                elif LineFunction.isMeet(bl, wl):
                    wl - bl
                else:
                    wall.lines.append(bl)

        


        

    
    