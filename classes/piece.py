class Piece:
    def __init__(self, width: float, height: float, isRotable: bool=True, idPiece: int=None):
        self.width = width
        self.height = height
        self.isRotable = isRotable
        self.idPiece = idPiece
        self.area = self.width * self.height

    
    def __repr__(self):
        return (f"Piece(width={self.width}, height={self.height}, "
                f"isRotable={self.isRotable}, idPiece={self.idPiece}, area={self.area})")
    
    def rotate(self):
        if self.isRotable:
            self.width, self.height = self.height, self.width

    