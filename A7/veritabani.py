import sqlite3 as sql
from PyQt5.QtWidgets import QMessageBox

def tablo_olustur():
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    im.execute('''CREATE TABLE IF NOT EXISTS Kullanici_Data(
        id INTEGER PRIMARY KEY,
        ad TEXT,
        soyad TEXT,
        tc_kimlik TEXT,
        sifre TEXT            
    )''')
    vt.commit()
    vt.close()

def kayit_ekle(ad,soyad,tc_kimlik,sifre):
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    add_command = '''INSERT INTO Kullanici_Data(ad,soyad,tc_kimlik,sifre) VALUES {}'''
    data = (ad, soyad, tc_kimlik, sifre)

    im.execute(add_command.format(data))
    QMessageBox.information(None, 'Kayıt', 'KAYIT BAŞARILI')

    vt.commit()
    vt.close()

def yazdir_kullanici():      #biseyler deniyom
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    im.execute('''SELECT * FROM Kullanici_Data''')
    yazdirma = im.fetchall()

    for user in yazdirma:
        print(user)

    vt.close()

def kullanici_ara(tc_kimlik):
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    search_command = '''SELECT * FROM Kullanici_Data WHERE tc_kimlik = '{}' '''
    im.execute(search_command.format(tc_kimlik))

    user = im.fetchone()

    vt.close()
    return user

def sifre_degistir(tc_kimlik,NewPW):
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    upd_command = ('''UPDATE Kullanici_Data SET sifre = '{}' WHERE tc_kimlik = '{}' ''')
    im.execute(upd_command.format(NewPW, tc_kimlik))

    print("ŞİFRE DEĞİŞTİRME BAŞARILI")

    vt.commit()
    vt.close()

def hesap_sil(tc_kimlik):
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    dlt_command = '''DELETE FROM Kullanici_Data WHERE tc_kimlik = '{}' '''
    im.execute(dlt_command.format(tc_kimlik))
    print("HESAP SİLME BAŞARILI")

    vt.commit()
    vt.close()

def uye_sayisi():   #aaaaaaaaaaaaaaaaa
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    count_command = '''SELECT MAX(id) FROM Kullanici_Data'''
    im.execute(count_command)
    uye = im.fetchone()[0]

    vt.commit()
    vt.close()

    return uye
