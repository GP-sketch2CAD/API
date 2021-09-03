from typing import Dict
import ezdxf
from object import *


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
    LAYER_DOOR = 'door'

    def __init__(self) -> None:
        # document를 생성
        self.doc = ezdxf.new(dxfversion='R2007', setup=True)        

        self.msp = self.doc.modelspace()

        # 필요한 layer를 생성
        # 중심선, 기둥선, 벽선, 창문선 순 
        # linetype document: https://ezdxf.readthedocs.io/en/stable/concepts/linetypes.html
        self.doc.layers.new(name= self.LAYER_CENTER, dxfattribs={'color': 1})
        self.doc.layers.new(name= self.LAYER_COLUMN, dxfattribs={'color': 2})
        self.doc.layers.new(name= self.LAYER_WALL, dxfattribs={'linetype': 'DASHED','color': 3})
        self.doc.layers.new(name= self.LAYER_WINDOW, dxfattribs={'color': 4})
        self.doc.layers.new(name= self.LAYER_DOOR, dxfattribs={'color': 4})
    
    
    def saveDxf(self, address: str, filename : str) -> None:
        self.doc.saveas(filename= address + '\\'+ filename)


    def drawLine(self, line: Line, layer: str) -> None:
        self.msp.add_line(line.start.toTuple(), line.end.toTuple(), dxfattribs={'layer':layer})
    
    def drawArc(self, arc: Arc, layer: str) -> None:
        self.msp.add_arc(arc.center.toTuple(), arc.radius, arc.startAngle, arc.endAngle, arc.isCCW, dxfattribs={'layer':layer})
    
    def drawCircle(self, circle: Circle, layer: str) -> None:
        self.msp.add_circle(circle.center.toTuple(), circle.radius, dxfattribs={'layer':layer})
            
    def drawWall(self, wall: Wall) -> None:
        for line in wall.lines:
            self.drawLine(line, self.LAYER_WALL)
        
    def drawDoor(self, door: Door) -> None:
       for line in door.lines:
           self.drawLine(line, self.LAYER_DOOR)

    def drawColumn(self, column: Column) -> None:
        if column.isCircle:
            self.drawCircle(column.circle, self.LAYER_COLUMN)
        else:
            for line in column.lines:
                self.drawLine(line, self.LAYER_COLUMN)
    
    def drawWindow(self, window: Window) -> None:
        for line in window.blank.toLines():
            self.drawLine(line, self.LAYER_WINDOW)
     
    #  ---------------------------------------- end dxfHandler ----------------------------------------

