from Interfaces import *

class ProductoControl(ICrud):
    def __init__(self, ICAn, nombre, frec, valor):
        self.pControl_ICA = ICAn
        self.pControl_nombre = nombre
        self.pControl_frec = frec
        self.pControl_valor = valor + (valor * ICAn) 

    @staticmethod
    def create(ICAn, nombre, frec, valor):
        return ProductoControl(ICAn, nombre, frec, valor)
    
    def read():
        return self
    
    def relation():
        pass