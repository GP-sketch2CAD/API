from object.base.arc import Circle
from object.base.blank import BlankFunction
from object.architecture.wall import WallFunction
from object import *
from handler import *
import socket
from os.path import exists
import sys
import json
#--------------------------------------------------
'''
def Test_combine1() -> None:
    b = BlankFunction.nemo(Cord(0,0), Cord(100, 300))
    b2 = BlankFunction.nemo(Cord(100,0), Cord(200, 100))
    b3 = BlankFunction.nemo(Cord(100,200), Cord(200, 300))
    w = WallFunction.blank2Wall(b)
    w2 = WallFunction.blank2Wall(b2)
    w3 = WallFunction.blank2Wall(b3)

    cad = DxfHandler()

    WallFunction.combineWall(w, w2)
    WallFunction.combineWall(w,w3)
    cad.drawWall(w)
    cad.drawWall(w2)
    cad.drawWall(w3)
    cad.saveDxf('Output', 'sample2.dxf')

def Test_combine2() -> None:
    b = BlankFunction.nemo(Cord(0,0), Cord(100, 100))
    b2 = BlankFunction.nemo(Cord(100,0), Cord(200, 100))
    w = WallFunction.blank2Wall(b)
    w2 = WallFunction.blank2Wall(b2)
    
    cad = DxfHandler()

    WallFunction.combineWall(w, w2)
    cad.drawWall(w)
    cad.drawWall(w2)
    cad.saveDxf('Output', 'sample2.dxf')

def Test_makeNemoRoom() -> None:
    w = WallFunction.nemoRoom(Cord(0,0), Cord(1000, 1000), 200.)
    cad = DxfHandler()

    cad.drawWall(w)
    cad.saveDxf('Output', 'sample3.dxf')

def Test_makeBlank() -> None:
    w = WallFunction.nemoRoom(Cord(0,0), Cord(1000, 1000), 200.)
    cad = DxfHandler()
    b = BlankFunction.nemo(Cord(200,-200), Cord(400,0)) 
    
    WallFunction.makeBlank(w, b)
    cad.drawWall(w)
    cad.saveDxf('Output', 'sample3.dxf')

def Test_makeBlank2() -> None:
    b = BlankFunction.nemo(Cord(0,0), Cord(100, 1000))
    w = WallFunction.blank2Wall(b)

    cad = DxfHandler()
    b = BlankFunction.nemo(Cord(0, 200), Cord(100,300)) 
    
    WallFunction.makeBlank(w, b)
    cad.drawWall(w)
    cad.saveDxf('Output', 'sample3.dxf')

def Test_door() -> None:
    ar = {'garo': 1000., 'sero': 200., 'doke': 40., 'frame': 50.}
    d1 = Door(cord= Cord(0,0), degree= 0, doorType= Door.NORMAL_LEFT, attr= ar)
    d2 = Door(cord= Cord(1100,0), degree= 0, doorType= Door.NORMAL_RIGHT, attr= ar)
    d3 = Door(cord= Cord(0,0), degree= 90, doorType= Door.NORMAL_LEFT, attr= ar)

    cad = DxfHandler()
    cad.drawDoor(d1)
    cad.drawDoor(d2)
    cad.drawDoor(d3)

    cad.saveDxf('Output', 'sample4.dxf')

def Test_Circle() -> None:
    c = Circle(Cord(10,10), 10.)
    l = Line(Cord(0,0), Cord(10,10))

    cad = DxfHandler()
    cad.drawLine(l, DxfHandler.LAYER_CENTER)
    cad.drawCircle(c, DxfHandler.LAYER_CENTER)
    cad.saveDxf('Output', 'sample4.dxf')

def Test_Arc() -> None:
    arc = Arc(Cord(10,10), 10., 0, 180)
   

    cad = DxfHandler()
    cad.drawArc(arc, DxfHandler.LAYER_WINDOW)
    cad.saveDxf('Output', 'sample4.dxf')

def Test_readJson():
    jsonInter = JsonInterpreter()
    jsonInter.loadJson('test_house.json')
    print(jsonInter.json)
'''

def Test_readDraw(fileName):
    jsonInter = JsonInterpreter()
    jsonInter.loadJson(fileName)
    jsonInter.convert2Obj()

    cadH = DxfHandler()
    cadH.drawJsonInter(jsonInter)
    cadH.saveDxf('Output', fileName + '.dxf')

#--------------------------------------------

if __name__ =='__main__':
    # 서버 주소랑 포트번호
    host = '192.168.219.109'
    port = 8080

    #소켓 통신
    server_sock = socket.socket(socket.AF_INET)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_sock.bind((host, port))
    server_sock.listen(1)

    while True:
        print("기다리는 중")
        client_sock, addr = server_sock.accept()
        if client_sock:
            print("Connected by", addr)
            # 여기 부분에서 안드로이드->파이썬 json data를 가져와야함.
            '''
            data = bytearray(client_sock.recv(1024))[2:]
            info = json.loads(data)
            print("room count:", len(info))
            print(info['room']['X,Y'])
            print(info['body'])
            '''

            filename = "test_house.json"
            Test_readDraw(filename)

            data_transferred = 0

            if not exists('Output'+'\\'+filename + '.dxf'):
                print("no file")
                sys.exit()

            print("파일 %s 전송 시작" % 'Output'+'\\'+filename + '.dxf')

            with open('Output'+'\\'+filename + '.dxf', 'rb') as f:
                try:
                    data = f.read(1024)  # 1024바이트 읽는다
                    while data:  # 데이터가 없을 때까지
                        data_transferred += client_sock.send(data)  # 1024바이트 보내고 크기 저장
                        data = f.read(1024)  # 1024바이트 읽음
                        print("전송완료 %s, 전송량 %d" % (filename + '.dxf', data_transferred))
                except Exception as ex:
                    print(ex)

    client_sock.close()
    server_sock.close()