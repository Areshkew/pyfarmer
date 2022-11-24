from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from Controller import *
from Database import *

class QProductos:
    #Añadir productos.
    def add_product(self):
        msg = QMessageBox()
        msg.setWindowTitle("¡ Alerta !")
        tipo_producto = self.stacked_productos.currentIndex()

        if(tipo_producto == 0): # Página Antibioticos
            nombre = self.form_antNombre.text()
            dosis = self.form_dosis.text()
            tipo = self.form_animal.currentText()
            precio = int( self.form_precio.text() )
            if((not nombre) or (not dosis) or (not precio) or (tipo == 'Escoge una opción...') or ( nombre in Storage.get_products() )):
                msg.setText("¡ Tienes que rellenar todos los campos o el producto ya existe! ")
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()
            else:
                message = "¡ Se agrego el nuevo antibiotico: [" + nombre + "] !"
                msg.setText(message)
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()
                self.reset_fields_products()
                controllerProducto.add_product(tipo = tipo_producto, p_nombre = nombre, p_dosis = dosis, p_tipo = tipo, p_precio = precio)
                self.add_antibiotic_table( p_nombre = nombre, p_dosis = dosis, p_tipo = tipo, p_precio = precio ) 

        elif(tipo_producto == 1): # Página Producto Control
            ica = float( self.form_ICA.text() )
            nombre = self.form_nombrePro.text()
            precio = int( self.form_precioP.text() )
            frecAp = self.form_frec.text()
            if((not ica) or (not nombre) or (not precio)  or (not frecAp) or ( nombre in Storage.get_products() )):
                msg.setText("¡ Tienes que rellenar todos los campos o el producto ya existe! ")
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()
            else:
                message = "¡ Se agrego el nuevo producto de control: [" + nombre + "] !"
                msg.setText(message)
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()
                self.reset_fields_products()
                controllerProducto.add_product(tipo = tipo_producto, p_ica = ica, p_nombre = nombre, p_precio = precio, p_frecAp = frecAp)
                self.add_pc_table( p_ica = ica, p_nombre = nombre, p_precio = precio, p_frecAp = frecAp ) 

        elif(tipo_producto == 2): # Página Producto Fertilizante
            ica = float( self.form_ICA_2.text() )
            nombre = self.form_nombrePro_2.text()
            precio = int( self.form_precioP_2.text() )
            frecAp = self.form_frec_2.text()
            carencia = self.form_carencia.text()
            if((not ica) or (not nombre) or (not precio) or (not frecAp) or (not carencia) or ( nombre in Storage.get_products() )):
                msg.setText("¡ Tienes que rellenar todos los campos o el producto ya existe! ")
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()
            else:
                message = "¡ Se agrego el nuevo producto de control: [" + nombre + "] !"
                msg.setText(message)
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()
                self.reset_fields_products()
                controllerProducto.add_product(tipo = tipo_producto, p_ica = ica, p_nombre = nombre, p_precio = precio, p_frecAp = frecAp, p_carencia = carencia)
                self.add_pc_table( p_ica = ica, p_nombre = nombre, p_precio = precio, p_frecAp = frecAp ) 

        elif(tipo_producto == 3): # Página Producto Plaga
            ica = float( self.form_ICA_3.text() )
            nombre = self.form_nombrePro_3.text()
            precio = int( self.form_precioP_3.text() )
            frecAp = self.form_frec_3.text()
            ultimaFechaAp = self.form_ultimaFechaAp.text()
            if((not ica) or (not nombre) or (not precio) or (not frecAp) or (not carencia) or ( nombre in Storage.get_products() )):
                msg.setText("¡ Tienes que rellenar todos los campos o el producto ya existe! ")
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()
            else:
                message = "¡ Se agrego el nuevo producto de control: [" + nombre + "] !"
                msg.setText(message)
                msg.setIcon(QMessageBox.Information)
                x = msg.exec_()
                self.reset_fields_products()
                controllerProducto.add_product(tipo = tipo_producto, p_ica = ica, p_nombre = nombre, p_precio = precio, p_frecAp = frecAp, p_uFechaAp = ultimaFechaAp)
                self.add_pc_table( p_ica = ica, p_nombre = nombre, p_precio = precio, p_frecAp = frecAp ) 

    #Eliminar Productos
    def delete_product(self):
        nombre = self.form_eProd.text()

        msg = QMessageBox()
        msg.setWindowTitle("¡ Alerta !")

        if((not nombre)):
            msg.setText("¡ Tienes que rellenar todos los campos ! ")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        else:
            if not nombre in Storage.get_products():
                message = "No existe este producto en la base de datos..."
            else:
                message = "¡ Se elimino el producto nombre: " + nombre + "!"
                controllerProducto.delete_product(nombre)
                self.update_product_tables( Storage.get_products() )

            msg.setText(message)
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
            self.reset_field_deleteP()

    #Reiniciar los campos para agregar cliente.
    def reset_field_deleteP(self): 
        self.form_eProd.clear()

    #Reiniciar los campos para agregar cliente.
    def reset_fields_products(self): 
        tipo_producto = self.stacked_productos.currentIndex()
        if( tipo_producto == 0): # Página Antibiotico
            self.form_antNombre.clear()
            self.form_dosis.clear()
            self.form_animal.setCurrentIndex(0)
            self.form_precio.clear()
        elif( tipo_producto == 1): # Página Producto Control
            self.form_ICA.clear()
            self.form_nombrePro.clear()
            self.form_precioP.clear()
            self.form_frec.clear()
        elif( tipo_producto == 2): # Página Producto Fertilizante
            self.form_ICA_2.clear()
            self.form_nombrePro_2.clear()
            self.form_precioP_2.clear()
            self.form_frec_2.clear()
            self.form_carencia.clear()
        elif( tipo_producto == 3): # Página Producto Plaga
            self.form_ICA_3.clear()
            self.form_nombrePro_3.clear()
            self.form_precioP_3.clear()
            self.form_frec_3.clear()
            self.form_carencia_2.clear()

    # Actualizar tabla de Productos
    def update_product_tables(self, storage):
        self.table_Antibioticos.setRowCount(0)
        self.table_ProductosC.setRowCount(0)

        for key, value in storage.items():
            if(isinstance(value, Antibiotico)):
                rowPosition = self.table_Antibioticos.rowCount()
                self.table_Antibioticos.insertRow(rowPosition)
                self.table_Antibioticos.setItem(rowPosition, 0, QTableWidgetItem( value.Antibiotico_nombre ))
                self.table_Antibioticos.setItem(rowPosition, 1, QTableWidgetItem( value.Antibiotico_dosis  ))
                self.table_Antibioticos.setItem(rowPosition, 2, QTableWidgetItem( value.Antibiotico_tipoAnimal ))
                self.table_Antibioticos.setItem(rowPosition, 3, QTableWidgetItem( str( value.Antibiotico_precio ) ) )
            else:
                rowPosition = self.table_ProductosC.rowCount()
                self.table_ProductosC.insertRow(rowPosition)
                self.table_ProductosC.setItem(rowPosition, 0, QTableWidgetItem( str( value.pControl_ICA ) ))
                self.table_ProductosC.setItem(rowPosition, 1, QTableWidgetItem( value.pControl_nombre ))
                self.table_ProductosC.setItem(rowPosition, 2, QTableWidgetItem( value.pControl_frec ))
                self.table_ProductosC.setItem(rowPosition, 3, QTableWidgetItem( str( value.pControl_valor ) ))

    # Agregar solo un antibiotico a Tabla 
    def add_antibiotic_table(self, **kwargs):
        rowPosition = self.table_Antibioticos.rowCount()
        self.table_Antibioticos.insertRow(rowPosition)
        self.table_Antibioticos.setItem(rowPosition, 0, QTableWidgetItem( kwargs["p_nombre"] ))
        self.table_Antibioticos.setItem(rowPosition, 1, QTableWidgetItem( kwargs["p_dosis"] ))
        self.table_Antibioticos.setItem(rowPosition, 2, QTableWidgetItem( kwargs["p_tipo"] ))
        self.table_Antibioticos.setItem(rowPosition, 3, QTableWidgetItem( str( kwargs["p_precio"] ) ))

    # Agregar solo un Producto Control a Tabla 
    def add_pc_table(self, **kwargs):
        rowPosition = self.table_ProductosC.rowCount()
        self.table_ProductosC.insertRow(rowPosition)
        real_price = kwargs["p_precio"] +  (kwargs["p_ica"] * kwargs["p_precio"])
        self.table_ProductosC.setItem(rowPosition, 0, QTableWidgetItem( str( kwargs["p_ica"] ) ))
        self.table_ProductosC.setItem(rowPosition, 1, QTableWidgetItem( kwargs["p_nombre"] ))
        self.table_ProductosC.setItem(rowPosition, 2, QTableWidgetItem( kwargs["p_frecAp"] ))
        self.table_ProductosC.setItem(rowPosition, 3, QTableWidgetItem( str( real_price ) ))