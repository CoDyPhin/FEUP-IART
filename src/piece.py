class Center:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.content = color + "C"

class Piece:
    def __init__(self, x, y, destX, destY, color):
        self.x = x
        self.y = y
        self.destX = destX
        self.destY = destY
        self.color = color
        self.content = color + "P"

