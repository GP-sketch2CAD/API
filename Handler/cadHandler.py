import ezdxf


# color information 
# 1 = red -> 중심선
# 2 = yellow -> 기둥
# 3 = green -> 벽
# 4 = cyan -> 문, 창문

# linetype information 
# https://ezdxf.readthedocs.io/en/stable/concepts/linetypes.html


# TODO: layer별로 선 타입을 다시 지정해줘야함







#  ---------------------------------------- end function definition ----------------------------------------

# 이 클래스는 dxf를 다루기 위한 클래스
# 함수를 다 여기다 넣을 예정입니다
class DxfHandler:
    
    # str을 변수로 구현
    LAYER_CENTER = 'cen'
    LAYER_COLUMN = 'col'
    LAYER_WALL = 'wal'
    LAYER_WINDOW = 'wid'

    def __init__(self) -> None:
        # document를 생성
        self.doc = ezdxf.new(dxfversion='R2010')        

        self.msp = self.doc.modelspace()

        # 필요한 layer를 생성
        # 중심선, 기둥선, 벽선, 창문선 순 
        self.doc.layers.new(name= self.LAYER_CENTER, dxfattribs={'color': 1})
        self.doc.layers.new(name= self.LAYER_COLUMN, dxfattribs={'color': 2})
        self.doc.layers.new(name= self.LAYER_WALL, dxfattribs={'color': 3})
        self.doc.layers.new(name= self.LAYER_WINDOW, dxfattribs={'color': 4})
    
    
    def saveDxf(self, filename: str) -> None:

        self.doc.saveas(filename= filename)


    def drawWall(self, cords: list) -> None:
        
        # 좌료 리스트에 있는 좌표들을 순서대로 그림
        for i in range(0, len(cords)-1):
            self.msp.add_line(cords[i], cords[i+1], dxfattribs={'layer': self.LAYER_WALL})
            
        # self.msp.add_line(cordsList[len(cordsList)-1], cordsList[0], dxfattribs={'layer': self.LAYER_WALL})
   

    #  ---------------------------------------- end dxfHandler ----------------------------------------


# # How to use dxfHandler
# # Test and Example
# cords = [(0,0),(10,0),(10,10),(0,10),(0,0)]

# # dxfHander 생성
# handler = dxfHandler()

# # 벽과 창문 그리기
# handler.drawWall(cords)
# handler.drawWindow((100,100), (200,200))

# # 파일로 저장하기
# handler.saveDxf('test2.dxf')

# room_2 = [rectangle2cords((-100,-100),(3100,3100)), rectangle2cords((0,0),(3000,3000))]
# blank_2 = rectangle2cords((400,-100), (1400,0))

# # print(room_2)
# # print(blank_2)

# result = severCords(room_2, blank_2)
# print(result)
# handler = dxfHandler.dxfHandler()
# for re in result:
#     handler.drawWall(re)
# handler.saveDxf('test.dxf')
