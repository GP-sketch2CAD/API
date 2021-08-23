from Handler import cordsHandler as cordH, cadHandler as cadH
from ArctObject import Door

def testRotate() -> None:
    box = cordH.rectangle2cords((0,0),(1,2))
    print(box)
    box = cordH.rotateCords(cords=box, degree=90)
    print('-------------change------------------')
    print(box)

def testMove()-> None:
    box = cordH.rectangle2cords((0,0),(1,2))
    print(box)
    box = cordH.moveCords(box,1,1)
    print('-------------change------------------')
    print(box)

def testDoorRotate() -> None:
    myDoor = door.Door((0,0),(1000,200))
    myDoor2 = door.Door((-1000,-200),(0,0),180)

    
    dxf = cadH.DxfHandler()
    dxf.drawLineCSL(myDoor.getCordsList(),dxf.LAYER_WINDOW)
    dxf.saveDxf('doortest.dxf')
    
#--------------------------------------------------

for i in range(0,5):
    if i == 2:
        i+=1
    print(i)
