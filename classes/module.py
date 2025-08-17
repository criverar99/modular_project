from .piece import Piece
class Module:
    def __init__(self, name: str =None, idModule: int=None, pieces: list[Piece] = None):
        self.name = name
        self.idModule = idModule
        self.pieces = pieces if pieces is not None else []
        self.totalArea = sum(piece.area for piece in self.pieces)