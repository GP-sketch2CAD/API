from typing import Dict
import ezdxf
from handler.jsonInterpreter import JsonInterpreter
from object import *
from object.architecture.column import SquareColumn


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
        self.doc.saveas(filename= address + '\\' +filename)
        


    def drawLine(self, line: Line, layer: str) -> None:
        # start = line.cords[0].getTuple()
        # end = line.cords[1].getTuple()
        self.msp.add_line(line.cords[0].getTuple(), line.cords[1].getTuple(), dxfattribs={'layer':layer})
    
    def drawArc(self, arc: Arc, layer: str) -> None:
        self.msp.add_arc(arc.center.getTuple(), arc.radius, arc.startAngle, arc.endAngle, arc.isCCW, dxfattribs={'layer':layer})
    
    def drawCircle(self, circle: Circle, layer: str) -> None:
        self.msp.add_circle(circle.center.getTuple(), circle.radius, dxfattribs={'layer':layer})
            

    def drawWall(self, wall: Wall) -> None:
        for line in wall.lines:
            self.drawLine(line, self.LAYER_WALL)
        
    def drawDoor(self, door: Door) -> None:
       for line in door.lines:
           self.drawLine(line, self.LAYER_DOOR)

    def drawSquareColumn(self, column: SquareColumn) -> None:
        # if column.isCircle:
        #     self.drawCircle(column.circle, self.LAYER_COLUMN)
        for line in column.lines:
            self.drawLine(line, self.LAYER_COLUMN)
    
    def drawWindow(self, window: Window) -> None:
        for line in window.lines:
            self.drawLine(line, self.LAYER_WINDOW)

    def drawJsonInter(self, jsonInter: JsonInterpreter):
        self.drawWall(jsonInter.wall)

        for d in jsonInter.doors:
            self.drawDoor(d)

        for w in jsonInter.windows:
            self.drawWindow(w)

        for c in jsonInter.columns:
            self.drawSquareColumn(c)
        
     
    #  ---------------------------------------- end dxfHandler ----------------------------------------

