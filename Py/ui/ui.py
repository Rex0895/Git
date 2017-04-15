# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programs\Py\ui\ui.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 310)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Light = QtWidgets.QDial(Dialog)
        self.Light.setGeometry(QtCore.QRect(20, 100, 121, 64))
        self.Light.setObjectName("Light")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 10, 47, 13))
        self.label.setObjectName("label")
        self.Poliv = QtWidgets.QSlider(Dialog)
        self.Poliv.setGeometry(QtCore.QRect(20, 40, 160, 22))
        self.Poliv.setOrientation(QtCore.Qt.Horizontal)
        self.Poliv.setObjectName("Poliv")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(220, 80, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 40, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(220, 120, 61, 16))
        self.label_5.setObjectName("label_5")
        self.Close = QtWidgets.QPushButton(Dialog)
        self.Close.setGeometry(QtCore.QRect(100, 70, 81, 23))
        self.Close.setObjectName("Close")
        self.Open = QtWidgets.QPushButton(Dialog)
        self.Open.setGeometry(QtCore.QRect(20, 70, 81, 23))
        self.Open.setObjectName("Open")
        self.Nasos = QtWidgets.QSlider(Dialog)
        self.Nasos.setGeometry(QtCore.QRect(20, 10, 160, 22))
        self.Nasos.setOrientation(QtCore.Qt.Horizontal)
        self.Nasos.setObjectName("Nasos")
        self.On = QtWidgets.QPushButton(Dialog)
        self.On.setGeometry(QtCore.QRect(20, 170, 81, 23))
        self.On.setObjectName("On")
        self.Off = QtWidgets.QPushButton(Dialog)
        self.Off.setGeometry(QtCore.QRect(100, 170, 81, 23))
        self.Off.setObjectName("Off")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(220, 170, 81, 16))
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(20, 210, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(220, 210, 81, 16))
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 250, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Насос"))
        self.label_4.setText(_translate("Dialog", "Ворота"))
        self.label_3.setText(_translate("Dialog", "Полив"))
        self.label_5.setText(_translate("Dialog", "Освещение"))
        self.Close.setText(_translate("Dialog", "Close"))
        self.Open.setText(_translate("Dialog", "Open"))
        self.On.setText(_translate("Dialog", "On"))
        self.Off.setText(_translate("Dialog", "Off"))
        self.label_6.setText(_translate("Dialog", "Сигнализация"))
        self.label_7.setText(_translate("Dialog", "Время"))

