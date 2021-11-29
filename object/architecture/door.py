from object.base.blank import Blank, BlankFunction
from object.base.cord import Cord, CordFunction
import copy

class Door:
    # TODO: 문 이동 경로 나중에 추가하기
    # TODO: 양문형, 슬라이드 나중에 추가하기

    NORMAL_LEFT = 0
    NORMAL_RIGHT = 1
    TWODOOR = 2
    SLIDE = 3
    
    def __init__(self, cord: Cord, degree: float, doorType, attr: dict) -> None:
        
        self.outerCords = []
        

        if doorType == self.NORMAL_LEFT:
            temp_lines = self.D_normalLeft(garo= attr.get('garo'), sero= attr.get('sero'), 
                                            doke = attr.get('doke'), frame= attr.get('frame'))
        elif doorType == self.NORMAL_RIGHT:
            temp_lines = self.D_normalRight(garo= attr.get('garo'), sero= attr.get('sero'), 
                                            doke = attr.get('doke'), frame= attr.get('frame'))



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
   
    def D_normalLeft(self, garo: float, sero: float, doke: float, frame: float) -> list:
        self.setOuterCords([[0,0], [0,sero], [garo,0], [garo,sero]])
        self.blank = BlankFunction.nemo(Cord(0,0), Cord(garo, sero))


        lines = []
        doorL = garo - 2*frame
        lines += BlankFunction.nemo(Cord(0,0), Cord(frame, sero)).toLines()
        lines += BlankFunction.nemo(Cord(frame, sero), Cord(frame + doke, sero + doorL)).toLines()
        lines += BlankFunction.nemo(Cord(garo-frame, 0), Cord(garo, sero)).toLines()

        return lines

    
    def D_normalRight(self, garo: float, sero: float, doke: float, frame: float) -> list:
        self.setOuterCords([[0,0], [0,sero], [garo,0], [garo,sero]])
        self.blank = BlankFunction.nemo(Cord(0,0), Cord(garo, sero))

        lines = []
        doorL = garo - 2*frame
        lines += BlankFunction.nemo(Cord(0,0), Cord(frame, sero)).toLines()
        lines += BlankFunction.nemo(Cord(garo-frame-doke, sero), Cord(garo - frame, sero + doorL)).toLines()
        lines += BlankFunction.nemo(Cord(garo-frame, 0), Cord(garo, sero)).toLines()

        return lines

    @staticmethod
    def D_twodoor() -> list:
        pass

    @staticmethod
    def D_slide() -> list:
        pass
       
    
    def setOuterCords(self, cords: list):
        for c in cords:
            self.outerCords.append(CordFunction.list2cord(c))

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