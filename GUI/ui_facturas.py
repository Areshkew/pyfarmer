from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from Controller import *
from Database import *

class QFacturas:
    def __init__(self):
        self.product_list = []

    # Crear Factura
    def create_bill(self):
        cedula = self.form_Fced.text()
        fecha = self.form_Fdat.text()
        cantidad_prods = self.table_Fprods.rowCount()
        total = float(self.l_Ftotal.text())

        msg = QMessageBox()
        msg.setWindowTitle("¡ Alerta !")

        if( (not cedula in Storage.get_clients()) or (not cedula) ):
            msg.setText("No existe la cedula especificada.")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        elif(cantidad_prods == 0):
            msg.setText("No se han agregado productos.")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        else:
            msg.setText("Se creo la factura.")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

            controllerCliente.add_billTo_client(cedula, fecha, self.product_list, total)
            self.reset_bill_fields()

    # Añadir producto a factura
    def add_bill_product(self):
        product = self.form_Fprod.text()
        quantity = self.form_FprodQ.text()

        msg = QMessageBox()
        msg.setWindowTitle("¡ Alerta !")

        if( (not product in Storage.get_products()) or (not product) or (not quantity)):
            msg.setText("No existe el producto especificado o no has rellenado todos los campos.")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        else:
            msg.setText("Se agrego el producto.")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

            new_product = Storage.storage_products[product]
            self.add_prod_table(new_product, quantity)
            self.set_total(new_product, quantity)
            self.reset_addpro_fields()

            self.product_list.append( new_product )
            
    
    # Resetear todos los campos
    def reset_bill_fields(self):
        self.form_Fced.clear()
        self.reset_addpro_fields()
        self.product_list.clear()
        self.table_Fprods.setRowCount(0)
        self.l_Ftotal.setText( "0" )

    # Resetear campos
    def reset_addpro_fields(self):
        self.form_Fprod.clear()
        self.form_FprodQ.clear()

    # Añadir producto tabla
    def add_prod_table(self, product, quantity):
        rowPosition = self.table_Fprods.rowCount()
        if(isinstance(product, Antibiotico)):
            self.table_Fprods.insertRow(rowPosition)
            self.table_Fprods.setItem(rowPosition, 0, QTableWidgetItem( product.Antibiotico_nombre ))
            self.table_Fprods.setItem(rowPosition, 1, QTableWidgetItem( quantity ))
            self.table_Fprods.setItem(rowPosition, 2, QTableWidgetItem( str(product.Antibiotico_precio) ))
        else:
            self.table_Fprods.insertRow(rowPosition)
            self.table_Fprods.setItem(rowPosition, 0, QTableWidgetItem( product.pControl_nombre ))
            self.table_Fprods.setItem(rowPosition, 1, QTableWidgetItem( quantity ))
            self.table_Fprods.setItem(rowPosition, 2, QTableWidgetItem( str(product.pControl_valor) ))

    # Total factura
    def set_total(self, new_product, quantity):
        if(isinstance(new_product, Antibiotico)):
            total = float(self.l_Ftotal.text()) + (new_product.Antibiotico_precio * int(quantity))
        else:
            total = float(self.l_Ftotal.text()) + (new_product.pControl_valor * int(quantity))

        self.l_Ftotal.setText( str(total) )

    # LISTA FACTURAS
    def load_bills_data(self):
        self.table_facturas.setRowCount(0)
        for key, value in Storage.storage_clients.items():
            client_facturas = value.read()
            if( len(client_facturas) != 0 ):
                for i in range( len(client_facturas) ):
                    rowPosition = self.table_facturas.rowCount()
                    self.table_facturas.insertRow(rowPosition)
                    self.table_facturas.setItem(rowPosition, 0, QTableWidgetItem( value.cliente_cedula ))
                    self.table_facturas.setItem(rowPosition, 1, QTableWidgetItem( value.cliente_nombre ))
                    self.table_facturas.setItem(rowPosition, 2, QTableWidgetItem( value.cliente_apellido ))
                    self.table_facturas.setItem(rowPosition, 3, QTableWidgetItem( value.cliente_facturas[i].factura_fecha ))
                    self.table_facturas.setItem(rowPosition, 4, QTableWidgetItem( str(value.cliente_facturas[i].factura_total) ))

    # Click fila de factura    
    def click_row(self, selected):
        row_selected = selected.indexes()[0].row()
        ced = self.table_facturas.item(row_selected,0).text()
        info_cedula = "Cedula: " + self.table_facturas.item(row_selected,0).text()
        info_nombre = "Nombre: " +  self.table_facturas.item(row_selected,1).text()
        info_apellido = "Apellido: " +  self.table_facturas.item(row_selected,2).text()
        info_total = "Total de Factura: " +  self.table_facturas.item(row_selected,4).text()

        self.groupBox.setHidden(False)
        self.label_fname.setText(info_cedula)
        self.label_flastn.setText(info_nombre)
        self.label_ftotal.setText(info_apellido)
        self.label_fced.setText(info_total)
        self.bill_product_table(ced)
    
    # Tabla Productos
    def bill_product_table(self, cedula):
        self.table_fproductos.setRowCount(0)
        facturas = Storage.storage_clients[cedula].read()

        for i in range( len(facturas) ):
            factura = facturas[i].factura_productos
            for i in range( len(factura) ):
                rowPosition = self.table_fproductos.rowCount()
                self.table_fproductos.insertRow(rowPosition)
                if(isinstance(factura[i], Antibiotico)):
                    self.table_fproductos.setItem(rowPosition, 0, QTableWidgetItem( factura[i].Antibiotico_nombre ))
                    self.table_fproductos.setItem(rowPosition, 1, QTableWidgetItem( type(factura[i]).__name__ ))
                    self.table_fproductos.setItem(rowPosition, 2, QTableWidgetItem( str(factura[i].Antibiotico_precio) ))
                else:
                    self.table_fproductos.setItem(rowPosition, 0, QTableWidgetItem( factura[i].pControl_nombre ))
                    self.table_fproductos.setItem(rowPosition, 1, QTableWidgetItem( type(factura[i]).__name__ ))
                    self.table_fproductos.setItem(rowPosition, 2, QTableWidgetItem( str(factura[i].pControl_valor) ))

