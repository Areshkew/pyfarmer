from Interfaces import *

class Factura(ICrud):
    def __init__(self, fecha, total):
        self.factura_fecha = fecha
        self.factura_total = total
        self.factura_productos = []

    @staticmethod
    def create(fecha, total):
        return Factura(fecha, total)
    
    def read():
        return self
    
    def relation(self, nuevos_productos):
        if(len(nuevos_productos) == 0):
            raise Exception("Error no se encontraron productos.") 
        else:    
            for i in range(len(nuevos_productos)):
                self.factura_productos.append( nuevos_productos[i] )
