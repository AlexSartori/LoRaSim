'''
    HomeWindow.py - The main window of the simulator
    Created by Alessandro Sartori, September 2020.
'''

from PyQt5 import QtWidgets, QtGui

from LoRaSim.Simulator import Simulator
from LoRaSim.gui.SimIntervalsView import SimIntervalsView
from LoRaSim.gui.PlotOptPanel import PlotOptPanel
from LoRaSim.gui.Plotter import Plotter


class HomeWindow(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()
        self.simulator = Simulator()

        self.setWindowTitle("LoRaSim - Home")
        self.setMinimumSize(400, 600)
        self.initUI()

    def initUI(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        self.simIntView = self.createSimIntView()
        self.plotOptPanel = self.createPlotOptPanel()
        self.start_btn = self.createStartBtn()

    def createSimIntView(self):
        s = SimIntervalsView(self.simulator)
        self.layout().addWidget(s)
        return s

    def createPlotOptPanel(self):
        p = PlotOptPanel()
        self.layout().addWidget(p)
        return p

    def createStartBtn(self):
        b = QtWidgets.QPushButton()
        b.setText("Start Simulation")
        b.setIcon(QtGui.QIcon.fromTheme('media-playback-start'))
        b.clicked.connect(self.runSimulation)
        self.layout().addWidget(b)
        return b

    def runSimulation(self):
        data = self.simulator.run()

        p = Plotter(data)
        
        if self.plotOptPanel.getRcvProbOption():
            p.plot_rcv_prob()
        if self.plotOptPanel.getThroughputOption():
            p.plot_throughput()

        p.show_plots()
