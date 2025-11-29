# -*- coding: utf-8 -*-
"""
UI Layout Definition - Auto-generated from Qt Designer
Author: Wanzhen Fu
WARNING: All changes made in this file will be lost when regenerated!
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    """Main form UI setup and layout."""
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(852, 510)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(660, 430, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 50, 101, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(450, 50, 111, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 81, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 430, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(140, 100, 211, 121))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(370, 100, 211, 121))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 240, 211, 121))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(370, 240, 211, 121))
        self.textEdit_4.setObjectName("textEdit_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """Set UI text labels and window title."""
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crypto Ticker - Binance API"))
        self.pushButton.setText(_translate("Form", "Exit"))
        self.label.setText(_translate("Form", "BTC/USDT"))
        self.label_2.setText(_translate("Form", "ETH/USDT"))
        self.label_3.setText(_translate("Form", "Real-time Price"))
        self.label_4.setText(_translate("Form", "MA(8)"))
        self.pushButton_2.setText(_translate("Form", "Start"))

