import sqlite3 as sql
import pandas as pd
from sklearn.datasets import load_breast_cancer
import os

################3
from flask import Flask, send_file
import os

app = Flask(__name__)

###########


veri_seti = load_breast_cancer()

vt = sql.connect('Breast-Cancer.db')
im = vt.cursor()

excel_dosya_yolu = 'data-veriler.xlsx'
df = pd.read_excel(excel_dosya_yolu)
tablo_adı = 'BreastCancer_Data'
df.to_sql(tablo_adı, vt, index=False, if_exists='replace')

vt.commit()

im.execute('''CREATE TABLE IF NOT EXISTS BreastCancer_Data_Hastalar(
    isim_Soyisim TEXT,
    Tumor_Huy TEXT,
    Ortalama_Yarıçap REAL,
    Ortalama_Çevresi REAL,
    Ortalama_Alan REAL,
    Ortalama_İçbükeylik REAL,
    Ortalama_İçbükey_Noktalar REAL
)''')

def userData_ekle(isim_Soyisim,Tumor_Huy,Ortalama_Yarıçap, Ortalama_Çevresi, Ortalama_Alan, Ortalama_İçbükeylik, Ortalama_İçbükey_Noktalar):
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    add_command = '''INSERT INTO BreastCancer_Data_Hastalar(isim_Soyisim,Tumor_Huy,Ortalama_Yarıçap,Ortalama_Çevresi,Ortalama_Alan,Ortalama_İçbükeylik,Ortalama_İçbükey_Noktalar) VALUES {}'''
    data = (isim_Soyisim,Tumor_Huy,Ortalama_Yarıçap, Ortalama_Çevresi, Ortalama_Alan, Ortalama_İçbükeylik, Ortalama_İçbükey_Noktalar)
    im.execute(add_command.format(data))

    vt.commit()
    vt.close()

def tumorHuy_ekle(isim_Soyisim,Ortalama_Yarıçap, Ortalama_Çevresi, Ortalama_Alan, Ortalama_İçbükeylik, Ortalama_İçbükey_Noktalar):
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    add_command = '''INSERT INTO BreastCancer_Data_Hastalar(isim_Soyisim,Ortalama_Yarıçap,Ortalama_Çevresi,Ortalama_Alan,Ortalama_İçbükeylik,Ortalama_İçbükey_Noktalar) VALUES {}'''
    data = (isim_Soyisim,Ortalama_Yarıçap, Ortalama_Çevresi, Ortalama_Alan, Ortalama_İçbükeylik, Ortalama_İçbükey_Noktalar)
    im.execute(add_command.format(data))

    vt.commit()
    vt.close()

def tumorhuy_ekle(isim_Soyisim,Tumor_Huy):
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()

    upd_command = (''''UPDATE BreastCancer_Data_Hastalar SET Tumor_Huy = '{}' WHERE isim_Soyisim = '{}' ''')
    im.execute(upd_command.format(Tumor_Huy, isim_Soyisim))


    vt.commit()
    vt.close()

def userData_indir():    #deneme
    vt = sql.connect('Breast-Cancer.db')
    im = vt.cursor()
    hasta_data = "SELECT * FROM BreastCancer_Data_Hastalar"
    df = pd.read_sql_query(hasta_data, vt)
    excel_dosya_adi = 'Hasta-Verisi.xlsx'
    df.to_excel(excel_dosya_adi, index=False, engine='openpyxl')
    vt.close()

    dosya_yolu = os.path.join(os.path.expanduser("~"), "Desktop", excel_dosya_adi)
    return send_file(dosya_yolu, as_attachment=True)

vt.commit()
vt.close()

