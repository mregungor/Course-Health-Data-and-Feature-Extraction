import os
import face_recognition
import numpy as np
#Ana klasörün yolunu belirt
ana_klasor_yolu = r'C:\Users\nurul\PycharmProjects\yuz\Face'
etiketler = []#isimleri saklamak için dizi
yuzler = []## Yüz verilerinin tutmak icin dizi

# Ana klasördeki her bir alt klasör için döngü başlatılır.
for alt_klasor in os.listdir(ana_klasor_yolu):
    # Alt klasörün tam yolunu oluşturmak için kullanılır.
    alt_klasor_yolu = os.path.join(ana_klasor_yolu, alt_klasor)
    # alt_klasor_yolu bir dizin ise
    if os.path.isdir(alt_klasor_yolu):# Eğer alt klasör yolu bir dizin ise, içindeki resim dosyalarını işle.
        for resim_adı in os.listdir(alt_klasor_yolu):# Alt klasördeki her bir resim dosyası için döngü başlatılır.
            resim_yolu = os.path.join(alt_klasor_yolu, resim_adı)# Resmin tam yolunu oluşturmak için kullanılır.
            etiket = alt_klasor# Etiket, resmin bulunduğu alt klasör adı olarak atanır.

            yuz = face_recognition.load_image_file(resim_yolu)# Resmin dosya yolundan yüzü yükleyin
            # resimde yüz var mı kontrol et
            yuz_konumlari = face_recognition.face_locations(yuz)
            if len(yuz_konumlari) > 0:# Eğer yüz tespit edilmişse
                # Yüzün özelliklerini kodlama olarak al
                yuz_encodings = face_recognition.face_encodings(yuz)[0]
                # Etiket ve yüz kodlamasını ilgili listelere ekle
                etiketler.append(etiket)
                yuzler.append(yuz_encodings)
            #ChatGPT ile yazdırılan yerin sonu
# Eğitim veri setini  sakla
egitim_data = {"etiketler": etiketler, "yuzler": yuzler}

# Eğitim veri setini kaydedilecek dosya yolunu belirle
egitim_data_yolu = "C:/Users/nurul/PycharmProjects/yuz/Face/egitim_data.npz"

# NumPy'nin savez fonksiyonuyla eğitim veri setini kaydet
np.savez(egitim_data_yolu, **egitim_data)

# Kullanıcıya başarıyla kaydedildiğine dair bir bildiri göster
print("Eğitim veri seti başarıyla kaydedildi.")

