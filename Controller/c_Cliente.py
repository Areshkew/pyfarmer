from Model import *
from Database import *

class controllerCliente:
    @staticmethod
    def add_client(cedula, nombre, apellido):
        new_client = Cliente.create(cedula, nombre, apellido)
        Storage.save_client(new_client)
    
    @staticmethod
    def add_billTo_client(cedula, fecha, productos, total):
        new_bill = Factura.create(fecha, total)
        new_bill.relation(productos)

        if(not cedula in Storage.storage_clients):
            print("No se encontró la cedula en la base de datos...")
        else:
            Storage.storage_clients[cedula].relation(new_bill)

    @staticmethod
    def delete_client(cedula):
        Storage.delete_client(cedula)
    
    @staticmethod
    def update_client(cedula, nombre, apellido):
        new_client = Cliente.create(cedula, nombre, apellido)
        Storage.save_client(new_client)