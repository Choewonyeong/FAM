# -*- coding: utf-8 -*-
# \AppData\Local\GitHubDesktop\app-2.2.2\resources\app\git\cmd

"""
Created on Sat Oct 26 13:26:32 2019
@author: Choewy
"""

import sys
from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QAction, QApplication, QToolBar, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, \
    QFrame, QPushButton


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.showMaximized()
        self.geometry().center()
        self.setWindowTitle('FAM v0.1')

        self.img1 = 'img/_run'
        self.img2 = 'img/_run'
        self.img3 = 'img/'

        action1 = QAction(QIcon(self.img1), 'importation', self)
        action2 = QAction(QIcon(self.img2), 'expense', self)
        action3 = QAction(QIcon(self.img3), 'save', self)

        action1.triggered.connect(self.toolbar1Clicked)
        action2.triggered.connect(self.toolbar2Clicked)
        action3.triggered.connect(self.toolbar3Clicked)

        action1.setShortcut('Ctrl+N')
        action2.setShortcut('Ctrl+I')
        action3.setShortcut('Ctrl+S')

        toolbar = QToolBar()
        toolbar.addAction(action1)
        toolbar.addAction(action2)
        toolbar.addAction(action3)

# main---------------------------------------------------------------------
        main = QLabel('Main')
        #main.setPixmap(QPixmap('img/'))
        main.setAlignment(Qt.AlignCenter)

# import-------------------------------------------------------------------
        import_main = QLabel('수입내역 등록')
        import_main.setAlignment(Qt.AlignCenter)
        label_import1 = QLabel('날짜')
        label_import2 = QLabel('금액')
        label_import3 = QLabel('입금자')
        label_import4 = QLabel('회차')
        label_import5 = QLabel('비고')

        self.lineEdit_import1 = QLineEdit()
        self.lineEdit_import2 = QLineEdit()
        self.lineEdit_import3 = QLineEdit()
        self.lineEdit_import4 = QLineEdit()
        self.lineEdit_import5 = QLineEdit()

        label_result_import1 = QLabel('합계')
        self.label_result_import2 = QLabel()

        btn_import = QPushButton('등록')
        
# expense----------------------------------------------------------------
        expense_main = QLabel('지출내역 등록')
        expense_main.setAlignment(Qt.AlignCenter)
        label_expense1 = QLabel('날짜')
        label_expense2 = QLabel('금액')
        label_expense3 = QLabel('발주자')
        label_expense4 = QLabel('내용')
        label_expense5 = QLabel('비고')

        self.lineEdit_expense1 = QLineEdit()
        self.lineEdit_expense2 = QLineEdit()
        self.lineEdit_expense3 = QLineEdit()
        self.lineEdit_expense4 = QLineEdit()
        self.lineEdit_expense5 = QLineEdit()

        label_result_expense1 = QLabel('합계')
        self.label_result_expense2 = QLabel()

        btn_expense = QPushButton('등록')

# main Layout-------------------------------------------------------------
        vbox_main = QVBoxLayout()
        vbox_main.addWidget(main)

        self.frame_main = QFrame()
        self.frame_main.setLayout(vbox_main)

# import Layout-----------------------------------------------------------
        import_hbox1 = QHBoxLayout()
        import_hbox1.addWidget(label_import1)
        import_hbox1.addWidget(label_import2)
        import_hbox1.addWidget(label_import3)
        import_hbox1.addWidget(label_import4)
        import_hbox1.addWidget(label_import5)

        import_hbox2 = QHBoxLayout()
        import_hbox2.addWidget(self.lineEdit_import1)
        import_hbox2.addWidget(self.lineEdit_import2)
        import_hbox2.addWidget(self.lineEdit_import3)
        import_hbox2.addWidget(self.lineEdit_import4)
        import_hbox2.addWidget(self.lineEdit_import5)

        import_hbox3 = QHBoxLayout()
        import_hbox3.addWidget(label_result_import1)
        import_hbox3.addWidget(self.label_result_import2)
        import_hbox3.addWidget(btn_import)

        vbox_import = QVBoxLayout()
        vbox_import.addWidget(import_main)
        vbox_import.addWidget(QLabel(''))
        vbox_import.addLayout(import_hbox1)
        vbox_import.addLayout(import_hbox2)
        vbox_import.addLayout(import_hbox3)
        vbox_import.addWidget(QLabel(''), 8)

        self.frame_import = QFrame()
        self.frame_import.setLayout(vbox_import)
        self.frame_import.hide()

# expense Layout-----------------------------------------------------------
        expense_hbox1 = QHBoxLayout()
        expense_hbox1.addWidget(label_expense1)
        expense_hbox1.addWidget(label_expense2)
        expense_hbox1.addWidget(label_expense3)
        expense_hbox1.addWidget(label_expense4)
        expense_hbox1.addWidget(label_expense5)

        expense_hbox2 = QHBoxLayout()
        expense_hbox2.addWidget(self.lineEdit_expense1)
        expense_hbox2.addWidget(self.lineEdit_expense2)
        expense_hbox2.addWidget(self.lineEdit_expense3)
        expense_hbox2.addWidget(self.lineEdit_expense4)
        expense_hbox2.addWidget(self.lineEdit_expense5)

        expense_hbox3 = QHBoxLayout()
        expense_hbox3.addWidget(label_result_expense1)
        expense_hbox3.addWidget(self.label_result_expense2)
        expense_hbox3.addWidget(btn_expense)

        vbox_expense = QVBoxLayout()
        vbox_expense.addWidget(expense_main)
        vbox_expense.addWidget(QLabel(''))
        vbox_expense.addLayout(expense_hbox1)
        vbox_expense.addLayout(expense_hbox2)
        vbox_expense.addLayout(expense_hbox3)
        vbox_expense.addWidget(QLabel(''), 8)

        self.frame_expense = QFrame()
        self.frame_expense.setLayout(vbox_expense)
        self.frame_expense.hide()

        self.hbox_label = QLabel('')
        self.hbox_label.hide()

        hbox = QHBoxLayout()
        hbox.addWidget(self.frame_import)
        hbox.addWidget(self.frame_expense)
        hbox.addWidget(self.hbox_label, 5)
        hbox.addWidget(self.frame_main)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addLayout(hbox)

        self.setLayout(layout)

    def toolbar1Clicked(self):
        if self.img1 == 'img/_run' and self.img2 == 'img/_stop':
            self.frame_main.hide()
            self.frame_import.show()
            self.hbox_label.show()
            self.img1 = 'img/_stop'
            print(self.img1)

        elif self.img1 == 'img/_run' and self.img2 == 'img/_run':
            self.frame_main.hide()
            self.frame_import.show()
            self.hbox_label.hide()
            self.img1 = 'img/_stop'

            print(self.img1)

        elif self.img1 == 'img/_stop' and self.img2 == 'img/_run':
            self.frame_main.hide()
            self.frame_import.hide()
            self.hbox_label.hide()
            self.img1 = 'img/_run'

            print(self.img1)

        elif self.img1 == 'img/_stop' and self.img2 == 'img/_stop':
            self.frame_main.hide()
            self.frame_import.hide()
            self.hbox_label.hide()
            self.img1 = 'img/_run'

            print(self.img1)


    def toolbar2Clicked(self):
        if self.img2 == 'img/_run' :
            self.frame_main.hide()
            self.frame_expense.show()
            self.hbox_label.show()
            self.img2 = 'img/_stop'

        elif self.img2 == 'img/_stop' :
            self.frame_expense.hide()
            self.frame_main.show()
            self.img2 = 'img/_run'

    def toolbar3Clicked(self):
        print(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    app.exec_()
