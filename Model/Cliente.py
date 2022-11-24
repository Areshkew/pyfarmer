from Interfaces import *

class Cliente(ICrud):
    def __init__(self, cedula, nombre, apellido):
        self.cliente_cedula = cedula
        self.cliente_nombre = nombre
        self.cliente_apellido = apellido
        self.cliente_facturas = []

    @staticmethod
    def create(cedula, nombre, apellido):
        return Cliente(cedula, nombre, apellido)
    
    def read(self):
        return self.cliente_facturas
    
    def relation(self, factura):
        self.cliente_facturas.append(factura)