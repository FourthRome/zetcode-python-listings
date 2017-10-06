#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import
import sys


class Example():

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):






        self.setGeometry()
        self.setWindowTitle('')
        self.show()
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())