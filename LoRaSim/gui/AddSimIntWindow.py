import os
from PyQt5 import QtWidgets, QtCore
from LoRaSim.MarkovChain import MarkovChain
from LoRaSim.gui.MarkovListItem import MarkovListItem


class AddSimIntWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.setWindowTitle("Add Simulation Interval")
        self.setMinimumSize(400, 400)
        self.initUI()

    def initUI(self):
        self.setLayout(QtWidgets.QVBoxLayout())
        self.title = self.createTitle()
        self.intView = self.createIntView()
        self.durationSpinner = self.createDurationSpinner()
        self.addBtn = self.createAddBtn()

        self.loadMarkovModels()

    def createTitle(self):
        title = QtWidgets.QLabel()
        title.setText("Available models:")
        self.layout().addWidget(title)
        return title

    def createIntView(self):
        view = QtWidgets.QListWidget()
        self.layout().addWidget(view)
        return view

    def loadMarkovModels(self):
        gui_dir = os.path.dirname(os.path.realpath(__file__))
        sim_dir = os.path.dirname(gui_dir)
        mod_dir = os.path.join(sim_dir, 'Models')

        for f in os.listdir(mod_dir):
            file = os.path.join(mod_dir, f)
            model = MarkovChain()
            model.loadFromFile(file)
            self.addModelWidget(model)

    def addModelWidget(self, model):
        assert isinstance(model, MarkovChain)
        w = MarkovListItem(model)
        container = QtWidgets.QListWidgetItem()
        container.setSizeHint(w.sizeHint())
        self.intView.addItem(container)
        self.intView.setItemWidget(container, w)

    def createDurationSpinner(self):
        label = QtWidgets.QLabel()
        label.setText("Duration (hh:mm:ss:ms):")
        self.layout().addWidget(label)

        spinner = QtWidgets.QTimeEdit()
        spinner.setTimeRange(
            QtCore.QTime(0, 0, 0, 0),
            QtCore.QTime(9, 0, 0, 0)
        )
        spinner.setDisplayFormat("hh:mm:ss:zzz")
        self.layout().addWidget(spinner)
        return spinner

    def createAddBtn(self):
        btn = QtWidgets.QPushButton()
        btn.setText("Add to simulation")
        self.layout().addWidget(btn)
        return btn
