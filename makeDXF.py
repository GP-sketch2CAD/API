import ezdxf
from ezdxf.document import Drawing

# color information 
# 1 = red -> 중심선
# 2 = yellow -> 기둥
# 3 = green -> 벽
# 4 = cyan -> 문, 창문
def drawDxf(doc: Drawing , cords: list, layerName: str, color: int):
    # 새로운 layer를 만들어서 그림
    # TODO: dxattribs 부분 수정할 것, linetype, color ...
    doc.layers.new(name=layerName, dxfattribs={'color':color})

    msp = doc.modelspace()

    # 리스트 순서대로 
    for i in range(0, len(cords)-1):
        msp.add_line(cords[i], cords[i+1], dxfattribs={'layer': layerName})





# Create a new DXF document.
doc = ezdxf.new(dxfversion='R2010')


cords = [(0,0),(10,0),(10,10),(0,10),(0,0)]
cordss = [(0,0),(100,0),(100,100),(0,100),(0,0)]

drawDxf(doc, cords, 'hoho', 3)
drawDxf(doc, cordss, 'window', 4)


# Save DXF document.
doc.saveas('test.dxf')

