from ArctObject import ArctObject
from Handler import cordsHandler as cordsH

class Wall(ArctObject.ArctObject):
    # 이 클래스는  csl(cordslist)이 총 3가지가 있다
    # csl, blankcsl, centercsl이 있다
    # csl은 벽을 구성할 하위 벽들의 집합
    # blankcls은 벽에 구멍을 뚫어야하는 위치 -> 문이나 창문이 들어가야하는 위치
    # centercls는 중심선을 그어줘야하는 위치이다
    def __init__(self, leftBot: tuple, rightTop: tuple, degree, cordsList: list, blankCordsList: list) -> None:
        super(Wall, self).__init__(leftBot, rightTop, degree=degree)

        self.blankCSL = blankCordsList
        self.centerCSL = []
        self.cordsList = cordsList
        
    def getCordsList(self) -> list:
        #1. 먼저 합칠 것 합치고

        for eumCords in enumerate(self.cordsList):
            for i in range(0, len(eumCords)-1):
                base1 = eumCords[1][i]
                base2 = eumCords[1][i+1]
            
                for targetIdx in range(eumCords[0]+1, len(self.cordsList)):
                    targetCords = self.cordsList[targetIdx]
                    for j in range(0, len(targetCords)-1):
                        target1 = targetCords[j]
                        target2 = targetCords[j+1]
                        if cordsH.isPointOnLine(base1, base2, target1):
                            # 여기서 해결봐야함
                            pass
             


        #2. 빵구 뚫은거 뚫어주고
        return super().getCordsList()
    
    def getCenterCordsList(self) -> list:
        pass

    def getCenterCordsList(self) -> list:
        pass