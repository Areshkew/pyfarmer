from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from Controller import *
from Database import *

class QCliente:
    #Añadir clientes.
    def add_client(self):
        nombre = self.f_nombre.text()
        apellido = self.f_apellido.text()
        cedula = self.f_cedula.text()

        msg = QMessageBox()
        msg.setWindowTitle("¡ Alerta !")

        if((not nombre) or (not apellido) or (not cedula) or (cedula in Storage.get_clients())):
            msg.setText("¡ Tienes que rellenar todos los campos o el usuario ya existe! ")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        else:
            message = "¡ Se agrego a [" + cedula + ", " + nombre + ", " + apellido + "] !"
            msg.setText(message)
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
            self.reset_fields_client()
            controllerCliente.add_client(cedula, nombre, apellido)
            self.add_client_table( nombre, apellido, cedula ) 

    #Actualizar cliente.
    def update_client(self):
        nombre = self.f_nombre.text()
        apellido = self.f_apellido.text()
        cedula = self.f_cedula.text()

        msg = QMessageBox()
        msg.setWindowTitle("¡ Alerta !")

        if((not nombre) and (not apellido) and (not cedula) or ( not cedula in Storage.get_clients() )):
            msg.setText("¡ Tienes que rellenar todos los campos o el usuario no existe! ")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        else:
            message = "¡ Se actualizo a [" + cedula + ", " + nombre + ", " + apellido + "] !"
            msg.setText(message)
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
            self.reset_fields_client()
            controllerCliente.update_client(cedula, nombre, apellido)
            self.update_clients_table( Storage.get_clients() ) 

    #Eliminar Clientes
    def delete_client(self):
        cedula = self.f_bCedula.text()

        msg = QMessageBox()
        msg.setWindowTitle("¡ Alerta !")

        if((not cedula)):
            msg.setText("¡ Tienes que rellenar todos los campos ! ")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        else:
            if not cedula in Storage.get_clients():
                message = "No existe esta cedula en los usuarios..."
            else:
                message = "¡ Se elimino al usuario con cedula: " + cedula + "!"
                controllerCliente.delete_client(cedula)
                self.update_clients_table( Storage.get_clients() )

            msg.setText(message)
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
            self.reset_field_delete()

    #Reiniciar los campos para agregar cliente.
    def reset_fields_client(self): 
        self.f_nombre.clear()
        self.f_apellido.clear()
        self.f_cedula.clear()

    #Reiniciar campo borrar cliente
    def reset_field_delete(self):
        self.f_bCedula.clear()

    # Actualizar tabla de Clientes
    def update_clients_table(self, storage):
        self.table_clientes.setRowCount(0)
        for key, value in storage.items():
            rowPosition = self.table_clientes.rowCount()
            self.table_clientes.insertRow(rowPosition)
            self.table_clientes.setItem(rowPosition, 0, QTableWidgetItem( key ))
            self.table_clientes.setItem(rowPosition, 1, QTableWidgetItem( value.cliente_nombre ))
            self.table_clientes.setItem(rowPosition, 2, QTableWidgetItem( value.cliente_apellido ))
    
    # Agregar solo una persona a Tabla 
    def add_client_table(self, name, last_name, id):
        rowPosition = self.table_clientes.rowCount()
        self.table_clientes.insertRow(rowPosition)
        self.table_clientes.setItem(rowPosition, 0, QTableWidgetItem( id ))
        self.table_clientes.setItem(rowPosition, 1, QTableWidgetItem( name ))
        self.table_clientes.setItem(rowPosition, 2, QTableWidgetItem( last_name ))