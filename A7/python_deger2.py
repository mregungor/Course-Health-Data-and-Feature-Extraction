from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res
from userdataa import *
from python_bosEkran import Ui_Form as Ui_python_bosEkran
from tahmin import *
from userdataa import *
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def hastalarim(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_python_bosEkran()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 565)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.goruntule_Button = QtWidgets.QPushButton(Form)
        self.goruntule_Button.clicked.connect(self.hastalarim)
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
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 491, 431))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(160, 110, 281, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.ort_Yaricap = QtWidgets.QLineEdit(Form)
        self.ort_Yaricap.setGeometry(QtCore.QRect(90, 170, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ort_Yaricap.setFont(font)
        self.ort_Yaricap.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.ort_Yaricap.setObjectName("ort_Yaricap")
        self.sonuc_Button = QtWidgets.QPushButton(Form)
        self.sonuc_Button.setGeometry(QtCore.QRect(200, 350, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sonuc_Button.setFont(font)
        self.sonuc_Button.setStyleSheet("QPushButton#sonuc_Button{\n"
"    background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#sonuc_Button:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton#sonuc_Button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.512438, y1:0.506, x2:1, y2:1, stop:0 rgba(255, 98, 166, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.sonuc_Button.setObjectName("sonuc_Button")
        self.sonuc_Button.clicked.connect(self.deger)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 390, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 450, 81, 31))
        self.pushButton_5.clicked.connect(Form.close)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.ort_Alan = QtWidgets.QLineEdit(Form)
        self.ort_Alan.setGeometry(QtCore.QRect(90, 230, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ort_Alan.setFont(font)
        self.ort_Alan.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.ort_Alan.setObjectName("ort_Alan")
        self.ort_Icbukey = QtWidgets.QLineEdit(Form)
        self.ort_Icbukey.setGeometry(QtCore.QRect(320, 230, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ort_Icbukey.setFont(font)
        self.ort_Icbukey.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.ort_Icbukey.setObjectName("ort_Icbukey")
        self.ort_Cevre = QtWidgets.QLineEdit(Form)
        self.ort_Cevre.setGeometry(QtCore.QRect(320, 170, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ort_Cevre.setFont(font)
        self.ort_Cevre.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.ort_Cevre.setObjectName("ort_Cevre")
        self.ort_IcbukeyNoktalar = QtWidgets.QLineEdit(Form)
        self.ort_IcbukeyNoktalar.setGeometry(QtCore.QRect(200, 290, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ort_IcbukeyNoktalar.setFont(font)
        self.ort_IcbukeyNoktalar.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.ort_IcbukeyNoktalar.setObjectName("ort_IcbukeyNoktalar")
        self.label_isim = QtWidgets.QLabel(Form)
        self.label_isim.setGeometry(QtCore.QRect(70, 80, 91, 16))
        self.label_isim.setText("")
        self.label_isim.setObjectName("label_isim")
        self.label_tc = QtWidgets.QLabel(Form)
        self.label_tc.setGeometry(QtCore.QRect(410, 80, 121, 16))
        self.label_tc.setText("")
        self.label_tc.setObjectName("label_tc")
        self.goruntule_Button = QtWidgets.QPushButton(Form)
        self.goruntule_Button.setGeometry(QtCore.QRect(220, 400, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.goruntule_Button.setFont(font)
        self.goruntule_Button.setStyleSheet("QPushButton#goruntule_Button{\n"
"    background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#goruntule_Button:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton#goruntule_Button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.512438, y1:0.506, x2:1, y2:1, stop:0 rgba(255, 98, 166, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.goruntule_Button.setObjectName("goruntule_Button")
        self.goruntule_Button.clicked.connect(self.hastalarim)
        self.isim_Soyisim = QtWidgets.QLineEdit(Form)
        self.isim_Soyisim.setGeometry(QtCore.QRect(80, 80, 131, 22))
        self.isim_Soyisim.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.isim_Soyisim.setObjectName("isim_Soyisim")
        self.pushButton_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.ort_Yaricap.raise_()
        self.sonuc_Button.raise_()
        self.pushButton_5.raise_()
        self.ort_Alan.raise_()
        self.ort_Icbukey.raise_()
        self.ort_Cevre.raise_()
        self.ort_IcbukeyNoktalar.raise_()
        self.label_isim.raise_()
        self.label_tc.raise_()
        self.goruntule_Button.raise_()
        self.isim_Soyisim.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def deger(self):
        isim_Soyisim = self.isim_Soyisim.text()
        Ortalama_Yarıçap = self.ort_Yaricap.text()
        Ortalama_Çevresi = self.ort_Cevre.text()
        Ortalama_Alan = self.ort_Alan.text()
        Ortalama_İçbükeylik = self.ort_Icbukey.text()
        Ortalama_İçbükey_Noktalar = self.ort_IcbukeyNoktalar.text()

        tahmin_sonuc = tahmin_yap(Ortalama_İçbükey_Noktalar,Ortalama_Alan,Ortalama_Yarıçap,Ortalama_Çevresi,Ortalama_İçbükeylik)
        Tumor_Huy = tahmin_sonuc

        userData_ekle(isim_Soyisim,Tumor_Huy,Ortalama_Yarıçap, Ortalama_Çevresi, Ortalama_Alan, Ortalama_İçbükeylik, Ortalama_İçbükey_Noktalar)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Değerleri Giriniz"))
        self.ort_Yaricap.setPlaceholderText(_translate("Form", "Ortalama Yarıçap"))
        self.sonuc_Button.setText(_translate("Form", "Sonucu Görüntüle"))
        self.pushButton_2.setText(_translate("Form", "Tıkla"))
        self.pushButton_5.setText(_translate("Form", "Çıkış"))
        self.ort_Alan.setPlaceholderText(_translate("Form", "Ortalama Alan"))
        self.ort_Icbukey.setPlaceholderText(_translate("Form", "Ortalama İçbükey"))
        self.ort_Cevre.setPlaceholderText(_translate("Form", "Ortalama Çevre"))
        self.ort_IcbukeyNoktalar.setPlaceholderText(_translate("Form", "Ortalama İçbükey Noktalar"))
        self.goruntule_Button.setText(_translate("Form", "Hastalarım"))
        self.isim_Soyisim.setPlaceholderText(_translate("Form", "Hasta İsim-Soyisim"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
