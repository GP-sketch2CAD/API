from Handler import cordsHandler as cordH, cadHandler as cadH
from ArctObject import door, arctObject

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
    for m in myDoor.getCordsList():
        dxf.drawWall(m)
    for m in myDoor2.getCordsList():
        dxf.drawWall(m)

    dxf.saveDxf('doortest.dxf')
    
#--------------------------------------------------

testDoorRotate()
