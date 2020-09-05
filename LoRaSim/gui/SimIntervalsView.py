'''
    SimIntervalsView.py - A QFrame to display currently scheduled
    simulation intervals and add new ones.
    Created by Alessandro Sartori, September 2020.
'''

from PyQt5 import QtWidgets, QtGui, QtCore


class SimIntervalsView(QtWidgets.QFrame):
    def __init__(self):
        super(SimIntervalsView, self).__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        self.initUI()

    def initUI(self):
        self.title = self.createTitle()
        self.table = self.createIntTable()
        self.add_btn = self.createAddBtn()

    def createTitle(self):
        title = QtWidgets.QLabel()
        title.setText("Simulation intervals:")
        self.layout().addWidget(title)
        return title

    def createIntTable(self):
        tab = QtWidgets.QTableView()
        self.layout().addWidget(tab)
        return tab

    def createAddBtn(self):
        add_btn = QtWidgets.QPushButton()
        add_btn.setText("+ Add interval")
        # add_btn.clicked.connect(...)
        self.layout().addWidget(add_btn)
        return add_btn
