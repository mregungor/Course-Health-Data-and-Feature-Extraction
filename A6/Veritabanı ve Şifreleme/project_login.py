from tkinter import * #GUI Tasarım
import hashlib #Şifreleme
import sqlite3 as sql #Veritabanı işlemi
import tkinter as tk
from menus import KayitUygulamasi

# Veritabanı bağlantısı oluştur
conn = sql.connect('app.db')
cursor = conn.cursor()

# USERS tablosunu oluştur
cursor.execute('CREATE TABLE IF NOT EXISTS USERS ('
               'name TEXT,'
               'lastname TEXT,'
               'username TEXT UNIQUE,' # Her kullanıcı adının benzersiz olmasını sağlar
               'password TEXT,'
               'security_question TEXT,'
               'security_answer TEXT,'
               'userID INTEGER PRIMARY KEY AUTOINCREMENT)') # Otomatik olarak artan bir kullanıcı kimlik numarası
conn.commit()

def cikis_yap():
    root.destroy()

#güncellenen kısım
# İsim ve soyisimin ilk harfleri hariç kalan kısımlarını şifreleme fonksiyonu
def encrypt_name_lastname(name, lastname):
    if not name or not lastname:
        return None
    encrypted_name = name[0] + hashlib.md5(name[1:].encode("UTF-8")).hexdigest()
    encrypted_lastname = lastname[0] + hashlib.md5(lastname[1:].encode("UTF-8")).hexdigest()
    return encrypted_name, encrypted_lastname

# Güvenlik sorusu ve cevabını şifreleme fonksiyonu
def encrypt_security_info(security_question, security_answer):
    if not security_question or not security_answer:
        return None
    encrypted_question = hashlib.md5(security_question.encode("UTF-8")).hexdigest()
    encrypted_answer = hashlib.md5(security_answer.encode("UTF-8")).hexdigest()
    return encrypted_question, encrypted_answer

# Ana pencereyi oluştur
root = Tk()
root.geometry("720x480")
root.configure(bg='#e6e6ff')

#sayfalardaki hata yazıları
global resultStr
resultStr = StringVar()
global sifremiUnuttumResultStr
sifremiUnuttumResultStr = StringVar()
global anaSayfaResultStr
anaSayfaResultStr = StringVar()

# Kullanıcı eklemek için fonksiyon
def insertToDb(name, lastname, username, password, password_reenter, security_question, security_answer):
    anaSayfaResultStr.set("")
    resultStr.set("")

    if not name or not lastname or not username or not password or not password_reenter or not security_question or not security_answer:
        resultStr.set("Lütfen tüm bilgileri giriniz")
        return
    if password != password_reenter:
        resultStr.set("Şifreler uyuşmuyor")
        return

    encrypted_name, encrypted_lastname = encrypt_name_lastname(name, lastname)
    hashedPassword = hashlib.md5(password.encode("UTF-8")).hexdigest()
    encrypted_question, encrypted_answer = encrypt_security_info(security_question, security_answer)

    try:
        cursor.execute(
            "INSERT INTO USERS(name, lastname, username, password, security_question, security_answer) VALUES(?,?,?,?,?,?)",
            (encrypted_name, encrypted_lastname, username, hashedPassword, encrypted_question, encrypted_answer))
        resultStr.set("Kullanıcı oluşturuldu")
        conn.commit()
        resultStr.set("Kullanıcı oluşturuldu")
        print("Kullanıcı oluşturuldu")
    except sql.IntegrityError:
        resultStr.set("Bu kullanıcı adı zaten kullanılıyor.")

# Yeni kullanıcı ekleme sayfasını oluşturmak için fonksiyon
def yeniKullaniciEklemeSayfasi():
    anaSayfaResultStr.set("")
    yeniKullanici = Frame(root, bg='#e6e6ff')

    yeniKullanici.place(relx=0.5, rely=0.5, anchor=CENTER)
    kayitol_label = Label(yeniKullanici, text="Kayıt Ol", font=("Times New Roman", 14, 'bold'), bg='#e6e6ff',
                              fg='#566573')
    kayitol_label.grid(row=0, column=1, padx=5, pady=5)
    nameLabel = Label(yeniKullanici, text="İsim:", bg='#e6e6ff')
    nameEntry = Entry(yeniKullanici, width=30)
    nameLabel.grid(row=1, column=0, padx=5, pady=5)
    nameEntry.grid(row=1, column=1, padx=5, pady=5)

    lastnameLabel = Label(yeniKullanici, text="Soyisim:", bg='#e6e6ff')
    lastnameEntry = Entry(yeniKullanici, width=30)
    lastnameLabel.grid(row=2, column=0, padx=5, pady=5)
    lastnameEntry.grid(row=2, column=1, padx=5, pady=5)

    usernameLabel = Label(yeniKullanici, text="Kullanıcı Adı:", bg='#e6e6ff')
    usernameEntry = Entry(yeniKullanici, width=30)
    usernameLabel.grid(row=3, column=0, padx=5, pady=5)
    usernameEntry.grid(row=3, column=1, padx=5, pady=5)

    passwordLabel = Label(yeniKullanici, text="Şifre:", bg='#e6e6ff')
    passwordEntry = Entry(yeniKullanici, width=30, show="*")
    passwordLabel.grid(row=4, column=0, padx=5, pady=5)
    passwordEntry.grid(row=4, column=1, padx=5, pady=5)

    passwordReenterLabel = Label(yeniKullanici, text="Şifre Tekrar:", bg='#e6e6ff')
    passwordReenterEntry = Entry(yeniKullanici, width=30, show="*")
    passwordReenterLabel.grid(row=5, column=0, padx=5, pady=5)
    passwordReenterEntry.grid(row=5, column=1, padx=5, pady=5)

    securityLabel = Label(yeniKullanici, text="(Cevabınızı buraya giriniz)", bg='#e6e6ff')
    securityLabel.grid(row=6, column=0, padx=5, pady=5)
    security_question = StringVar()
    security_question.set("İlk evcil hayvanınızın adı")
    securityDropdown = OptionMenu(yeniKullanici, security_question, "İlk evcil hayvanınızın adı",
                                  "İlkokuldaki öğretmeninizin adı", "En sevdiğiniz renk")
    securityDropdown.grid(row=6, column=1, padx=5, pady=5)

    securityAnswerLabel = Label(yeniKullanici, text="Güvenlik Sorusu Cevabı:", bg='#e6e6ff')
    securityAnswerEntry = Entry(yeniKullanici, width=30)
    securityAnswerLabel.grid(row=7, column=0, padx=5, pady=5)
    securityAnswerEntry.grid(row=7, column=1, padx=5, pady=5)

    result = Label(yeniKullanici, textvariable=resultStr, bg='#e6e6ff', fg="black", font=('Calibri', 11, 'bold'))
    result.grid(row=8, columnspan=2, padx=5, pady=5)
    bos_label = Label(yeniKullanici, text="", font=("Helvetica", 10), bg='#e6e6ff')
    bos_label.grid(row=7, column=3, padx=5, pady=5)
    bos_label = Label(yeniKullanici, text="", font=("Helvetica", 10), bg='#e6e6ff')
    bos_label.grid(row=7, column=4, padx=5, pady=5)
    bos_label = Label(yeniKullanici, text="", font=("Helvetica", 10), bg='#e6e6ff')
    bos_label.grid(row=7, column=5, padx=5, pady=5)

    enter = Button(yeniKullanici, text="Kayıt Ol", bg="green", fg="white",
                   command=lambda: insertToDb(nameEntry.get(), lastnameEntry.get(), usernameEntry.get(),
                                              passwordEntry.get(), passwordReenterEntry.get(), security_question.get(),
                                              securityAnswerEntry.get()))
    enter.grid(row=9, columnspan=2, padx=5, pady=5)

    back = Button(yeniKullanici, text="Geri dön", bg="red", fg="white", command=lambda: resultStr.set("") or yeniKullanici.place_forget())
    back.grid(row=10, columnspan=2, padx=5, pady=5)

anaSayfaResultStr.set("")
resultLabel = Label(root, textvariable=anaSayfaResultStr, bg='#e6e6ff', fg="black", font=('Calibri', 11, 'bold'))
resultLabel.place(relx=0.45, rely=0.85, anchor=CENTER)

# Ana sayfada kullanıcı kimlik doğrulama fonksiyonu
def auth(username, password):
    anaSayfaResultStr.set("")

    #veritabanında kullanıcı kontrolü
    cursor.execute("SELECT userID, password FROM USERS WHERE username = ?", (username,))
    user_data = cursor.fetchone()

    if user_data is None:
        anaSayfaResultStr.set("Kullanıcı bulunamadı")
    else:
        user_id, stored_password = user_data
        hashed_password = hashlib.md5(password.encode("UTF-8")).hexdigest()

        if stored_password == hashed_password:
            anaSayfaResultStr.set("Kullanıcı girişi başarılı")
            # Eklenen kullanıcının userID'sini al
            root.destroy()
            uygulama = KayitUygulamasi(tk.Tk())  # Yeni bir root penceresi oluşturarak KayitUygulamasi sınıfını başlat
            uygulama.root.mainloop()
        else:
            anaSayfaResultStr.set("Şifre yanlış girildi")

# Şifre sıfırlama fonksiyonu
def sifremi_unuttum():
    anaSayfaResultStr.set("")
    sifremiUnuttumResultStr.set("")

    sifremiUnuttumFrame = Frame(root, bg='#e6e6ff')
    sifremiUnuttumFrame.place(relx=0.5, rely=0.5, anchor="center")
    sifreyenile_label = Label(sifremiUnuttumFrame, text="Şifreni Yenile", font=("Times New Roman", 14, 'bold'), bg='#e6e6ff',
                              fg='#566573')
    sifreyenile_label.grid(row=0, column=3, padx=5, pady=5)
    usernameLabel = Label(sifremiUnuttumFrame, text="Kullanıcı Adı:", bg='#e6e6ff')
    usernameEntry = Entry(sifremiUnuttumFrame, width=30)
    usernameLabel.grid(row=1, column=2, padx=5, pady=5)
    usernameEntry.grid(row=1, column=3, padx=5, pady=5)

    security_question = StringVar()
    security_question.set("İlk evcil hayvanınızın adı")
    securityLabel = Label(sifremiUnuttumFrame, text="Güvenlik Sorusu:", bg='#e6e6ff')
    securityLabel.grid(row=2, column=2, padx=5, pady=5)

    securityDropdown = OptionMenu(sifremiUnuttumFrame, security_question, "İlk evcil hayvanınızın adı",
                                 "İlkokuldaki öğretmeninizin adı", "En sevdiğiniz renk")
    securityDropdown.grid(row=2, column=3, padx=5, pady=5)

    securityAnswerLabel = Label(sifremiUnuttumFrame, text="Güvenlik Sorusu Cevabı:", bg='#e6e6ff')
    securityAnswerLabel.grid(row=4, column=2, padx=5, pady=5)

    securityAnswerEntry = Entry(sifremiUnuttumFrame, width=30)
    securityAnswerEntry.grid(row=4, column=3, padx=5, pady=5)

    newPasswordLabel = Label(sifremiUnuttumFrame, text="Yeni Şifre:", bg='#e6e6ff')
    newPasswordLabel.grid(row=5, column=2, padx=5, pady=5)
    newPasswordEntry = Entry(sifremiUnuttumFrame, width=30, show="*")
    newPasswordEntry.grid(row=5, column=3, padx=5, pady=5)

    newPasswordReenterLabel = Label(sifremiUnuttumFrame, text="Şifre Tekrar:", bg='#e6e6ff')
    newPasswordReenterLabel.grid(row=6, column=2, padx=5, pady=5)
    newPasswordReenterEntry = Entry(sifremiUnuttumFrame, width=30, show="*")
    newPasswordReenterEntry.grid(row=6, column=3, padx=5, pady=5)
    bos_label = Label(sifremiUnuttumFrame, text="", font=("Helvetica", 10), bg='#e6e6ff')
    bos_label.grid(row=7, column=5, padx=5, pady=5)
    bos_label = Label(sifremiUnuttumFrame, text="", font=("Helvetica", 10), bg='#e6e6ff')
    bos_label.grid(row=7, column=6, padx=5, pady=5)
    bos_label = Label(sifremiUnuttumFrame, text="", font=("Helvetica", 10), bg='#e6e6ff')
    bos_label.grid(row=7, column=7, padx=5, pady=5)
    bos_label = Label(sifremiUnuttumFrame, text="", font=("Helvetica", 10), bg='#e6e6ff')
    bos_label.grid(row=7, column=8, padx=5, pady=5)
    enter = Button(sifremiUnuttumFrame, text="Şifreyi Yenile", bg="green", fg="white",
                   command=lambda: update_password(usernameEntry.get(), security_question.get(),
                                                   securityAnswerEntry.get(), newPasswordEntry.get(),
                                                   newPasswordReenterEntry.get()))
    enter.grid(row=8, columnspan=4, padx=5, pady=5)

    resultLabel = Label(sifremiUnuttumFrame, textvariable=sifremiUnuttumResultStr, bg='#e6e6ff', fg="black", font=('Calibri', 11, 'bold'))
    resultLabel.grid(row=7, columnspan=4, padx=5, pady=5)

    back = Button(sifremiUnuttumFrame, text="Geri Dön", bg="red", fg="white",
                  command=lambda: sifremiUnuttumResultStr.set("") or sifremiUnuttumFrame.place_forget())
    back.grid(row=9, columnspan=4, padx=5, pady=5)


# Şifreyi güncelleme fonksiyonu
def update_password(username, security_question, security_answer, new_password, new_password_reenter):
    anaSayfaResultStr.set("")
    sifremiUnuttumResultStr.set("")

    if not username or not security_question or not security_answer or not new_password or not new_password_reenter:
        sifremiUnuttumResultStr.set("Lütfen tüm bilgileri giriniz")
        return

    cursor.execute("SELECT username, security_question, security_answer FROM USERS WHERE username = ?", (username,))
    user_data = cursor.fetchone()

    if user_data is None:
        sifremiUnuttumResultStr.set("Kullanıcı bulunamadı")
        return

    stored_security_question = user_data[1]
    stored_security_answer = user_data[2]

    #güncellenen kısım
    if not security_question or not security_answer:
        return None
    else:
        encrypted_question = hashlib.md5(security_question.encode("UTF-8")).hexdigest()
        encrypted_answer = hashlib.md5(security_answer.encode("UTF-8")).hexdigest()

    if stored_security_question != encrypted_question:
        sifremiUnuttumResultStr.set("Güvenlik sorusu uyuşmuyor")
        return

    if stored_security_answer != encrypted_answer:
        sifremiUnuttumResultStr.set("Güvenlik sorusu cevabı yanlış")
        return

    hashed_password = hashlib.md5(new_password.encode("UTF-8")).hexdigest()
    cursor.execute("UPDATE USERS SET password = ? WHERE username = ?", (hashed_password, username))
    if new_password == new_password_reenter:
        sifremiUnuttumResultStr.set("Şifre başarıyla değiştirilmiştir")
    if new_password != new_password_reenter:
        sifremiUnuttumResultStr.set("Şifreler aynı değil")
    conn.commit()

# AnaSayfa penceresini oluştur
anaSayfa = Frame(root,bg='#e6e6ff')
anaSayfa.place(relx=0.5, rely=0.5, anchor="center")

hosgeldiniz_label = Label(anaSayfa, text="Hoşgeldiniz!", font=("Times New Roman", 20, 'bold'), bg='#e6e6ff', fg='black')
hosgeldiniz_label.grid(row=0, column=4, padx=5, pady=5)

usernameLabel = Label(anaSayfa, text="Kullanıcı Adı:", bg='#e6e6ff')
usernameEntry = Entry(anaSayfa, width=30)
usernameLabel.grid(row=3, column=3, padx=5, pady=5)
usernameEntry.grid(row=3, column=4, padx=5, pady=5)

passwordLabel = Label(anaSayfa, text="Şifre:", bg='#e6e6ff')
passwordEntry = Entry(anaSayfa, width=30, show="*")
passwordLabel.grid(row=4, column=3, padx=5, pady=5)
passwordEntry.grid(row=4, column=4, padx=5, pady=5)
enter = Button(anaSayfa, text="Giriş Yap", bg="Green", fg="white", command=lambda: auth(usernameEntry.get(), passwordEntry.get()))
enter.grid(row=6, column=3, padx=5, pady=5)

registerButton = Button(anaSayfa, text="Kayıt Ol", bg="Thistle", fg="black", command=yeniKullaniciEklemeSayfasi)
registerButton.grid(row=6, column=4, padx=5, pady=5)

sifremiUnuttumButton = Button(anaSayfa, text="Şifremi Unuttum", bg="Thistle", fg="black", command=sifremi_unuttum)
sifremiUnuttumButton.grid(row=7, column=4, padx=0, pady=5)

cikisButton = Button(anaSayfa, text="Çıkış Yap", bg="Red3", fg="white", command=cikis_yap)
cikisButton.grid(row=7, column=3, padx=0, pady=5)

baslik_label = Label(anaSayfa, text="Dijital Duygu Günlüğü", font=("Caveat", 14, 'bold', 'italic'), bg='#e6e6ff', fg='#8b7b8b')
baslik_label.grid(row=1, column=4, padx=5, pady=5)
baslik_label = Label(anaSayfa, text="Duygularınızı Paylaşın", font=("Caveat", 11,'italic'), bg='#e6e6ff', fg='#8b7b8b')
baslik_label.grid(row=2, column=4, padx=5, pady=5)

# Pencereyi çalıştır
root.mainloop()