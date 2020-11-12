'''
    PlotOptPanel.py - A GroupBox to configure the Simulation output
    Created by Alessandro Sartori, November 2020.
'''

from PyQt5 import QtWidgets


class PlotOptPanel(QtWidgets.QGroupBox):
    def __init__(self):
        super(PlotOptPanel, self).__init__()
        self.initUI()

    def initUI(self):
        self.setTitle("Simulation output:")
        self.setLayout(QtWidgets.QVBoxLayout())

        rcv_prob = QtWidgets.QCheckBox()
        rcv_prob.setText("Probability of successful delivery vs. Time")
        rcv_prob.setChecked(True)
        self.layout().addWidget(rcv_prob)

        throughput = QtWidgets.QCheckBox()
        throughput.setText("Throughput vs. Time")
        throughput.setChecked(False)
        self.layout().addWidget(throughput)
