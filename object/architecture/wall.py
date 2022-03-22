from object.base.cord import Cord
from object.base.line import Line
from object.base.blank import Blank,  NemoBlank
from object.base.arc import Arc
import copy

class Wall:
    def __init__(self, lines: list) -> None:
        """
        """
        self.lines = []
        self.addLines(lines)
        self.arcs = []

    def __str__(self) -> str:
        return str(self.lines)

    def setNemoRoom(self, leftBot: Cord, rightTop: Cord, thickness: float):
        """
        set self lines as nemo room's wall
        """
        # inner nemo
        self.addLines(NemoBlank(leftBot,rightTop).toLines())
        
        # outer nemo
        leftBot.move(-thickness,-thickness)
        rightTop.move(thickness,thickness)
        self.addLines(NemoBlank(leftBot,rightTop).toLines())

    def addCurveWall(self, arcs: list) -> None:
        for a in arcs:
            self.arcs.append(a)
    
    def addLines(self, lines: list) -> None:
        for line in lines:
            self.lines.append(line)
        self._mergeLines()

    def appendWall(self, other) -> None:
        if not isinstance(other, Wall): return
        
        self.addCurveWall(other.arcs)
        self.addLines(other.lines)

    def _mergeLines(self):
        """
        merge with minimal lines 
        """
        # 같은 직선 상에 있는 선분들 정리 (연결 혹은 제거)
        oldLines = self.lines
        newLines = []
        while not oldLines:
            temp = oldLines.pop()
            if not isinstance(temp, Line) or temp.cords[0] == temp.cords[1]:
                continue

            toAdd = True
            for o in oldLines:
                rel = temp.getRelOnStraight(o)
                if rel in [None, 'not meet']: 
                    continue
                else:
                    four_cords = temp.cords + o.cords
                    four_cords.sort(key = lambda x: (x[0], x[1]))
                    if rel == 'connect':
                        temp.setLine([four_cords[0], four_cords[3]])
                        oldLines.remove(o)
                        oldLines.append(temp)
                        toAdd = False
                        break
                    else: # [include, be included, overlap]
                        temp.setLine([four_cords[2], four_cords[3]])
                        o.setLine([four_cords[0], four_cords[1]])
                        oldLines.append(temp)
                        toAdd = False
                        break
                
            if toAdd:
                newLines.append(temp)

        # TODO: 내부에 있는 쓰잘데기 없는 선분 지우기
        # 교차점을 구해서 라인을 나누고
        # 링크드 리스트처럼 연결하고
        # 점의 내외부 계산해서 쓸데 없는 것 지우기
        self.lines = newLines
        

    

# class WallFunction:
#     def blank2Wall(blank: Blank) -> Wall:
#         lines = []
#         cords = blank.cords
#         a = lines.append
#         for i in range(0, len(cords)-1):
#             a(Line(cords[i], cords[i+1]))
#         a(Line(cords[len(cords)-1], cords[0]))

#         return Wall(lines=lines)
    
    

#     def combineWall(w1: Wall, w2: Wall):
#         popone = []
#         poptwo = []
#         for one in w1.lines:
#             for two in w2.lines:
#                 # 한 점에서 만나는 경우
#                 if LineFunction.isOnePointMeet(one, two):
#                     one + two
#                     w2.lines.remove(two)
#                 # 선이 겹치는 경우
#                 elif LineFunction.isMeet(one, two):
#                     if LineFunction.isPcontainQ(one, two):
#                         w2.lines.remove(two)
#                     elif LineFunction.isPcontainQ(two, one):
#                         w1.lines.remove(one)
#                     else:
#                         one - two
#                         one + two
#                         w2.lines.remove(two)
#                 # 선이 크로스되는 경우
    

#     # 라인 빼고 더하는 부분 수정해야함
#     def makeBlank(wall: Wall, blank: Blank):
#         for bl in blank.toLines():
#             isChange = False
#             poplist = []
#             for wl in wall.lines:
#                 if LineFunction.isPcontainQ(wl,bl):
#                     isChange = True
#                     if wl.start == bl.start or wl.end == bl.end: 
#                         if wl - bl == True:
#                             poplist.append(wl)
#                     else:
#                         wall.lines.append(Line(bl.end, wl.end))
#                         wl.end = bl.start
                        
#                 elif LineFunction.isMeet(bl, wl):
#                     isChange = True
#                     wl - bl
#             for pl in poplist:
#                 wall.lines.remove(pl)
#             if isChange == False:
#                 wall.lines.append(bl)

        


        

    
    