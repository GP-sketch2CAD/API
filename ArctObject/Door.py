from ArctObject import arctObject
from Handler import cordsHandler as cordsH

class Door(arctObject.ArctObject):
    # TODO: 문 이동 경로도 생각해야하는데.... 어떻게 해야할지 고민을 더 해야함
    # attribute: 문에 사용되는 속성들
    # 카테고리는 값 수정 못하게 튜플로 하자
    types = ('normal_cw', 'normal_ccw', 'slide', 'double')
    
    def __init__(self, leftBot: tuple, rightTop: tuple, degree = 0, 
                    typeIdx = 0, width = 1000, length = 200 ,frame = 50, thickness = 50) -> None:
        
        super(Door, self).__init__(leftBot, rightTop, degree)
        
        # set attributes
        if 0 <= typeIdx and typeIdx < len(self.types): 
            self.typeIdx = typeIdx
        else: self.typeIdx = 0

        self.width = width
        self.length = length
        self.frame = frame
        self.thickness = thickness

        # normal_cw
        if typeIdx == 0:
            # frame
            self.cordsList.append(cordsH.rectangle2cords((0,0), (frame, length)))
            self.cordsList.append(cordsH.rectangle2cords((width-frame, 0), (width, length)))
            # door
            temp = cordsH.rectangle2cords((0,0),(thickness,width-2*frame))
            temp = cordsH.moveCords(temp, frame, length)
            self.cordsList.append(temp)
        # normal_ccw
        elif typeIdx == 1:
            # frame
            self.cordsList.append(cordsH.rectangle2cords((0,0), (frame, length)))
            self.cordsList.append(cordsH.rectangle2cords((width-frame,0), (width,length)))
            # door
            temp = cordsH.rectangle2cords((0,0),(thickness,width-2*frame))
            temp = cordsH.moveCords(temp, width-frame-thickness, length)
            self.cordsList.append(temp)
        # TODO: slide, twodoor 생각해서 추가해야함 
        
