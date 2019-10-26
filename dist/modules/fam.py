# -*- coding: utf-8 -*-
#\AppData\Local\GitHubDesktop\app-2.2.2\resources\app\git\cmd

"""
Created on Sat Oct 26 13:26:32 2019
@author: Choewy
"""
import sys
from PyQt5.QtWidgets import *

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.showMaximized()
        self.geometry().center()
        self.setWindowTitle('FAM v0.1')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    app.exec_()
