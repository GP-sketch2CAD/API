# 이건 건축요소 클래스들의 상위 클래스
from Handler import cordsHandler as cordsH

class ArctObject:
    """
    기본 건축 요소들의 상위 클래스
    문, 벽, 기둥, 계단, 창문이 공통으로 상속 받음

    Attribute-----------------
    cordsList: 좌표들을 저장하는 이중 리스트 [[(),()...], [], [] ...]
    leftBot, rightTop: 객체가 들어가야할 위치
    degree: 좌표들을 돌려야하는 각도

    객체를 돌리거나 옮기고 싶으면 좌표들을 수정하는 것이 아닌
    위치와 각도를 수정하면 됨
    """
    def __init__(self, leftBot: tuple, rightTop: tuple, degree = 0) -> None:
        self.cordsList = []
        self.leftBot = leftBot
        self.rightTop = rightTop
        self.degree = degree

        self.leftTop = (leftBot[0], rightTop[1])
        self.rightBot = (rightTop[0], leftBot[1])
       

    def getCordsList(self) -> list:
        """
        좌표들을 위치와 각도에 맞게 수정한 후 cordsList로 리턴

        return
        ------------
        list: cordsList 
        """

        d = self.degree % 360
        rotated = []
        if d != 0 :
            for cords in self.cordsList:
                rotated.append(cordsH.rotateCords(cords, d))
        else: rotated = self.cordsList
        
        # TODO: 돌리는게 좀 애매모호함 -> 나중에 한 번 더 확인하기
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