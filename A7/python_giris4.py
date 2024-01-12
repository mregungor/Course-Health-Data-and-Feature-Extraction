from PyQt5 import QtCore, QtGui, QtWidgets
from python_kayit7 import Ui_Form as Ui_python_kayit7
from python_deger2 import Ui_Form as Ui_python_deger2
import sys, res
import sqlite3 as sql
from PyQt5.QtWidgets import QLineEdit
from veritabani import *

class Ui_Form(object):
    def yeniac(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_python_kayit7()
        self.ui.setupUi(self.window)
        self.window.show()

    def basarili(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_python_deger2()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 565)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.clicked.connect(self.yeniac)
        self.loginText = QtWidgets.QPushButton(Form)
        self.loginText.clicked.connect(self.basarili)
        self.label.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.label.setStyleSheet("QPushButton#pushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:5px;\n"
            "}\n"
            "\n"
            "QPushButton#pushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "QPushButton#pushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 280, 430))
        self.label_2.setStyleSheet("border-image: url(:/image/cancer.jpg);\n"
            "background-color:rgba(0 ,0 ,0 ,80);\n"
            "border-top-left-radius: 50px\n"
            "")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(340, 70, 240, 430))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(410, 110, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.usernameText2 = QtWidgets.QLineEdit(Form)
        self.usernameText2.setGeometry(QtCore.QRect(350, 190, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usernameText2.setFont(font)
        self.usernameText2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(0, 0, 0, 240);\n"
            "padding-bottom:7px;")
        self.usernameText2.setObjectName("usernameText2")
        self.passwordText2 = QtWidgets.QLineEdit(Form)
        self.passwordText2.setGeometry(QtCore.QRect(350, 260, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordText2.setFont(font)
        self.passwordText2.setEchoMode(QLineEdit.Password)
        self.passwordText2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
            "color:rgba(0, 0, 0, 240);\n"
            "padding-bottom:7px;")
        self.passwordText2.setObjectName("passwordText2")
        self.loginText = QtWidgets.QPushButton(Form)
        self.loginText.setGeometry(QtCore.QRect(350, 340, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.loginText.setFont(font)
        self.loginText.setStyleSheet("QPushButton#loginText{\n"
            "    background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:5px;\n"
            "}\n"
            "\n"
            "QPushButton#loginText:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "\n"
            "QPushButton#loginText:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0.512438, y1:0.506, x2:1, y2:1, stop:0 rgba(255, 98, 166, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}")
        self.loginText.setObjectName("loginText")
        self.loginText.clicked.connect(self.giris)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(400, 390, 71, 16))
        self.label_5.setStyleSheet("font: 63 8pt \"Segoe UI\";\n"
            "font: 8pt \"Segoe UI Symbol\";")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 390, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4.setGeometry(QtCore.QRect(468, 389, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 460, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.clicked.connect(Form.close)
        self.pushButton_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-radius;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.usernameText2.raise_()
        self.passwordText2.raise_()
        self.loginText.raise_()
        self.label_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def giris(self):
        tc_kimlik = self.usernameText2.text()
        sifre = self.passwordText2.text()

        arama = kullanici_ara(tc_kimlik)
        if arama is None:
            QMessageBox.information(None, 'Giriş', 'GİRİŞ BAŞARISIZ - Kullanıcı Bulunamadı')
        elif sifre == arama[3]:
            QMessageBox.information(None, 'Giriş', 'GİRİŞ BAŞARILI / Eminseniz tekrar tıklayın :D')
            self.loginText.clicked.connect(self.basarili)
        else:
            QMessageBox.critical(None, 'Giriş Hatası', 'Giriş Başarısız - Şifre Hatalı', QMessageBox.Ok)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Giriş"))
        self.usernameText2.setPlaceholderText(_translate("Form", "Kullanıcı Adı"))
        self.passwordText2.setPlaceholderText(_translate("Form", "Şifre"))
        self.loginText.setText(_translate("Form", "Giriş Yap"))
        self.label_5.setText(_translate("Form", "KAYIT İÇİN"))
        self.pushButton_2.setText(_translate("Form", "Tıkla"))
        self.pushButton_4.setText(_translate("Form", "Tıkla"))
        self.pushButton_5.setText(_translate("Form", "Çıkış"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
