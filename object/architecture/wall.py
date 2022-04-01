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
        self._addLines(lines)
        self.arcs = []

    def __str__(self) -> str:
        return str(self.lines)

    def setNemoRoom(self, leftBot: Cord, rightTop: Cord, thickness: float):
        """
        set self lines as nemo room's wall
        """
        # inner nemo
        self._addLines(NemoBlank(leftBot, rightTop).toLines())

        # outer nemo
        out_leftBot = copy.deepcopy(leftBot)
        out_leftBot.move(-thickness, -thickness)
        out_rightTop = copy.deepcopy(rightTop)
        out_rightTop.move(thickness, thickness)
        self._addLines(NemoBlank(out_leftBot, out_rightTop).toLines())

    def appendWall(self, other) -> None:
        if not isinstance(other, Wall):
            return

        self._addCurveWall(other.arcs)
        self._addLines(other.lines)

    def breakWall(self, other) -> None:
        if not isinstance(other, Blank):
            return
        for ol in other.toLines():
            if not isinstance(ol, Line):
                continue
            to_remove = []
            to_add = []
            isAppendOL = True
            for line in self.lines:
                rel = ol.getRelOnStraight(line)
                if rel in [None, 'not meet', 'connect']:
                    continue
                elif rel == 'include':
                    to_remove.append(line)
                elif rel == 'overlap':
                    temp = ol.cords + line.cords
                    temp.sort(key = lambda x : (x.x, x.y))
                    if temp[0] in line.cords:
                        line.setLine([temp[0], temp[1]])
                    else:
                        line.setLine([temp[2], temp[3]])
                elif rel == 'be included':
                    temp = ol.cords + line.cords
                    temp.sort(key = lambda x : (x.x, x.y))
                    to_remove.append(line)
                    to_add.append(Line(temp[0], temp[1]))
                    to_add.append(Line(temp[2], temp[3]))
                
                isAppendOL = False
            
            for r in to_remove:
                self.lines.remove(r)
            for a in to_add:
                self.lines.append(a)
            if isAppendOL: self.lines.append(ol)
            

    def _addLines(self, lines: list) -> None:
        for line in lines:
            self.lines.append(line)
        self._arrangementLines()

    def _addCurveWall(self, arcs: list) -> None:
        for a in arcs:
            self.arcs.append(a)

    def _arrangementLines(self):
        """
        merge with minimal lines 
        """
        # merge line
        oldLines = self.lines
        newLines = []
        while oldLines:
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
                    four_cords.sort(key=lambda x: (x.x, x.y))
                    temp.setLine([four_cords[0], four_cords[3]])
                    oldLines.remove(o)
                    oldLines.append(temp)
                    toAdd = False
                    break

            if toAdd:
                newLines.append(temp)

        # split the line with cross point
        # oldLines = newLines
        # newLines = []
        # for a in oldLines:
        #     if not isinstance(a, Line):
        #         break
        #     cp_list = [a.cords[0], a.cords[1]]
        #     for b in oldLines:
        #         if a == b:
        #             continue
        #         if a.isCross(b):
        #             cp = a.getCrossPoint(b)
        #             if cp not in cp_list:
        #                 cp_list.append(cp)

        #     if len(cp_list) == 2:
        #         newLines.append(a)
        #     else:
        #         cp_list.sort(key=lambda x: (x.x, x.y))
        #         for i in range(len(cp_list)-1):
        #             newLines.append(Line(cp_list[i], cp_list[i+1]))

        # TODO:
        # remove the inner line

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
