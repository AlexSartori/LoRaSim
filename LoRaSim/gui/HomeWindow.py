from PyQt5 import QtWidgets, QtGui, QtCore

from LoRaSim.Simulator import Simulator
from LoRaSim.gui.SimIntervalsView import SimIntervalsView


class HomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        self.simulator = Simulator()
        
        self.setWindowTitle("LoRaSim - Home")
        self.setMinimumSize(400, 600)
        self.initUI()

    def initUI(self):
        self.toolbar = self.createToolbar()
        self.simIntView = self.createSimIntView()

    def createToolbar(self):
        startAction = QtWidgets.QAction(
            QtGui.QIcon.fromTheme('media-playback-start'),
            'Start', self
        )
        # startAction.triggered.connect(...)

        toolbar = self.addToolBar('HomeToolbar')
        toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        toolbar.addAction(startAction)
        return toolbar

    def createSimIntView(self):
        s = SimIntervalsView(self.simulator)
        self.setCentralWidget(s)
        return s
