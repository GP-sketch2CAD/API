import socket
import json
import sys
from os.path import exists
from handler.jsonInterpreter import JsonInterpreter
from handler.dxfHandler import DxfHandler


class Communicator:
    def __init__(self) -> None:
        self.hostIP = socket.gethostbyname(socket.gethostname())
        print(self.hostIP)

        self.port = 8080

        # socket communicate
        self.server_sock = socket.socket(socket.AF_INET)
        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_sock.bind((self.hostIP, self.port))
        self.server_sock.listen(1)

        self.jsonInter = JsonInterpreter()
        self.cadH = DxfHandler()

        self.json = None

    def getJsonSendDwg(self):
        while True:
            print("Wait to connect with client...")
            client_sock, addr = self.server_sock.accept()

            if client_sock:
                print("Connected by", addr)
                # 여기 부분에서 안드로이드->파이썬 json data를 가져와야함.
                data = bytearray(client_sock.recv(1024))[2:]
                self.jsonInter.loadJsonData(data)
                self.jsonInter.convert2Obj()

                self.cadH.drawJsonInter(self.jsonInter)
                self.cadH.saveDxf('Output', self.jsonInter.name + '.dxf')

                data_transferred = 0

                if not exists('Output'+'\\'+self.jsonInter.name + '.dxf'):
                    print("no file")
                    sys.exit()

                print('send dxf file')

                with open('Output'+'\\'+self.jsonInter.name + '.dxf', 'rb') as f:
                    try:
                        data = f.read(1024)  # 1024바이트 읽는다
                        while data:  # 데이터가 없을 때까지
                            # 1024바이트 보내고 크기 저장
                            data_transferred += client_sock.send(data)
                            data = f.read(1024)  # 1024바이트 읽음
                            print("전송완료 %s, 전송량 %d" %
                                  (self.jsonInter.name + '.dxf', data_transferred))

                    except Exception as ex:
                        print(ex)
                    finally:
                        break

        client_sock.close()
        self.server_sock.close()
