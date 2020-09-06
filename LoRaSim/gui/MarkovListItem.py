'''
    MarkovListItem.py - QtWidget for QListViews to nicely display
    a Markov Model and its details.
    Creted by Alessandro Sartori, September 2020.
'''

from PyQt5 import QtWidgets, QtGui


class MarkovListItem(QtWidgets.QWidget):
    def __init__(self, model):
        super(MarkovListItem, self).__init__()
        self.model = model
        self.initUI()

    def initUI(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        self.title = self.createTitle()
        self.desc = self.createDesc()

    def createTitle(self):
        t = QtWidgets.QLabel()
        t.setText(self.model.title)
        t.setFont(QtGui.QFont("sans-serif", 14, QtGui.QFont.Bold))
        self.layout().addWidget(t)
        return t

    def createDesc(self):
        d = QtWidgets.QLabel()
        d.setText(self.model.description)
        self.layout().addWidget(d)
        return d
