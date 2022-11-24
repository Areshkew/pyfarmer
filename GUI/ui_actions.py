from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class QActions:
    def __init__(self):
        # PAGINAS CADA PAGINA DEL PROGRAMA
        self.ui.btn_clientes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.btn_productos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.btn_facturas.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        
        # BOTONES CLIENTES
        self.ui.btn_agregar.clicked.connect( self.ui.add_client ) # Agregar Cliente
        self.ui.btn_eliminar.clicked.connect( self.ui.delete_client ) # Eliminar Cliente
        self.ui.btn_actualizar.clicked.connect( self.ui.update_client ) # Actualizar Cliente

        # PAGINAS AGREGAR PRODUCTO
        self.ui.btn_antibiotico.clicked.connect(lambda: self.ui.stacked_productos.setCurrentWidget(self.ui.page_a))
        self.ui.btn_productoControl.clicked.connect(lambda: self.ui.stacked_productos.setCurrentWidget(self.ui.page_pC))
        self.ui.btn_productoControl_2.clicked.connect(lambda: self.ui.stacked_productos.setCurrentWidget(self.ui.page_pFert))
        self.ui.btn_productoControl_3.clicked.connect(lambda: self.ui.stacked_productos.setCurrentWidget(self.ui.page_pPlaga))

        # BOTONES PRODUCTOS
        self.ui.btn_agregarAnt.clicked.connect( self.ui.add_product ) # Agregar Producto
        self.ui.btn_agregarP.clicked.connect( self.ui.add_product ) # Agregar Producto
        self.ui.btn_agregarP_2.clicked.connect( self.ui.add_product ) # Agregar Producto
        self.ui.btn_agregarP_3.clicked.connect( self.ui.add_product ) # Agregar Producto   
        self.ui.btn_eProd.clicked.connect( self.ui.delete_product ) # Eliminar Cliente

        # PAGINAS SECCIÓN FACTURA
        self.ui.btn_crearF.clicked.connect(lambda: self.ui.stacked_facturas.setCurrentWidget(self.ui.p_crearF))
        self.ui.btn_listaF.clicked.connect(lambda: self.ui.stacked_facturas.setCurrentWidget(self.ui.p_listaF))

        # BOTONES CREAR FACTURA
        self.ui.btn_FaddP.clicked.connect( self.ui.add_bill_product ) # Agregar Producto
        self.ui.btn_Fcreate.clicked.connect( self.ui.create_bill ) # Agregar Factura

        # LISTA DE FACTURAS
        self.ui.btn_listaF.clicked.connect( self.ui.load_bills_data ) # Cargar lista de facturas
        self.ui.groupBox.setHidden(True) # Información de la factura clickeada
        self.ui.table_facturas.selectionModel().selectionChanged.connect(self.ui.click_row) # Acciones a clickear una fila
        