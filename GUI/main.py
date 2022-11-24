# Qt Designer
import sys, os, platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# Establecer Directorio Padre
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

#Gui
from ui_window import Ui_MainWindow
from ui_actions import *

#
class MainWindow(QActions, QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Botones y demás
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QActions.__init__(self)

        # VENTANA
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
