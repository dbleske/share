#! /usr/bin/env python
"""PyQt Test."""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    """Doc string placeholder."""

    def __init__(self):
        """Doc string placeholder."""
        super().__init__()
        self.title = 'PyQt5 messagebox'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        """Doc string placeholder."""
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        buttonReply = QMessageBox.question(self, "Message",
                                           "Do you like PyQt?",
                                           QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Fusion, Windows, WindowsVista
#    window = QWidget()
#    layout = QVBoxLayout()
#    layout.addWidget(QLabel("Hello World!"))
#    window.setLayout(layout)
#    window.show()
    ex = App()
    sys.exit(app.exec_())
