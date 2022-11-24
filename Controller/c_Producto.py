from Model import *
from Database import *

class controllerProducto:
    @staticmethod
    def add_product(**kwargs):
        if(kwargs["tipo"] == 0):
            new_product = Antibiotico.create(kwargs["p_nombre"], kwargs["p_dosis"], kwargs["p_tipo"], kwargs["p_precio"])
        elif(kwargs["tipo"] == 1):
            new_product = ProductoControl.create(kwargs["p_ica"], kwargs["p_nombre"], kwargs["p_frecAp"], kwargs["p_precio"])
        elif(kwargs["tipo"] == 2):
            new_product = ProductoFertilizante.create(kwargs["p_ica"], kwargs["p_nombre"], kwargs["p_frecAp"], kwargs["p_precio"], kwargs["p_carencia"])
        elif(kwargs["tipo"] == 3):
            new_product = ProductoPlaga.create(kwargs["p_ica"], kwargs["p_nombre"], kwargs["p_frecAp"], kwargs["p_precio"], kwargs["p_uFechaAp"])

        Storage.save_product(new_product, kwargs["tipo"])
    
    @staticmethod
    def delete_product(nombre):
        Storage.delete_product(nombre)