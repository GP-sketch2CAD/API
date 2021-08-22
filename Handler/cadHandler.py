from typing import Dict
import ezdxf


# color information 
# 1 = red -> 중심선
# 2 = yellow -> 기둥
# 3 = green -> 벽
# 4 = cyan -> 문, 창문

# linetype information 
# https://ezdxf.readthedocs.io/en/stable/concepts/linetypes.html


# TODO: layer별로 선 타입을 다시 지정해줘야함

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


    def drawLine(self, cords: list, layer: str) -> None:
        for i in range(0, len(cords)-1):
            self.msp.add_line(cords[i], cords[i+1], dxfattribs={'layer':layer})
            
    def drawLineCSL(self, cordsList: list, layer: str) -> None:
        for cords in cordsList:
            self.drawLine(cords, layer)
   
     
    #  ---------------------------------------- end dxfHandler ----------------------------------------

