from . import arctObject
from Handler import cordsHandler as cordsH

class Wall(arctObject.ArctObject):
    def __init__(self, leftBot: tuple, rightTop: tuple, degree, cordsList: list, blankCordsList: list) -> None:
        super(Wall, self).__init__(leftBot, rightTop, degree=degree)

        self.blankCSL = blankCordsList
        self.centerCSL = []
        self.cordsList = cordsList
        
    def getCordsList(self) -> list:
        #1. 먼저 합칠 것 합치고
        #2. 빵구 뚫은거 뚫어주고
        return super().getCordsList()

    def getCenterCordsList(self) -> list:
        pass