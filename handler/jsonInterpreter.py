import json
from object.architecture.column import SquareColumn
from object.architecture.door import Door
from object.architecture.wall import Wall
from object.architecture.window import Window
from object.base.cord import Cord

class JsonInterpreter:
    def __init__(self) -> None:
        self.wall = Wall([])
        self.doors = []
        self.windows = []
        self.columns = []
        self.stairs = []
        self.name = ""

    def loadJson(self, filename: str):
        with open(filename, 'r') as json_file:
            self.json = json.load(json_file)

    def loadJsonData(self, jsonData):
        self.json = json.loads(jsonData)

    def convert2Obj(self):
        self.name = self.json["name"]
        objs = self.json['arctObj']

        for obj in objs:
            if obj['type'] == 'nemoRoom':
                w = Wall([])
                w.setNemoRoom(leftBot= Cord(obj['leftBot'][0], obj['leftBot'][1]), 
                            rightTop=  Cord(obj['rightTop'][0],obj['rightTop'][1]), 
                            thickness= obj['thickness'])
                
                self.wall.appendWall(w)

        for obj in objs:  
            if obj['type'] == 'door':
                door = Door(Cord(obj['cord'][0],obj['cord'][1]), obj['degree'], obj['doorType'], obj['attr'])
                self.wall.breakWall(door.blank)
                self.doors.append(door)
            
            if obj['type'] == 'window':
                window = Window(Cord(obj['cord'][0],obj['cord'][1]), obj['degree'], obj['windowType'], obj['attr'])
                self.wall.breakWall(window.blank)
                self.windows.append(window)
            
            if obj['type'] == 'column':
                column = SquareColumn(leftBot=Cord(obj['leftBot'][0], obj['leftBot'][1]), 
                                    rigthTop= Cord(obj['rightTop'][0],obj['rightTop'][1]))
                self.columns.append(column)
