# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser


class WarningApp(object):
    def clicked(self):
        webbrowser.open('http://172.20.10.2:8080/')

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 343)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 300, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 10, 101, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"C:\Users\Airat\PycharmProjects\BayMax_Bank\logo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 110, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 481, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.clicked) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Оповещение"))
        self.label_2.setText(_translate("Dialog", "ОПОВЕЩЕНИЕ"))
        self.label_3.setText(_translate("Dialog", "Система заподозрила что-то странное в ваших действиях. \n"
"Мы всегда готовы вам помочь в любой ситуации. \n"
"Если вы не уверены в проведении транзакции или вами кто-то управляет, \n"
"то нажмите на кнопку ниже, вам откроется чат с админом для решения \n"
"всех проблем"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = WarningApp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
