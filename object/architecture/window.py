import copy
from object.base.blank import Blank, NemoBlank
from object.base.cord import Cord
from object.base.line import Line
from object.base.blank import Blank


class Window:

    BASIC_TYPE = 0

    def __init__(self, cord: Cord, degree: float, windowType, attr: dict) -> None:

        self.outerCords = []

        if windowType == self.BASIC_TYPE:
            temp_lines = self.W_base(garo= attr.get('garo'), sero= attr.get('sero'), 
                                    frame_garo = attr.get('frame_garo'), frame_sero= attr.get('frame_sero'))
       
        for c in self.outerCords:
            c.rotate(degree)
        dx, dy = self.getOuterLBCord()

        self.lines = []
        for line in temp_lines:
            ll = copy.deepcopy(line)
            ll.rotate(degree, 0, 0)
            ll.move(cord.x - dx, cord.y - dy)
            self.lines.append(ll)

        self.blank.rotate(degree)
        self.blank.move(cord.x - dx, cord.y - dy)
        pass

    def W_base(self, garo: float, sero: float, frame_garo: float, frame_sero: float) -> list:

        self.setOuterCords([[0,0], [0,sero], [garo,0], [garo,sero]])
        self.blank = NemoBlank(Cord(0,0), Cord(garo, sero))


        lines = []
        dy = (sero - frame_sero)/2
        lines += NemoBlank(Cord(0, dy),
                                    Cord(frame_garo, dy+frame_sero)).toLines()
        lines += NemoBlank(Cord(garo-frame_garo, dy),
                                    Cord(garo, dy+frame_sero)).toLines()

        lines.append(Line(Cord(frame_garo, dy), Cord(garo-frame_garo, dy)))
        lines.append(Line(Cord(frame_garo, sero/2),
                     Cord(garo-frame_garo, sero/2)))
        lines.append(Line(Cord(frame_garo, dy+frame_sero),
                     Cord(garo-frame_garo, dy+frame_sero)))

        return lines

    def setOuterCords(self, cords: list):
        for c in cords:
            self.outerCords.append(Cord(c[0],c[1]))

    def getOuterLBCord(self):
        min_y = None
        min_x = None

        for c in self.outerCords:
            if min_y == None or min_y > c.y:
                min_x = c.x
                min_y = c.y
            elif min_y == c.y and min_x > c.x:
                min_x = c.x
                min_y = c.y
        
        return min_x, min_y