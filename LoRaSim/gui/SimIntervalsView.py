'''
    SimIntervalsView.py - A QFrame to display currently scheduled
    simulation intervals and add new ones.
    Created by Alessandro Sartori, September 2020.
'''

from PyQt5 import QtWidgets, QtGui
from LoRaSim.gui.AddSimIntWindow import AddSimIntWindow


class SimIntervalsView(QtWidgets.QFrame):
    def __init__(self):
        super(SimIntervalsView, self).__init__()
        self.initUI()

    def initUI(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        self.title = self.createTitle()
        self.table = self.createIntTable()
        self.add_btn = self.createAddBtn()

    def createTitle(self):
        title = QtWidgets.QLabel()
        title.setText("Simulation intervals:")
        self.layout().addWidget(title)
        return title

    def createIntTable(self):
        tab = QtWidgets.QTableWidget()
        tab.setColumnCount(3)
        tab.setHorizontalHeaderLabels(['Start time (ms)', 'Duration (ms)', 'Model'])
        tab.horizontalHeader().setStretchLastSection(True)
        tab.resizeColumnsToContents()
        # tab.setRowCount(1)
        # tab.setItem(0, 0, QtWidgets.QTableWidgetItem('a'))

        self.layout().addWidget(tab)
        return tab

    def createAddBtn(self):
        add_btn = QtWidgets.QPushButton()
        add_btn.setText("+ Add interval")
        add_btn.clicked.connect(self.openAddSimIntWindow)
        self.layout().addWidget(add_btn)
        return add_btn

    def openAddSimIntWindow(self):
        dialog = AddSimIntWindow(self)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            selected = dialog.intView.selectedItems()
            if len(selected) < 1: return
            modelItem = dialog.intView.itemWidget(selected[0])
            model = modelItem.model

            self.addIntervalToSim(
                model,
                dialog.durationSpinner.time().msecsSinceStartOfDay()
            )
        else:
            print('Cancelled')
        dialog.deleteLater()

    def addIntervalToSim(self, model, duration_ms):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QtWidgets.QTableWidgetItem('-'))
        self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(duration_ms)))
        self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(model.title))
