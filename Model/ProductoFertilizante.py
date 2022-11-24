from .ProductoControl import *

class ProductoFertilizante(ProductoControl):
    def __init__(self, ICAn, nombre, frec, valor, carencia):
        ProductoControl.__init__(self, ICAn, nombre, frec, valor)
        self.pControl_carencia = carencia

    @staticmethod
    def create(ICAn, nombre, frec, valor, carencia):
        return ProductoFertilizante(ICAn, nombre, frec, valor, carencia)
    
    def read():
        return self
    
    def relation():
        pass
