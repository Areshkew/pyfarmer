from Model import *

class Storage(object):
    storage_clients = {}
    storage_products = {}

    # CLIENTES
    @staticmethod
    def save_client(new_client):
        if(not isinstance(new_client, Cliente)):
            print("Solo es posible agregar Clientes...")
        
        Storage.storage_clients.update({new_client.cliente_cedula: new_client})
    
    @staticmethod
    def delete_client(cedula):
        if(not cedula in Storage.storage_clients):
            print("No existe el cliente")
            return
        
        Storage.storage_clients.pop(cedula)
        
    @staticmethod
    def get_clients():
        return Storage.storage_clients

    # PRODUCTOS
    @staticmethod 
    def save_product(new_product, type):
        if(type == 0):
            Storage.storage_products.update({new_product.Antibiotico_nombre: new_product})
        else:
            Storage.storage_products.update({new_product.pControl_nombre: new_product})
            
    @staticmethod
    def get_products():
        return Storage.storage_products

    @staticmethod
    def delete_product(nombre):
        if(not nombre in Storage.storage_products):
            print("No existe el cliente")
            return
        
        Storage.storage_products.pop(nombre)