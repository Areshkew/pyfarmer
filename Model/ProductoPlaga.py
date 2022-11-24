from .ProductoControl import *

class ProductoPlaga(ProductoControl):
    def __init__(self, ICAn, nombre, frec, valor, uFechaAp):
        ProductoControl.__init__(self, ICAn, nombre, frec, valor)
        self.pControl_ultimaFechaAp = uFechaAp

    @staticmethod
    def create(ICAn, nombre, frec, valor, uFechaAp):
        return ProductoFertilizante(ICAn, nombre, frec, valor, uFechaAp)
    
    def read():
        return self
    
    def relation():
        pass
