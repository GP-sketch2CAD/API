import json
from object.architecture.column import SquareColumn
from object.architecture.door import Door
from object.architecture.wall import Wall, WallFunction
from object.architecture.window import Window
from object.base.blank import BlankFunction
from object.base.cord import Cord, CordFunction

class JsonInterpreter:
    def __init__(self) -> None:
        self.wall = Wall([])
        self.doors = []
        self.windows = []
        self.columns = []
        self.stairs = []

    def loadJson(self, filename: str):
        with open(filename, 'r') as json_file:
            self.json = json.load(json_file)
    
    def convert2Obj(self):
        objs = self.json['arctObj']

        for obj in objs:
            if obj['type'] == 'nemoRoom':
                w = WallFunction.nemoRoom(CordFunction.list2cord(obj['leftBot']), 
                                        CordFunction.list2cord(obj['rightTop']), 
                                        obj['thickness'])
                self.wall.lines = self.wall + w
            
            if 'door' in obj:
                o = obj['door']
                door = Door(CordFunction.list2cord(o['cord']), o['degree'], o['doorType'], o['attr'])
                WallFunction.makeBlank(self.wall, door.blank)
                self.doors.append(door)
            
            if 'window' in obj:
                o = obj['window']
                window = Window(CordFunction.list2cord(o['cord']), o['degree'], o['windowType'], o['attr'])
                WallFunction.makeBlank(self.wall, window.blank)
                self.windows.append(window)
            
            if 'column' in obj:
                o = obj['column']
                if o['type'] == 'square':
                    column = SquareColumn(CordFunction.list2cord(o['leftBot']), CordFunction.list2cord(o['rightTop']))
                    self.columns.append(column)


