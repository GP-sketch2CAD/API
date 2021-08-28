from object.base.blank import Blank

class Door():
    # TODO: 문 이동 경로도 생각해야하는데.... 어떻게 해야할지 고민을 더 해야함
    # attribute: 문에 사용되는 속성들
    # 카테고리는 값 수정 못하게 튜플로 하자
    NORMAL = 0
    TWODOOR = 1
    SLIDE = 2
    doorType = (NORMAL, TWODOOR, SLIDE)
    
    def __init__(self, blank: Blank, type = 0, direct = 0 ,frame = 50, doorT = 50) -> None:
        
        #super(Door, self).__init__(leftBot, rightTop, degree)
        
        # set attributes
       
        self.frame = frame
        self.doorT = doorT

        # normal_cw
        # if typeIdx == 0:
        #     # frame
        #     self.cordsList.append(cordsH.rectangle2cords((0,0), (frame, length)))
        #     self.cordsList.append(cordsH.rectangle2cords((width-frame, 0), (width, length)))
        #     # door
        #     temp = cordsH.rectangle2cords((0,0),(thickness,width-2*frame))
        #     temp = cordsH.moveCords(temp, frame, length)
        #     self.cordsList.append(temp)
        # # normal_ccw
        # elif typeIdx == 1:
        #     # frame
        #     self.cordsList.append(cordsH.rectangle2cords((0,0), (frame, length)))
        #     self.cordsList.append(cordsH.rectangle2cords((width-frame,0), (width,length)))
        #     # door
        #     temp = cordsH.rectangle2cords((0,0),(thickness,width-2*frame))
        #     temp = cordsH.moveCords(temp, width-frame-thickness, length)
        #     self.cordsList.append(temp)
        # # TODO: slide, twodoor 생각해서 추가해야함
        # else:  
        # pass
