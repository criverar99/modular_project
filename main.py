from classes import Module, Piece, Material
from utils import ExampleCatalog

def main(): 
    exampleCatalog = ExampleCatalog()
    blancoArauco = exampleCatalog.findMaterialByName("Blanco Arauco")
    print(repr(blancoArauco))

if __name__ == "__main__":
    main()