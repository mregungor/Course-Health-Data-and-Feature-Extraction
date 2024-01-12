from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QLabel, QPushButton, QMessageBox, QLineEdit
from PyQt5 import uic, QtWidgets
import cv2
import hashlib
from datetime import datetime
import sqlite3 as sql
# Veritabanı bağlantısı oluştur
conn = sql.connect('app.db')
cursor = conn.cursor()

# USERS tablosunu oluştur
cursor.execute('CREATE TABLE IF NOT EXISTS USERS ('
               'name TEXT,'
               'lastname TEXT,'
               'username TEXT UNIQUE,'
               'password TEXT,'
               'security_question TEXT,'
               'security_answer TEXT,'
               'userID INTEGER PRIMARY KEY AUTOINCREMENT)')
conn.commit()

# UserEmotions tablosunu oluştur
cursor.execute('CREATE TABLE IF NOT EXISTS UserEmotions ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'emotion_name TEXT,'
                'date TEXT,'
                'user_id INTEGER,'
                'FOREIGN KEY(user_id) REFERENCES USERS(userID)'
                ')')
conn.commit()


def encrypt_name_lastname(name, lastname):
    if not name or not lastname:
        return None
    encrypted_name = name[0] + hashlib.md5(name[1:].encode("UTF-8")).hexdigest()
    encrypted_lastname = lastname[0] + hashlib.md5(lastname[1:].encode("UTF-8")).hexdigest()
    return encrypted_name, encrypted_lastname

def encrypt_security_info(security_question, security_answer):
    if not security_question or not security_answer:
        return None
    encrypted_question = hashlib.md5(security_question.encode("UTF-8")).hexdigest()
    encrypted_answer = hashlib.md5(security_answer.encode("UTF-8")).hexdigest()
    return encrypted_question, encrypted_answer

def reset_password_in_database(username, new_password):
    try:
        hashed_password = hashlib.md5(new_password.encode("UTF-8")).hexdigest()
        cursor.execute("UPDATE USERS SET password = ? WHERE username = ?", (hashed_password, username))
        conn.commit()
        return True
    except Exception as e:
        print(f"Password reset failed: {e}")
        return False
class FormII(QWidget):  # kayıt ol
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\Sude\Desktop\proje\form2olan.ui", self)
        self.lineEdit_2.setReadOnly(True) #Kullanıcının belirli lineEditler üzerinde değişiklik yapmasını engeller
        self.lineEdit_3.setReadOnly(True)

        # QLabel'in arka plan resmini QSS ile ayarla
        self.label.setStyleSheet(
            'color: black; background-image: url("C:/Users/Sude/Desktop/proje/ekrang.png"); background-size: 100% 100%;')

        # "Homepage" butonuna basıldığında geri gitme işlevini bağla
        self.pushButton_2.clicked.connect(self.go_to_login_page)

        # "Save" butonuna basıldığında kullanıcı kaydını yap
        self.pushButton.clicked.connect(self.save_user)
        # Girilen şifrenin görünmesini engeller
        self.lineEdit_8.setEchoMode(QLineEdit.Password)
        self.lineEdit_10.setEchoMode(QLineEdit.Password)

    def go_to_login_page(self):
        # QStackedWidget'ın içinden hangi Widget'ın görüneceğini seçmek için setCurrentIndex ve parent() kullanılır
        self.parent().setCurrentIndex(0)

    def save_user(self):
        name = self.lineEdit.text()
        lastname = self.lineEdit_4.text()
        username = self.lineEdit_6.text()
        password = self.lineEdit_8.text()
        password_reenter = self.lineEdit_10.text()
        security_question = self.comboBox.currentText()
        security_answer = self.lineEdit_13.text()

        self.insert_to_db(name, lastname, username, password, password_reenter, security_question, security_answer)


    def insert_to_db(self, name, lastname, username, password, password_reenter, security_question, security_answer):
        anaSayfaResultStr = ""  # Ana sayfa sonuç string'ini temizle

        if not name or not lastname or not username or not password or not password_reenter or not security_question or not security_answer:
            anaSayfaResultStr = "Lütfen tüm bilgileri giriniz"
            QMessageBox.warning(self, "Hata", anaSayfaResultStr)
            return

        if password != password_reenter:
            anaSayfaResultStr = "Şifreler uyuşmuyor"
            QMessageBox.warning(self, "Hata", anaSayfaResultStr)
            return

        encrypted_name, encrypted_lastname = encrypt_name_lastname(name, lastname)
        hashed_password = hashlib.md5(password.encode("UTF-8")).hexdigest()
        encrypted_question, encrypted_answer = encrypt_security_info(security_question, security_answer)

        #kullanıcı kaydetme işlemi
        try:
            cursor.execute(
                "INSERT INTO USERS(name, lastname, username, password, security_question, security_answer) VALUES(?,?,?,?,?,?)",
                (encrypted_name, encrypted_lastname, username, hashed_password, encrypted_question, encrypted_answer))
            conn.commit()
            anaSayfaResultStr = "Kullanıcı başarıyla oluşturuldu"
            QMessageBox.information(self, "Başarı", anaSayfaResultStr)
        except sql.IntegrityError:
            anaSayfaResultStr = "Bu kullanıcı adı zaten kullanılıyor."
            QMessageBox.warning(self, "Hata", anaSayfaResultStr)
        except Exception as e:
            anaSayfaResultStr = "Bilinmeyen bir hata oluştu."
            QMessageBox.warning(self, "Hata", anaSayfaResultStr + f"\nHata Detayı: {e}")

    def perform_password_reset(self, username, security_question, security_answer, new_password):
        pass


class FormIII(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(620, 580)
        self.user_id = None  # Kullanıcı ID'sini tutmak için bir değişken

        # QLabel oluştur ve arkaplan resmini ayarla
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 620, 580)
        self.background_label.setStyleSheet("border-image: url('C:/Users/Sude/Desktop/proje/ekrang.png');")

        uic.loadUi(r"C:\Users\Sude\Desktop\proje\duygular.ui", self)

        # Kamera başlatma işlemi burada olmalı
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Kameranın başarıyla başlatılıp başlatılmadığını kontrol et
        if not self.camera.isOpened():
            print("Kamera başlatılamadı.")
            return

        # QPushButton'a bir fonksiyon bağla
        self.pushButton_7.clicked.connect(self.start_camera)

        # Duygu kaydı için QPushButton'lara bağlı işlevleri tanımla
        self.pushButton_1.clicked.connect(lambda: self.save_emotion("Sad"))
        self.pushButton_2.clicked.connect(lambda: self.save_emotion("Scared"))
        self.pushButton_3.clicked.connect(lambda: self.save_emotion("Furious"))
        self.pushButton_4.clicked.connect(lambda: self.save_emotion("Surprised"))
        self.pushButton_5.clicked.connect(lambda: self.save_emotion("Happy"))
        self.pushButton_6.clicked.connect(lambda: self.save_emotion("Disgusted"))

    def set_user_id(self, user_id):
        # Kullanıcı ID'sini ayarla
        self.user_id = user_id

    def save_emotion(self, emotion_name):
        try:
            # Kullanıcı ID'sini al
            if self.user_id is not None:
                user_id = self.user_id
            else:
                QMessageBox.warning(self, "Hata", "Kullanıcı ID'si bulunamadı")
                return

            # Tarih ve saat bilgisini al
            date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            # Duygu adını, tarihi ve kullanıcı ID'sini UserEmotions tablosuna ekleme
            cursor.execute("INSERT INTO UserEmotions(emotion_name, date, user_id) VALUES(?, ?, ?)",
                           (emotion_name, date, user_id))
            conn.commit() #kaydet

            # Başarı mesajını göster
            QMessageBox.information(self, "Başarı", f"{emotion_name} duygusu kaydedildi.")
        except Exception as e:
            # Hata durumunda hata mesajını göster
            QMessageBox.warning(self, "Hata", f"Hata oluştu: {e}")
    def start_camera(self):
        while True:
            # Görüntüyü al
            ret, frame = self.camera.read()
            if ret:
                # Alınan görüntüyü işleme sok, QLabel gibi bir widget üzerine yerleştir
                cv2.imshow("Kamera Görüntüsü", frame)

            # QCoreApplication.processEvents() çağrısı, PyQt'nin olay döngüsünü güncellemesine yardımcı olur
            QApplication.processEvents()

            # 'q' tuşuna basıldığında döngüyü sonlandır
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Kamera serbest bırakma
        self.camera.release()
        cv2.destroyAllWindows()

    def closeEvent(self, event):
        # Form kapatıldığında kamerayı serbest bırak
        if hasattr(self, 'camera') and self.camera.isOpened():
            self.camera.release()
        event.accept()
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(480, 580)
        self.stacked_widget = QStackedWidget(self)

        self.form_i = QWidget()
        self.form_i_ui = uic.loadUi(r"C:\Users\Sude\Desktop\proje\Son2.ui", self.form_i)
        self.stacked_widget.addWidget(self.form_i)

        self.form_ii = FormII()
        self.stacked_widget.addWidget(self.form_ii)

        self.form_iii = FormIII()
        self.stacked_widget.addWidget(self.form_iii)

        self.anaSayfaResultStr = ""
        self.sifremiUnuttumResultStr = ""
        self.reset_password_form = ResetPassword(cursor, conn, self.anaSayfaResultStr, self.sifremiUnuttumResultStr)
        self.stacked_widget.addWidget(self.reset_password_form)

        self.form_i_ui.pushButton.clicked.connect(self.check_login)
        self.form_i_ui.pushButton_2.clicked.connect(self.show_form_ii)
        self.form_i_ui.pushButton_3.clicked.connect(self.show_password_reset_form)

        self.set_styles()

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        self.stacked_widget.setCurrentIndex(0)
        self.show()

    def set_styles(self):
        self.form_i_ui.pushButton.setStyleSheet('color: black;')
        self.form_i_ui.pushButton_2.setStyleSheet('color: black;')
        self.form_i_ui.pushButton_3.setStyleSheet('color: black;')
        self.form_i_ui.lineEdit.setStyleSheet('color: black;')
        self.form_i_ui.lineEdit_2.setStyleSheet('color: black;')

        # QLabel'in arka plan resmini QSS ile ayarla
        self.form_i_ui.label.setStyleSheet(
            'color: black; background-image: url("C:/Users/Sude/Desktop/proje/ekrang.png");')

    def show_form_ii(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_form_iii(self):
        self.stacked_widget.setCurrentIndex(2)

    def check_login(self):
        anaSayfaResultStr = ""
        username = self.form_i_ui.lineEdit.text()
        password = self.form_i_ui.lineEdit_2.text()

        # Veritabanında kullanıcı kontrolü
        cursor.execute("SELECT userID, password FROM USERS WHERE username = ?", (username,))
        user_data = cursor.fetchone()

        if user_data is None:
            QMessageBox.warning(self, "Warning", "Kullanıcı bulunamadı")
        else:
            user_id, stored_password = user_data
            hashed_password = hashlib.md5(password.encode("UTF-8")).hexdigest()

            if stored_password == hashed_password:
                self.form_iii.set_user_id(user_id)
                self.stacked_widget.setCurrentIndex(2)  # duygular.ui göster
            else:
                QMessageBox.warning(self, "Warning", "Şifre yanlış girildi")

    def show_password_reset_form(self):
        # Şifre sıfırlama sayfasını göster
        self.reset_password_form.clear_inputs()  # Giriş alanlarını temizle
        self.stacked_widget.setCurrentIndex(3)  # ResetPassword formunu göster
        self.reset_password_form.setFocus()  # ResetPassword formuna odaklan
class ResetPassword(QWidget):
    def __init__(self, cursor, conn, anaSayfaResultStr, sifremiUnuttumResultStr):
        super(ResetPassword, self).__init__()

        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(0, 0, 500, 600)
        self.bg_label.setStyleSheet(
            'background-image: url("C:/Users/Sude/Desktop/proje/resetpassword.jpg"); background-size: cover;')

        uic.loadUi(r"C:\Users\Sude\Desktop\proje\resetpassword.ui", self)


        # Kullanıcıya geri bildirim göstermek için sonuç string'lerini tutuyoruz
        self.anaSayfaResultStr = anaSayfaResultStr
        self.sifremiUnuttumResultStr = sifremiUnuttumResultStr

        # Şifre girişi alanlarını gizle
        self.lineEdit_8.setEchoMode(QLineEdit.Password)
        self.lineEdit_10.setEchoMode(QLineEdit.Password)

        # "Reset Password" butonuna basıldığında perform_password_reset fonksiyonunu çağır
        self.pushButton.clicked.connect(self.perform_password_reset)
        # "Homepage" butonuna basıldığında geri gitme işlevini bağla
        self.pushButton_2.clicked.connect(self.go_to_home_page)
        # Kullanıcı adı, güvenlik sorusu ve cevabını tutmak için değişkenler
        self.username = ""
        self.security_question = ""
        self.security_answer = ""

        # Veritabanı bağlantısı ve cursor
        self.cursor = cursor
        self.conn = conn
        self.clear_results()


    def save_user(self):
        # Forget Password işlemi için kullanıcı adını al
        forget_password_username = self.forget_password_username_edit.text()

        # Girilen yeni şifreleri al
        new_password = self.lineEdit_8.text()
        new_password_reenter = self.lineEdit_10.text()

        # Girilen güvenlik soru ve cevapları al
        security_question = self.comboBox.currentText()
        security_answer = self.lineEdit_13.text()

        # FormII sınıfındaki kullanıcı adını ve diğer bilgileri ResetPassword sınıfına geçir
        self.parent().reset_password_form.set_user_info(forget_password_username, security_question, security_answer)

        # Şifre sıfırlama işlemini gerçekleştir
        self.perform_password_reset(forget_password_username, security_question, security_answer, new_password, new_password_reenter)

    def set_user_info(self, username, security_question, security_answer):
        # Kullanıcı bilgilerini ayarla
        self.username = username
        self.security_question = security_question
        self.security_answer = security_answer

    def perform_password_reset(self):
        self.clear_results()

        # Girilen yeni şifreleri al
        new_password = self.lineEdit_8.text()
        new_password_reenter = self.lineEdit_10.text()

        # Girilen güvenlik soru ve cevapları al
        security_question = self.comboBox.currentText()
        security_answer = self.lineEdit_13.text()

        # Kullanıcı adını al
        username = self.lineEdit_6.text()

        if not username or not new_password or not new_password_reenter or not security_question or not security_answer:
            self.show_result("Lütfen tüm bilgileri giriniz")
            return

        try:
            # Veritabanından kullanıcının güvenlik sorusunu ve cevabını al
            self.cursor.execute(
                "SELECT username, security_question, security_answer, password FROM USERS WHERE username = ?",
                (username,))
            user_data = self.cursor.fetchone() #sorgulama, fetchone() sonuçlardan sadece birinin alınmasını sağlar

            if user_data is None:
                self.show_result("Kullanıcı adı bulunamadı")
                return

            stored_username, stored_security_question, stored_security_answer, stored_encrypted_password = user_data

            # Güvenlik bilgilerini kontrol et
            #lower() küçük büyük harf hatasına takılmamayı sağlar
            if stored_security_answer.lower() != hashlib.md5(
                    security_answer.encode("UTF-8")).hexdigest():
                self.show_result("Güvenlik bilgileri uyuşmuyor")
                return

            # Şifre kontrolü
            if new_password != new_password_reenter:
                self.show_result("Şifreler uyuşmuyor")
                return

            # Şifreyi güncelle
            hashed_password = hashlib.md5(new_password.encode("UTF-8")).hexdigest()
            self.cursor.execute("UPDATE USERS SET password = ? WHERE username = ?",
                                (hashed_password, username))
            self.conn.commit()

            if new_password == new_password_reenter:
                self.show_result("Şifre başarıyla değiştirilmiştir")
            else:
                self.show_result("Şifreler aynı değil")

        except Exception as e:
            print(f"Bilinmeyen Hata: {e}")
            self.show_result(f"Bilinmeyen Hata: {e}")

    def check_security_info(input_question, stored_question, input_answer, stored_answer):
        # Kullanıcının girdiği güvenlik sorusunu ve cevabını şifreleme algoritmasıyla karşılaştır
        encrypted_input_question = hashlib.md5(input_question.encode("UTF-8")).hexdigest()
        encrypted_input_answer = hashlib.md5(input_answer.encode("UTF-8")).hexdigest()

        return encrypted_input_question == stored_question and encrypted_input_answer == stored_answer

    def clear_inputs(self):
        # Giriş alanlarını temizle
        self.lineEdit_8.clear()
        self.lineEdit_10.clear()

    def clear_results(self):
        # Sonuç string'lerini temizle
        self.anaSayfaResultStr = ""
        self.sifremiUnuttumResultStr = ""

    def show_result(self, message):
        # Sonuçları göster
        QMessageBox.warning(self, "Hata", message)

    def go_to_home_page(self):
        # QStackedWidget'ın indeksini ayarla
        self.parent().setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()