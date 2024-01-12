import mysql.connector

class HastaKayit:
    def __init__(self, isim, soyisim, dogum_tarihi, cinsiyet, dogum_yeri):
        self.isim = isim
        self.soyisim = soyisim
        self.dogum_tarihi = dogum_tarihi
        self.cinsiyet = cinsiyet
        self.dogum_yeri = dogum_yeri

    def baglan(self):
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nukleotits.1',
            database='Nukleotits'
        )

    def hasta_ekle(self):
        conn = self.baglan()
        cursor = conn.cursor()

        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS hasta_kayit (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    isim VARCHAR(50),
                    soyisim VARCHAR(50),
                    dogum_tarihi DATE,
                    cinsiyet VARCHAR(10),
                    dogum_yeri VARCHAR(100)
                )
            ''')

            sql = '''
                INSERT INTO hasta_kayit (isim, soyisim, dogum_tarihi, cinsiyet, dogum_yeri)
                VALUES (%s, %s, %s, %s, %s)
            '''
            values = (self.isim, self.soyisim, self.dogum_tarihi, self.cinsiyet, self.dogum_yeri)
            cursor.execute(sql, values)

            conn.commit()
            print("Hasta başarıyla eklendi.")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            conn.close()