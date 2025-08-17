class Material:
    def __init__(self, name: str = None, pricePerUnit: float = 0.0, width: float = 0.0, height: float = 0.0, hasGrain: bool = False,  idMaterial: int=None):
        self.name = name
        self.pricePerUnit = pricePerUnit
        self.width = width
        self.height = height
        self.hasGrain = hasGrain
        self.idMaterial = idMaterial
        self.area = self.width * self.height

    def __repr__(self):
        return (f"Material(Price=${self.pricePerUnit}, Width={self.width} cm, "
                f"Height={self.height} cm, HasGrain={self.hasGrain}, ID={self.idMaterial})")
