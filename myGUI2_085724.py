import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Toggle Button App")  # set the window title
        self.setGeometry(100, 100, 800, 600)  # set the window geometry
        self.button = QPushButton("Toggle!", self)  # create a push button
        self.button.setGeometry(350, 250, 100, 40)  # set button geometry
        self.button.setCheckable(True)  # set checkable to true
        self.button.clicked.connect(self.change_color)  # set calling method by button
        self.button.setStyleSheet("background-color: cyan")  # set default bckgrnd color

    # Method (slot) called by button
    def change_color(self):
        # button checked?
        if self.button.isChecked():
            self.button.setStyleSheet("background-color: red")
            print("You just checked the push button")
        # button unchecked?
        else:
            self.button.setStyleSheet("background-color: cyan")
            print("You just unchecked the push button")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
