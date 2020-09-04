import sys
from PyQt5.QtWidgets import QApplication
from LoRaSim.gui.HomeWindow import HomeWindow


def launch():
    app = QApplication(sys.argv)

    win = HomeWindow()
    win.show()

    sys.exit(app.exec_())
