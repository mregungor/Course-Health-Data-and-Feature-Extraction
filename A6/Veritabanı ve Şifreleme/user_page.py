from PyQt5.QtWidgets import QApplication, QMainWindow, QDateEdit, QLabel, QPushButton, QListWidget
from PyQt5.QtCore import Qt, QDate, QRect
import sqlite3 as sql
from notesandemotions import Ui_Form

# Veritabanı bağlantısı oluştur
conn = sql.connect('app.db')
cursor = conn.cursor()
class MyApp(QMainWindow, Ui_Form):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.cursor = cursor

        today = QDate.currentDate() #Bugünün tarihini tutma

        # Tarih seçici (QDateEdit) için özelliklerin ayarlanması
        self.dateEdit = QDateEdit(self)
        self.dateEdit.setGeometry(QRect(100, 70, 140, 25))
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDateRange(today.addDays(-365), today.addDays(365))

        # Kullanıcıya bilgi veren etiket (QLabel) ve stil ayarları
        self.label = QLabel("Geçmiş notunuzu görmek için tarih seçiniz:", self)
        self.label.setStyleSheet("color: rgb(0, 66, 48);")
        self.label.setGeometry(QRect(60, 40, 300, 30))

        # Kullanıcıya mesaj veren etiket (QLabel) ve stil ayarları
        self.messageLabel = QLabel("", self)
        self.messageLabel.setStyleSheet("color: green; font-size: 10pt;")
        self.messageLabel.setGeometry(QRect(140, 250, 300, 30))

        # Göster butonu (QPushButton) ve özelliklerin ayarlanması
        self.pushButton = QPushButton("Göster", self)
        self.pushButton.setGeometry(QRect(250, 70, 80, 25))
        self.pushButton.clicked.connect(self.show_note_and_emotion)

        # Liste widget (QListWidget) ve özelliklerin ayarlanması
        self.listWidget = QListWidget(self)  # listWidget ekleyin
        self.listWidget.setGeometry(QRect(60, 150, 200, 200))  # uygun bir konum ve boyut ekleyin
        self.listWidget.hide()  # ListWidget'i başlangıçta gizle

#Veritabanından notların sorgulanması
    def show_note_and_emotion(self):
        # Kullanıcıdan seçilen tarihi al
        selected_date = self.dateEdit.date().toString(Qt.ISODate)
        self.cursor.execute('SELECT notebook, emotionEntry FROM USERDATA WHERE entryDate = ?', (selected_date,))
        result = self.cursor.fetchall()

        # ListWidget'i temizle
        self.listWidget.clear()
        if result:
            # Notları ve duyguları ListWidget'e ekle
            for note, emotion in result:
                self.listWidget.addItem(f"Not: {note}")
            self.listWidget.show()  # ListWidget'i görünür yap
            self.messageLabel.clear()
        else:
            self.listWidget.hide()  # Not bulunamadığında ListWidget'i gizle
            self.messageLabel.setText("Burası boş görünüyor.")

if __name__ == "__main__":
    app = QApplication([])  # PyQt uygulama nesnesini oluştur
    window = MyApp()  # MyApp sınıfından bir pencere (window) oluştur
    window.show()  # Pencereyi göster
    app.exec_()  # Uygulamayı başlat ve olay döngüsünü başlat