#-*- coding:utf-8 -*-

import sys

import modules.pcalc

#PyQt must be installed.
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

formClass = uic.loadUiType('_ui/design.ui')[0]

class CalcObj:
    def __init__(self):
        self.value = 0
        self.type = ''

class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.b_f.clicked.connect(self.display_update)
        #self.'(object)'.'(event)'.connect(self.calc)

    def obj_btn_clicked():
        self.display_update()
    
    def display_update():
        self.list_in.addItem()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()