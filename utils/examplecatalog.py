import pandas as pd
from classes import Material
import os

class ExampleCatalog:
    def __init__(self):
        self.dfMaterialsCatalog = pd.read_csv(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'utils', 'materialsexample.csv')
        )
        self.MaterialsCatalog = self.getMaterialsCatalog()

    def getMaterialsCatalog(self) -> list[Material]:
        materials = []
        for _, row in self.dfMaterialsCatalog.iterrows():
            material = Material(
                idMaterial=row['idMaterial'],
                name=row['Code'],
                pricePerUnit=row['Price'],
                width=row['Width'],
                height=row['Height'],
                hasGrain=row['HasGrain'] == 'TRUE'
            )
            materials.append(material)
        return materials

    def findMaterialByName(self, name: str) -> Material | None:
        for material in self.MaterialsCatalog:
            if material.name == name:
                return material
        return None
