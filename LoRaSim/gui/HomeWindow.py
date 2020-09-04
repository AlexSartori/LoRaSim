from PyQt5 import QtWidgets, QtGui, QtCore


class HomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        self.setWindowTitle("LoRaSim")
        self.setMinimumSize(self.sizeHint())
