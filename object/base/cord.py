class Cord:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        pass

    def __str__(self) -> str:
        return '({},{})'.format(self.x, self.y)

    def __eq__(self, o: object) -> bool:
        return (self.__class__ == o.__class__) and (self.x == o.x) and (self.y == o.y)

    def move(self, x = 0., y= 0.) -> None:
        """
        move cord by given x,y
        """
        self.x += x
        self.y += y
        pass