from PyQt5 import QtWidgets, QtGui, QtCore


class HomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        self.setWindowTitle("LoRaSim - Home")
        self.setMinimumSize(400, 600)
        self.initUI()

    def initUI(self):
        self.toolbar = self.createToolbar()

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
