from PyQt5 import QtWidgets


class AddSimIntWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.setWindowTitle("Add Simulation Interval")
        self.setMinimumSize(400, 400)
        self.initUI()

    def initUI(self):
        pass
