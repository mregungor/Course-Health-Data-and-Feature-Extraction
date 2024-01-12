from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res
import sqlite3
import os

from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 565)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
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
        self.label_3.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(390, 110, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.nameText = QtWidgets.QLineEdit(Form)
        self.nameText.setGeometry(QtCore.QRect(350, 180, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameText.setFont(font)
        self.nameText.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.nameText.setObjectName("nameText")
        self.registerButton = QtWidgets.QPushButton(Form)
        self.registerButton.setGeometry(QtCore.QRect(360, 360, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("QPushButton#registerButton{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#registerButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton#registerButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.512438, y1:0.506, x2:1, y2:1, stop:0 rgba(255, 98, 166, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.registerButton.setObjectName("registerButton")
        # Kayıt Ol butonuna sinyal bağla
        self.registerButton.clicked.connect(self.kayit_ol)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 390, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.clicked.connect(Form.close)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 410, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius;\n"
"\n"
"QPushButton#pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.512438, y1:0.506, x2:1, y2:1, stop:0 rgba(255, 98, 166, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lastnameText = QtWidgets.QLineEdit(Form)
        self.lastnameText.setGeometry(QtCore.QRect(460, 180, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lastnameText.setFont(font)
        self.lastnameText.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lastnameText.setObjectName("lastnameText")
        self.usernameText = QtWidgets.QLineEdit(Form)
        self.usernameText.setGeometry(QtCore.QRect(350, 260, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usernameText.setFont(font)
        self.usernameText.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.usernameText.setObjectName("usernameText")
        self.passwordText = QtWidgets.QLineEdit(Form)
        self.passwordText.setGeometry(QtCore.QRect(460, 260, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordText.setFont(font)
        self.passwordText.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.passwordText.setObjectName("passwordText")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(415, 435, 91, 20))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.nameText.raise_()
        self.registerButton.raise_()
        self.pushButton_5.raise_()
        self.lastnameText.raise_()
        self.usernameText.raise_()
        self.passwordText.raise_()
        self.label_5.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def kayit_ol(self):
        ad = self.nameText.text()
        soyad = self.lastnameText.text()
        tc_kimlik = self.usernameText.text()
        sifre = self.passwordText.text()

        if ad and soyad and tc_kimlik and sifre:
            self.kayit_ekle(ad, soyad, tc_kimlik, sifre)
        else:
            QMessageBox.warning(None, 'Kayıt Hatası', 'KAYIT BAŞARISIZ')

    def kayit_ekle(self, ad, soyad, tc_kimlik, sifre):
        program_dizini = os.path.dirname(os.path.realpath(__file__))
        print("Veritabanı dosyası şu konumda kaydedildi:", program_dizini)

        veritabani_yolu = os.path.join(program_dizini, 'Breast-Cancer.db')

        vt = sqlite3.connect(veritabani_yolu)
        im = vt.cursor()

        try:
            im.execute("CREATE TABLE IF NOT EXISTS Kullanici_Data (ad TEXT, soyad TEXT, tc_kimlik TEXT, sifre TEXT)")
            im.execute("INSERT INTO Kullanici_Data (ad, soyad, tc_kimlik, sifre) VALUES (?, ?, ?, ?)",
                       (ad, soyad, tc_kimlik, sifre))
            vt.commit()
            QMessageBox.information(None, 'Kayıt', 'KAYIT BAŞARILI')
        except sqlite3.Error as e:
            print("Veritabanı hatası:", e)
        finally:
            vt.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Kayıt Ol"))
        self.nameText.setPlaceholderText(_translate("Form", "Ad"))
        self.registerButton.setText(_translate("Form", "Kayıt Ol"))
        self.pushButton_2.setText(_translate("Form", "Tıkla"))
        self.pushButton_5.setText(_translate("Form", "Çıkış"))
        self.lastnameText.setPlaceholderText(_translate("Form", "Soyad"))
        self.usernameText.setPlaceholderText(_translate("Form", "TC Kimlik"))
        self.passwordText.setPlaceholderText(_translate("Form", "Şifre"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
