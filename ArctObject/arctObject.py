# 이건 건축요소 클래스들의 상위 클래스
from Handler import cordsHandler as cordsH

class ArctObject:
    """
    클래스 변수(attribute) 설명
    leftBot, leftTop, rightTop, rightBot -> 객체가 캐드 상에서 차지할 공간
    cordsList: 그려야할 좌표리스트, 이걸 캐드상 표시에해야할 위치에 따라 돌리고 옮겨줘야함
    degree: 돌려줘야할 각도
    """
    def __init__(self, leftBot: tuple, rightTop: tuple, degree = 0) -> None:
        # 기본 좌표 위치를 이중 리스트로 기지고 있음
        self.cordsList = []

        # cordsList의 기준 위치와 각도
        # 객체의 움직이거나 돌려야 한다면 cordsList를 수정하는게 아니라
        # x, y, degree를 수정하면 됨
        self.leftBot = leftBot
        self.rightTop = rightTop
        self.degree = degree

        self.leftTop = (leftBot[0], rightTop[1])
        self.rightBot = (rightTop[0], leftBot[1])
       

    def getCordsList(self) -> list:

        # 1. 먼저 각도에 맞춰 돌리고
        # 2. 차지하는 공간이 차지할 공간이랑 일치하는지 확인
        # 3.0 일치하면 위치에 맞게 이동시켜줘
        # 3.1 불일치시 None 리턴

        d = self.degree % 360
        rotated = []
        if d != 0 :
            for cords in self.cordsList:
                rotated.append(cordsH.rotateCords(cords, d))
        else: rotated = self.cordsList
        
        # 돌리는게 좀 애매모호함
        if d < 90: 
            return rotated
        elif d < 180:
            m = self.rightBot
        elif d < 270:
            m = self.rightTop
        else:
            m = self.leftTop
        
        result = []
        for cords in rotated:
            result.append(cordsH.moveCords(cords, x = m[0],y = m[1]))
        return result