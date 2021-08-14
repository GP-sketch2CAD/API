import Handler.cordsHandler as cordsH

class Door:
    ONE_DOOR = 'one door'
    def __init__(self, leftBot: tuple, rightTop: tuple, attrib: dict) -> None:
        self.leftBot = leftBot
        self.rightTop = rightTop
        
        if abs(leftBot[0] - rightTop[0]) > abs(leftBot[1] - rightTop[1]):
            self.short = abs(leftBot[1] - rightTop[1])
            self.long = abs(leftBot[0] - rightTop[0])
        else:
            self.long = abs(leftBot[1] - rightTop[1])
            self.short = abs(leftBot[0] - rightTop[0])

        # attribute
        # type: onedoor, slide, twodoor
        if attrib.get('type') != None: self.type = attrib.get('type')
        else : self.type = self.ONE_DOOR

        # direction: clock or counterclock
        if attrib.get('isCW'): self.isCW = True
        else: self.isCW = False

        # degree: 0, 90, 180, 270
        if attrib.get('degree') != None: self.degree = attrib.get('degree')
        else: self.degree = 0

        # door frame: default 50
        if attrib.get('frame') != None: self.frame = attrib.get('frame')
        else: self.frame = 50

        # door thickness: default 40
        if attrib.get('thickness') != None: self.thickness = attrib.get('thickness')
        else: self.thickness = 50


    def getCords(self) -> list:
        result = []

        leftFrame = [(0,0), (self.frame, 0), (self.frame, self.short), (0, self.short), (0,0)]
        rightFrame = cordsH.moveCords(self.long - self.frame, 0, leftFrame)
        door = [(0,0), (self.thickness,0), (self.thickness, self.long - 2*(self.frame)), (0, self.long - 2*(self.frame)), (0,0)]

        if self.isCW:
            door = cordsH.moveCords(self.frame, self.short, door)
        else:
            door = cordsH.moveCords(self.long - self.frame, self.short, door)
        

        return [leftFrame, door, rightFrame]