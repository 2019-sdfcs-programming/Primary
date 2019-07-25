#-*- coding:utf-8 -*-

import sys

import modules.pcalc as pc
import modules.util as ut

#PyQt must be installed.
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

formClass = uic.loadUiType('_ui/design.ui')[0]

index = []
variables = []

class CalcObj:
    def __init__(self):
        self.value = float(0)
        self.valuestr = ''
        self.type = ''

    def update_valuestr(self, num=''):
        self.valuestr = num
        try:
            self.value = float(self.valuestr)
        except ValueError:
            pass

class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.b_f.clicked.connect(lambda: self.obj_btn_clicked('f'))
        self.b_m.clicked.connect(lambda: self.obj_btn_clicked('m'))
        self.b_a.clicked.connect(lambda: self.obj_btn_clicked('a'))
        self.b_t.clicked.connect(lambda: self.obj_btn_clicked('t'))
        self.b_s.clicked.connect(lambda: self.obj_btn_clicked('s'))
        self.b_erase.clicked.connect(lambda: self.obj_btn_clicked('e'))
        self.b_v1.clicked.connect(lambda: self.obj_btn_clicked('v1'))
        self.b_v2.clicked.connect(lambda: self.obj_btn_clicked('v2'))
        self.b_p1.clicked.connect(lambda: self.obj_btn_clicked('p1'))
        self.b_p2.clicked.connect(lambda: self.obj_btn_clicked('p2'))
        self.b_I.clicked.connect(lambda: self.obj_btn_clicked('i'))
        self.b_Clear.clicked.connect(lambda: self.obj_btn_clicked('c'))
        self.b_1.clicked.connect(lambda: self.obj_btn_clicked('1'))
        self.b_2.clicked.connect(lambda: self.obj_btn_clicked('2'))
        self.b_3.clicked.connect(lambda: self.obj_btn_clicked('3'))
        self.b_4.clicked.connect(lambda: self.obj_btn_clicked('4'))
        self.b_5.clicked.connect(lambda: self.obj_btn_clicked('5'))
        self.b_6.clicked.connect(lambda: self.obj_btn_clicked('6'))
        self.b_7.clicked.connect(lambda: self.obj_btn_clicked('7'))
        self.b_8.clicked.connect(lambda: self.obj_btn_clicked('8'))
        self.b_9.clicked.connect(lambda: self.obj_btn_clicked('9'))
        self.b_0.clicked.connect(lambda: self.obj_btn_clicked('0'))
        self.b_dot.clicked.connect(lambda: self.obj_btn_clicked('.'))
        self.b_Enter.clicked.connect(lambda: self.obj_btn_clicked('n'))
        #self.'(object)'.'(event)'.connect(self.calc)

    def obj_btn_clicked(self, btn=''):
        global index
        global variables
        if btn == 'f' or btn == 'm' or btn == 'a' or btn == 't' or btn == 's' or btn == 'v1' or btn == 'v2' or btn == 'p1' or btn == 'p2' or btn == 'i':
            self.display_update(btn)
        elif btn == '0' or btn == '1' or btn == '2' or btn == '3' or btn == '4' or btn == '5' or btn == '6' or btn == '7' or btn == '8' or btn == '9' or btn == '0' or btn == '.':
            self.num_update('add', btn)
        elif btn == 'c':
            self.list_in.clear()
            variables = []
            index = []
        elif btn == 'e':
            self.num_update('del')
        print(variables)
        self.check_result()

    def display_update(self, var, data=[]):
        global index
        global variables
        nowcalc = CalcObj()
        nowcalc.type = var
        index += [var]
        variables += [{'var' : var, 'obj' : nowcalc}]
        self.list_in.addItem('{0} = '.format(var))
        print(str(index))
        print(str(variables))

    def num_update(self, op, var = ''):
        global variables
        row = self.list_in.currentRow()
        item = self.list_in.currentItem()
        if row != -1:
            if op == 'add':
                variables[row]['obj'].update_valuestr(variables[row]['obj'].valuestr + var)
                item.setText('{} = {}'.format(variables[row]['var'], variables[row]['obj'].valuestr))
            elif op == 'del':
                variables[row]['obj'].update_valuestr(ut.delbtn(variables[row]['obj'].valuestr))
                item.setText('{} = {}'.format(variables[row]['var'], variables[row]['obj'].valuestr))

    def check_result(self):
        global index
        global variables
        
        from __LocalSettings__ import RESULT_INDEXER as RI
        for i in range(len(RI)):
            print('chkif = {}'.format(i))
            if ut.chkif(RI[i], index):
                break
        if i >= 0 and i < 5:
            __type__ = 'svt'
            if i == 0 or i == 1:
                __requ__ = 't'
            elif i == 2:
                __requ__ = 'v'
            elif i == 3 or i == 4:
                __requ__ = 's'
        elif i >= 5 and i < 8:
            __type__ = 'fma'
            if i == 5:
                __requ__ = 'a'
            elif i == 6:
                __requ__ = 'm'
            elif i == 7:
                __requ__ = 'f'
        elif i >= 8 and i < 14:
            __type__ = 'pmv'
            if i == 8 or i == 9:
                __requ__ = 'v'
            elif i >= 10 and i < 12:
                __requ__ = 'm'
            else:
                __requ__ = 'p'
        elif i >= 14 and i < 17:
            __type__ = 'ift'
            if i == 14:
                __requ__ = 't'
            elif i == 15:
                __requ__ = 'f'
            elif i == 16:
                __requ__ = 'i'
        else:
            return 0

        #if ('s' in index and 'v1' in index) or ('s' in index and 'v2' in index) or ('s' in index and 't' in index) or ('v1' in index and 't' in index) or ('v2' in index and 't' in index):
        #elif ('f' in index and 'm' in index) or ('f' in index and 'a' in index) or ('m' in index and 'a' in index):
        #elif ('p1' in index and 'm' in index) or ('p2' in index and 'm' in index) or ('p1' in index and 'v1' in index) or ('p1' in index and 'v2' in index) or ('p2' in index and 'v1' in index) or ('p2' in index and 'v2' in index) or ('m' in index and 'v1' in index) or ('m' in index and 'v2' in index):
        #elif ('i' in index and 'f' in index) or ('i' in index and 't' in index) or ('f' in index and 't' in index):

        if 'v1' in index:
            v = 'v1'
        elif 'v2' in index:
            v = 'v2'
        if 'p1' in index:
            p = 'p1'
        elif 'p2' in index:
            p = 'p2'

        data = []
        if __type__ == 'svt': # svt
            if __requ__ == 't': 
                data += [ut.wrapper(variables, 's')]
                data += [ut.wrapper(variables, v)]
            elif __requ__ == 'v':
                data += [ut.wrapper(variables, 's')]
                data += [ut.wrapper(variables, 't')]
            elif __requ__ == 's':
                data += [ut.wrapper(variables, v)]
                data += [ut.wrapper(variables, 't')]
        if __type__ == 'fma': # fma
            if __requ__ == 'a':
                data += [ut.wrapper(variables, 'f')]
                data += [ut.wrapper(variables, 'm')]
            elif __requ__ == 'm':
                data += [ut.wrapper(variables, 'f')]
                data += [ut.wrapper(variables, 'a')]
            elif __requ__ == 'f':
                data += [ut.wrapper(variables, 'm')]
                data += [ut.wrapper(variables, 'a')]
        if __type__ == 'pmv': # pmv
            if __requ__ == 'v':
                data += [ut.wrapper(variables, p)]
                data += [ut.wrapper(variables, 'm')]
            elif __requ__ == 'm':
                data += [ut.wrapper(variables, p)]
                data += [ut.wrapper(variables, v)]
            elif __requ__ == 'p':
                data += [ut.wrapper(variables, 'm')]
                data += [ut.wrapper(variables, v)]
        if __type__ == 'ift': # ift
            if __requ__ == 't':
                data += [ut.wrapper(variables, 'i')]
                data += [ut.wrapper(variables, 'f')]
            elif __requ__ == 'f':
                data += [ut.wrapper(variables, 'i')]
                data += [ut.wrapper(variables, 't')]
            elif __requ__ == 'i':
                data += [ut.wrapper(variables, 'f')]
                data += [ut.wrapper(variables, 't')]

        reqdata = {
            '__init__' : 'calc',
            '__type__' : __type__,
            '__requ__' : __requ__,
            'data' : data
        }

        print(str(reqdata))
        try:
            result = pc.calc(reqdata)
            print(result)
            self.list_out.clear()
            self.list_out.addItem('{} = {}'.format(__requ__, str(result['result'])))
        except TypeError:
            self.list_out.clear()
        except ZeroDivisionError:
            self.list_out.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()