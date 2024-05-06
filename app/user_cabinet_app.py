# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from ai.get_photo import get_photo
from ai.get_photos import get_photos
from ai.check_warnings import check_warnings
from app.warning_app import WarningApp
import sys

name = ""
surname = ""
card = ""
cvv = ""
date = ""


class UserCabinet(object):
    def open_warning(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = WarningApp()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def clicked_getMoney(self):
        get_photo(name='photo0')
        self.tabWidget.setCurrentIndex(1)


    def clicked_credit(self):
        get_photo(name='photo0')
        self.tabWidget.setCurrentIndex(2)

    def clicked_ipoteka(self):
        get_photo(name='photo0')
        self.tabWidget.setCurrentIndex(3)

    def getMoney(self):
        get_photos(name='photo', counter=2, timer=0.3)
        path = rf'C:\Users\Airat\PycharmProjects\BayMax_Bank\ai\photos'
        counter = 3
        counter_angry = 0
        counter_fear = 0
        counter_old = 0
        for i in range(0, counter):
            file = rf'{path}\photo{str(i)}.png'
            print(file)
            res = check_warnings(img_path=file)
            if res == "Dangerous emoji: fear":
                counter_fear += 1
            if res == "Dangerous emoji: angry":
                counter_angry += 1
            if res == "Dangerous: old user":
                counter_old += 1

        with open('data_about_current_user.txt', 'w', encoding='utf-8') as file:
            file.write(f'User: {name} {surname}\nCard number: {card}\nCVV: {cvv}\nDate: {date}\n')
            file.write(f'Counter of fear emotion: {counter_fear}\nCounter of angry emotion: {counter_angry}\nCounter of old factor: {counter_old}')

        print(f'Counter of fear emotion: {counter_fear}')
        print(f'Counter of angry emotion: {counter_angry}')
        print(f'Counter of old factor: {counter_old}')
        if (counter_fear + counter_angry + counter_old) > 1.5:
            print('WARNING‼‼‼')
            self.open_warning()
        else:
            # Working arduino
            print('all ok')

    def getCredit(self):
        get_photos(name='photo', counter=2, timer=0.3)
        path = rf'C:\Users\Airat\PycharmProjects\BayMax_Bank\ai\photos'
        counter = 3
        counter_angry = 0
        counter_fear = 0
        counter_old = 0
        for i in range(0, counter):
            file = rf'{path}\photo{str(i)}.png'
            print(file)
            if check_warnings(img_path=file) == "Dangerous emoji: fear":
                counter_fear += 1
            if check_warnings(img_path=file) == "Dangerous emoji: angry":
                counter_angry += 1
            if check_warnings(img_path=file) == "Dangerous: old user":
                counter_old += 1

        with open('data_about_current_user.txt', 'w', encoding='utf-8') as file:
            file.write(f'User: {name} {surname}\nCard number: {card}\nCVV: {cvv}\nDate: {date}\n')
            file.write(f'Counter of fear emotion: {counter_fear}\nCounter of angry emotion: {counter_angry}\nCounter of old factor: {counter_old}')

        print(f'Counter of fear emotion: {counter_fear}')
        print(f'Counter of angry emotion: {counter_angry}')
        print(f'Counter of old factor: {counter_old}')
        if (counter_fear + counter_angry + counter_old) > 1.5:
            print('WARNING‼‼‼')
            self.open_warning()
        else:
            # working arduino
            print('all ok')

    def getIpoteka(self):
        get_photos(name='photo', counter=2, timer=0.3)
        path = rf'C:\Users\Airat\PycharmProjects\BayMax_Bank\ai\photos'
        counter = 3
        counter_angry = 0
        counter_fear = 0
        counter_old = 0
        for i in range(0, counter):
            file = rf'{path}\photo{str(i)}.png'
            print(file)
            if check_warnings(img_path=file) == "Dangerous emoji: fear":
                counter_fear += 1
            if check_warnings(img_path=file) == "Dangerous emoji: angry":
                counter_angry += 1
            if check_warnings(img_path=file) == "Dangerous: old user":
                counter_old += 1

        with open('data_about_current_user.txt', 'w') as file:
            file.write(f'User: {name} {surname}\nCard number: {card}\nCVV: {cvv}\nDate: {date}\n')
            file.write(f'Counter of fear emotion: {counter_fear}\nCounter of angry emotion: {counter_angry}\nCounter of old factor: {counter_old}')

        print(f'Counter of fear emotion: {counter_fear}')
        print(f'Counter of angry emotion: {counter_angry}')
        print(f'Counter of old factor: {counter_old}')
        if (counter_fear + counter_angry + counter_old) > 1.5:
            print('WARNING‼‼‼')
            self.open_warning()
        else:
            # working arduino
            print('all ok')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1091, 721))
        self.tabWidget.setObjectName("tabWidget")
        self.start_page = QtWidgets.QWidget()
        self.start_page.setObjectName("start_page")
        self.logo_start_page = QtWidgets.QLabel(self.start_page)
        self.logo_start_page.setGeometry(QtCore.QRect(490, 90, 101, 121))
        self.logo_start_page.setText("")
        self.logo_start_page.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo_start_page.setObjectName("logo_start_page")
        self.name_start_page = QtWidgets.QLabel(self.start_page)
        self.name_start_page.setGeometry(QtCore.QRect(440, 190, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page.setFont(font)
        self.name_start_page.setObjectName("name_start_page")
        self.lozung_star_page = QtWidgets.QLabel(self.start_page)
        self.lozung_star_page.setGeometry(QtCore.QRect(430, 220, 261, 20))
        self.lozung_star_page.setObjectName("lozung_star_page")
        self.version_start_page = QtWidgets.QLabel(self.start_page)
        self.version_start_page.setGeometry(QtCore.QRect(880, 650, 181, 31))
        self.version_start_page.setObjectName("version_start_page")
        self.type_operation = QtWidgets.QLabel(self.start_page)
        self.type_operation.setGeometry(QtCore.QRect(430, 280, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.type_operation.setFont(font)
        self.type_operation.setObjectName("type_operation")
        self.get_money_button_start_page = QtWidgets.QPushButton(self.start_page)
        self.get_money_button_start_page.setGeometry(QtCore.QRect(110, 340, 261, 241))
        self.get_money_button_start_page.setObjectName("get_money_button_start_page")
        self.get_money_button_start_page.clicked.connect(self.clicked_getMoney)
        self.get_credit_button_start_page = QtWidgets.QPushButton(self.start_page)
        self.get_credit_button_start_page.setGeometry(QtCore.QRect(410, 340, 261, 241))
        self.get_credit_button_start_page.setObjectName("get_credit_button_start_page")
        self.get_credit_button_start_page.clicked.connect(self.clicked_credit)
        self.get_ipoteka_button_start_page = QtWidgets.QPushButton(self.start_page)
        self.get_ipoteka_button_start_page.setGeometry(QtCore.QRect(710, 340, 261, 241))
        self.get_ipoteka_button_start_page.setObjectName("get_ipoteka_button_start_page")
        self.get_ipoteka_button_start_page.clicked.connect(self.clicked_ipoteka)
        self.tabWidget.addTab(self.start_page, "")
        self.get_money = QtWidgets.QWidget()
        self.get_money.setObjectName("get_money")
        self.logo_start_page_2 = QtWidgets.QLabel(self.get_money)
        self.logo_start_page_2.setGeometry(QtCore.QRect(90, 60, 101, 121))
        self.logo_start_page_2.setText("")
        self.logo_start_page_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo_start_page_2.setObjectName("logo_start_page_2")
        self.name_start_page_2 = QtWidgets.QLabel(self.get_money)
        self.name_start_page_2.setGeometry(QtCore.QRect(40, 160, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page_2.setFont(font)
        self.name_start_page_2.setObjectName("name_start_page_2")
        self.name_start_page_3 = QtWidgets.QLabel(self.get_money)
        self.name_start_page_3.setGeometry(QtCore.QRect(380, 20, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page_3.setFont(font)
        self.name_start_page_3.setObjectName("name_start_page_3")
        self.label = QtWidgets.QLabel(self.get_money)
        self.label.setGeometry(QtCore.QRect(330, 80, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.get_money)
        self.label_2.setGeometry(QtCore.QRect(330, 100, 91, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.get_money)
        self.label_3.setGeometry(QtCore.QRect(330, 130, 71, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.get_money)
        self.label_4.setGeometry(QtCore.QRect(330, 160, 91, 41))
        self.label_4.setObjectName("label_4")
        self.name_start_page_4 = QtWidgets.QLabel(self.get_money)
        self.name_start_page_4.setGeometry(QtCore.QRect(300, 230, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page_4.setFont(font)
        self.name_start_page_4.setObjectName("name_start_page_4")
        self.label_5 = QtWidgets.QLabel(self.get_money)
        self.label_5.setGeometry(QtCore.QRect(430, 90, 431, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.get_money)
        self.label_6.setGeometry(QtCore.QRect(430, 110, 431, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.get_money)
        self.label_7.setGeometry(QtCore.QRect(390, 140, 431, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.get_money)
        self.label_8.setGeometry(QtCore.QRect(420, 170, 431, 16))
        self.label_8.setObjectName("label_8")
        self.radioButton = QtWidgets.QRadioButton(self.get_money)
        self.radioButton.setGeometry(QtCore.QRect(50, 310, 311, 51))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.get_money)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 340, 241, 61))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_9 = QtWidgets.QLabel(self.get_money)
        self.label_9.setGeometry(QtCore.QRect(400, 320, 461, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.get_money)
        self.lineEdit.setGeometry(QtCore.QRect(400, 350, 541, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.get_money)
        self.pushButton.setGeometry(QtCore.QRect(210, 430, 611, 121))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getMoney)
        self.label_10 = QtWidgets.QLabel(self.get_money)
        self.label_10.setGeometry(QtCore.QRect(410, 550, 211, 31))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.get_money, "")
        self.credit = QtWidgets.QWidget()
        self.credit.setObjectName("credit")
        self.label_41 = QtWidgets.QLabel(self.credit)
        self.label_41.setGeometry(QtCore.QRect(340, 90, 101, 31))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.credit)
        self.label_42.setGeometry(QtCore.QRect(340, 110, 91, 41))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.credit)
        self.label_43.setGeometry(QtCore.QRect(340, 170, 91, 41))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.credit)
        self.label_44.setGeometry(QtCore.QRect(340, 140, 71, 41))
        self.label_44.setObjectName("label_44")
        self.name_start_page_17 = QtWidgets.QLabel(self.credit)
        self.name_start_page_17.setGeometry(QtCore.QRect(50, 170, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page_17.setFont(font)
        self.name_start_page_17.setObjectName("name_start_page_17")
        self.name_start_page_18 = QtWidgets.QLabel(self.credit)
        self.name_start_page_18.setGeometry(QtCore.QRect(390, 30, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page_18.setFont(font)
        self.name_start_page_18.setObjectName("name_start_page_18")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.credit)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 360, 541, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_45 = QtWidgets.QLabel(self.credit)
        self.label_45.setGeometry(QtCore.QRect(440, 120, 431, 16))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.credit)
        self.label_46.setGeometry(QtCore.QRect(430, 180, 431, 16))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.credit)
        self.label_47.setGeometry(QtCore.QRect(450, 330, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.pushButton_5 = QtWidgets.QPushButton(self.credit)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 400, 611, 121))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.getCredit)
        self.label_48 = QtWidgets.QLabel(self.credit)
        self.label_48.setGeometry(QtCore.QRect(440, 100, 431, 16))
        self.label_48.setObjectName("label_48")
        self.logo_start_page_9 = QtWidgets.QLabel(self.credit)
        self.logo_start_page_9.setGeometry(QtCore.QRect(100, 70, 101, 121))
        self.logo_start_page_9.setText("")
        self.logo_start_page_9.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo_start_page_9.setObjectName("logo_start_page_9")
        self.label_49 = QtWidgets.QLabel(self.credit)
        self.label_49.setGeometry(QtCore.QRect(410, 530, 211, 31))
        self.label_49.setObjectName("label_49")
        self.name_start_page_19 = QtWidgets.QLabel(self.credit)
        self.name_start_page_19.setGeometry(QtCore.QRect(330, 270, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page_19.setFont(font)
        self.name_start_page_19.setObjectName("name_start_page_19")
        self.label_50 = QtWidgets.QLabel(self.credit)
        self.label_50.setGeometry(QtCore.QRect(400, 150, 431, 16))
        self.label_50.setObjectName("label_50")
        self.tabWidget.addTab(self.credit, "")
        self.ipoteka = QtWidgets.QWidget()
        self.ipoteka.setObjectName("ipoteka")
        self.label_51 = QtWidgets.QLabel(self.ipoteka)
        self.label_51.setGeometry(QtCore.QRect(440, 550, 211, 31))
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.ipoteka)
        self.label_52.setGeometry(QtCore.QRect(470, 120, 431, 16))
        self.label_52.setObjectName("label_52")
        self.pushButton_6 = QtWidgets.QPushButton(self.ipoteka)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 420, 611, 121))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.getIpoteka)
        self.label_53 = QtWidgets.QLabel(self.ipoteka)
        self.label_53.setGeometry(QtCore.QRect(480, 350, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.name_start_page_20 = QtWidgets.QLabel(self.ipoteka)
        self.name_start_page_20.setGeometry(QtCore.QRect(80, 190, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page_20.setFont(font)
        self.name_start_page_20.setObjectName("name_start_page_20")
        self.label_54 = QtWidgets.QLabel(self.ipoteka)
        self.label_54.setGeometry(QtCore.QRect(370, 130, 91, 41))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.ipoteka)
        self.label_55.setGeometry(QtCore.QRect(370, 160, 71, 41))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.ipoteka)
        self.label_56.setGeometry(QtCore.QRect(470, 140, 431, 16))
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.ipoteka)
        self.label_57.setGeometry(QtCore.QRect(460, 200, 431, 16))
        self.label_57.setObjectName("label_57")
        self.name_start_page_21 = QtWidgets.QLabel(self.ipoteka)
        self.name_start_page_21.setGeometry(QtCore.QRect(420, 50, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page_21.setFont(font)
        self.name_start_page_21.setObjectName("name_start_page_21")
        self.logo_start_page_10 = QtWidgets.QLabel(self.ipoteka)
        self.logo_start_page_10.setGeometry(QtCore.QRect(130, 90, 101, 121))
        self.logo_start_page_10.setText("")
        self.logo_start_page_10.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo_start_page_10.setObjectName("logo_start_page_10")
        self.label_58 = QtWidgets.QLabel(self.ipoteka)
        self.label_58.setGeometry(QtCore.QRect(430, 170, 431, 16))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.ipoteka)
        self.label_59.setGeometry(QtCore.QRect(370, 190, 91, 41))
        self.label_59.setObjectName("label_59")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.ipoteka)
        self.lineEdit_6.setGeometry(QtCore.QRect(270, 380, 541, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_60 = QtWidgets.QLabel(self.ipoteka)
        self.label_60.setGeometry(QtCore.QRect(370, 110, 101, 31))
        self.label_60.setObjectName("label_60")
        self.name_start_page_22 = QtWidgets.QLabel(self.ipoteka)
        self.name_start_page_22.setGeometry(QtCore.QRect(360, 290, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_start_page_22.setFont(font)
        self.name_start_page_22.setObjectName("name_start_page_22")
        self.tabWidget.addTab(self.ipoteka, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_start_page.setText(_translate("MainWindow", "BAYMAX SAFETY SYSTEM"))
        self.lozung_star_page.setText(_translate("MainWindow", "ИИ на благо безопасности банкоматов мира"))
        self.version_start_page.setText(_translate("MainWindow", "Baymax Safety System. 2024 - 2025"))
        self.type_operation.setText(_translate("MainWindow", "ВЫБЕРИТЕ ТИП ОПЕРАЦИИ:"))
        self.get_money_button_start_page.setText(_translate("MainWindow", "Снять/положить деньги на карту"))
        self.get_credit_button_start_page.setText(_translate("MainWindow", "Оформить кредит"))
        self.get_ipoteka_button_start_page.setText(_translate("MainWindow", "Оформить ипотеку"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.start_page), _translate("MainWindow", "Стартовая страница"))
        self.name_start_page_2.setText(_translate("MainWindow", "BAYMAX SAFETY SYSTEM"))
        self.name_start_page_3.setText(_translate("MainWindow", "ВВЕДИТЕ ВСЕ НЕОБХОДИМЫЕ ДАННЫЕ: "))
        self.label.setText(_translate("MainWindow", "Номер карты: "))
        self.label_2.setText(_translate("MainWindow", "Дата истечения:"))
        self.label_3.setText(_translate("MainWindow", "CVV код: "))
        self.label_4.setText(_translate("MainWindow", "Пользователь: "))
        self.name_start_page_4.setText(_translate("MainWindow", "ЗАПОЛНИТЕ НИЖЕУКАЗАННУЮ ФОРМУ: "))
        self.label_5.setText(_translate("MainWindow", card))
        self.label_6.setText(_translate("MainWindow", f"{date}"))
        self.label_7.setText(_translate("MainWindow", f"{cvv}"))
        self.label_8.setText(_translate("MainWindow", f"{surname} {name}"))
        self.radioButton.setText(_translate("MainWindow", "Снять деньги"))
        self.radioButton_2.setText(_translate("MainWindow", "Получить деньги"))
        self.label_9.setText(_translate("MainWindow", "Введите сумму: "))
        self.pushButton.setText(_translate("MainWindow", "ВЫПОЛНИТЬ ЗАПРОС"))
        self.label_10.setText(_translate("MainWindow", "Запрос выполнится в течение 1-2 минут..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.get_money), _translate("MainWindow", "Снять/получить деньги"))
        self.label_41.setText(_translate("MainWindow", "Номер карты: "))
        self.label_42.setText(_translate("MainWindow", "Дата истечения:"))
        self.label_43.setText(_translate("MainWindow", "Пользователь: "))
        self.label_44.setText(_translate("MainWindow", "CVV код: "))
        self.name_start_page_17.setText(_translate("MainWindow", "BAYMAX SAFETY SYSTEM"))
        self.name_start_page_18.setText(_translate("MainWindow", "ВВЕДИТЕ ВСЕ НЕОБХОДИМЫЕ ДАННЫЕ: "))
        self.label_45.setText(_translate("MainWindow", f"{date}"))
        self.label_46.setText(_translate("MainWindow", f"{surname} {name}"))
        self.label_47.setText(_translate("MainWindow", "Введите сумму: "))
        self.pushButton_5.setText(_translate("MainWindow", "ВЫПОЛНИТЬ ЗАПРОС"))
        self.label_48.setText(_translate("MainWindow", f"{card}"))
        self.label_49.setText(_translate("MainWindow", "Запрос выполнится в течение 1-2 минут..."))
        self.name_start_page_19.setText(_translate("MainWindow", "ЗАПОЛНИТЕ НИЖЕУКАЗАННУЮ ФОРМУ: "))
        self.label_50.setText(_translate("MainWindow", f"{cvv}"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.credit), _translate("MainWindow", "Кредит"))
        self.label_51.setText(_translate("MainWindow", "Запрос выполнится в течение 1-2 минут..."))
        self.label_52.setText(_translate("MainWindow", f"{card}"))
        self.pushButton_6.setText(_translate("MainWindow", "ВЫПОЛНИТЬ ЗАПРОС"))
        self.label_53.setText(_translate("MainWindow", "Введите сумму: "))
        self.name_start_page_20.setText(_translate("MainWindow", "BAYMAX SAFETY SYSTEM"))
        self.label_54.setText(_translate("MainWindow", "Дата истечения:"))
        self.label_55.setText(_translate("MainWindow", "CVV код: "))
        self.label_56.setText(_translate("MainWindow", f"{date}"))
        self.label_57.setText(_translate("MainWindow", f"{surname} {name}"))
        self.name_start_page_21.setText(_translate("MainWindow", "ВВЕДИТЕ ВСЕ НЕОБХОДИМЫЕ ДАННЫЕ: "))
        self.label_58.setText(_translate("MainWindow", f"{cvv}"))
        self.label_59.setText(_translate("MainWindow", "Пользователь: "))
        self.label_60.setText(_translate("MainWindow", "Номер карты: "))
        self.name_start_page_22.setText(_translate("MainWindow", "ЗАПОЛНИТЕ НИЖЕУКАЗАННУЮ ФОРМУ: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ipoteka), _translate("MainWindow", "Ипотека"))


def run_userCabinet(user_info=()):
    global name, surname, card, cvv, date
    name = user_info[0]
    surname = user_info[1]
    card = user_info[2]
    card = card[:-7] + '*******'
    cvv = user_info[3]
    cvv = cvv[0] + '**'
    date = user_info[4]
    date = date[:3] + '**'
    print('! ', name, surname, card, date, cvv)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UserCabinet()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UserCabinet()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
