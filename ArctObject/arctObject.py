# 이건 건축요소 클래스들의 상위 클래스
import Handler.cordsHandler as crdh
class arctObject:
    def __init__(self) -> None:
        # 기본 좌표 위치를 이중 리스트로 기지고 있음
        self.cordsList = []

        # cordsList의 기준 위치와 각도
        # 객체의 움직이거나 돌려야 한다면 cordsList를 수정하는게 아니라
        # x, y, degree를 수정하면 됨
        self.x = 0
        self.y = 0
        self.degree = 0
       

    def convertCords(self) -> list:
        # x,y 만큼 좌표들을 옮기고
        # degree만큼 돌려주고
        moved = []
        for cords in self.cordsList:
            moved.append(crdh.moveCords(self.x, self.y, cords))
        
        converted = []
        for cords in moved:
            converted.append(crdh.rotateCords(self.degree, 0, 0, cords))
        
        return converted

    def move(self, x: int, y: int) -> tuple:
        """
        move object as x,y

        param
        -----------------
        x: move to x(not target, amount)
        y: move to y(not target, amount)

        return
        -----------------
        changed x,y value 

        """
        self.x += x
        self.y += y
        return (self.x, self,y)

    def rotate(self, degree: int) -> int:
        """
        rotate object as degree

        param
        -----------------
        degree: degree amount to rotate

        return
        -----------------
        changed degree 
        """
        self.degree += degree
        return self.degree 