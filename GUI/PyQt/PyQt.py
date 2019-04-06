import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui,QtCore
class Ana(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.win = uic.loadUi(r"D:\İbrahim EDİZ\23022019\Örnekler\GUI\ana.ui")
        self.win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ana()
    sys.exit(app.exec_())

