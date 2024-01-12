import sqlite3 as sql #veritabanı ile etkileşim
from datetime import datetime

# Veritabanı bağlantısı oluştur
conn = sql.connect('app.db')
cursor = conn.cursor()

#USERDATA tablosunu oluştur (Eğer yoksa)
cursor.execute('CREATE TABLE IF NOT EXISTS USERDATA ('
               'age INTEGER,'
               'dateofBirth DATE,'
               'gender TEXT,'
               'job TEXT,'
               'entryDate DATE,'
               'maritalStatus TEXT,'
               'emotionEntry TEXT,'
               'notebook TEXT,'
               'hobbies TEXT,'
               'user_id INTEGER PRIMARY KEY,'
               'FOREIGN KEY(user_id) REFERENCES USERS(userID)'
               ')')
conn.commit() # Değişiklikleri kaydet
class UserManager:
    def __init__(self):
        self.conn = sql.connect('app.db') #veritabanına bağlantı oluşturma
        self.cursor = self.conn.cursor() #sorgulama

    def add_user(self, age, birthdate, gender, job, marital_status, entryDate):
        try:
            entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute(
                "INSERT INTO USERDATA(age, dateofBirth, gender, job, maritalStatus, entryDate) VALUES(?,?,?,?,?,?)",
                (age, birthdate, gender, job, marital_status, entryDate))
            self.conn.commit()
            print("Kullanıcı bilgileri başarıyla eklendi.")
            return self.cursor.lastrowid #Son eklenen kullanıcının benzersiz id'ye sahip olmasını sağlar
        except Exception as e:
            print(f"Hata: {e}")
            return None

    def update_hobbies(self, user_id, hobbies):
        try:
            # hobilerinin güncellenmesi, query, işlemi gerçekleştirmek için kullanılacak olan SQL sorgusunu ifade der
            query = "UPDATE USERDATA SET hobbies = ? WHERE user_id = ?"
            # join hobbies, seçilen tüm hobileri dizi olarak tutarak tek bir sütunda virgülle ayırarak yazar
            self.cursor.execute(query, (",".join(hobbies), user_id))
            self.conn.commit()
        except Exception as e:
            print("Hata:", str(e))

    def add_notes(self, user_id, notes):
        try:
            query = "UPDATE USERDATA SET notebook = ? WHERE user_id = ?"
            self.cursor.execute(query, (notes, user_id))
            self.conn.commit()
            print("Notlar başarıyla eklendi.")
        except Exception as e:
            print("Hata:", str(e))

    def add_emotion_and_notebook(self, user_id,notebook):
        try:
            entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO USERDATA (notebook, userID, entryDate) VALUES (?, ?, ?, ?)"
            self.cursor.execute(query, (notebook, user_id, entry_date))
            self.conn.commit()
            print("Not bilgileri başarıyla eklendi.")
            return True
        except Exception as e:
            print(f"Hata: {e}")
            return False

    def __del__(self):
        self.conn.close()
