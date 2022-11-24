from Interfaces import *

class Antibiotico(ICrud):
    def __init__(self, nombre, dosis, tipoAnimal, valor):
        self.Antibiotico_nombre = nombre
        self.Antibiotico_dosis = dosis
        self.Antibiotico_tipoAnimal = tipoAnimal
        self.Antibiotico_precio = valor

    @staticmethod
    def create(nombre, dosis, tipoAnimal, precio):
        return Antibiotico(nombre, dosis, tipoAnimal, precio)
    
    def read():
        return self
    
    def relation():
        pass