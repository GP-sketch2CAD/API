from object.base.blank import BlankFunction
from object.base.cord import Cord
import copy

class Door:
    # TODO: 문 이동 경로 나중에 추가하기
    # TODO: 양문형, 슬라이드 나중에 추가하기

    NORMAL_LEFT = 0
    NORMAL_RIGHT = 1
    TWODOOR = 2
    SLIDE = 3
    
    def __init__(self, cord: Cord, degree: float, doorType, attr: dict) -> None:

        if doorType == self.NORMAL_LEFT:
            lines = self.D_normalLeft(garo= attr.get('garo'), sero= attr.get('sero'), 
                                            doke = attr.get('doke'), frame= attr.get('frame'))
        elif doorType == self.NORMAL_RIGHT:
            lines = self.D_normalRight(garo= attr.get('garo'), sero= attr.get('sero'), 
                                            doke = attr.get('doke'), frame= attr.get('frame'))

        self.lines = []
        for line in lines:
            ll = copy.deepcopy(line)
            ll.rotate(degree, 0, 0)
            ll.move(cord.x, cord.y)
            self.lines.append(ll)
    
    @staticmethod
    def D_normalLeft(garo: float, sero: float, doke: float, frame: float) -> list:
        lines = []
        doorL = garo - 2*frame
        lines += BlankFunction.nemo(Cord(0,0), Cord(frame, sero)).toLines()
        lines += BlankFunction.nemo(Cord(frame, sero), Cord(frame + doke, sero + doorL)).toLines()
        lines += BlankFunction.nemo(Cord(garo-frame, 0), Cord(garo, sero)).toLines()

        return lines

    @staticmethod
    def D_normalRight(garo: float, sero: float, doke: float, frame: float) -> list:
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
       

