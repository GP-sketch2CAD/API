class Column:
    def __init__(self, obj: object, isCircle: bool = False) -> None:
        self.isCircle = isCircle
        if isCircle:
            self.circle = obj
        else:
            self.lines = obj
        
    