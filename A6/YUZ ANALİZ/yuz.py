import cv2
import face_recognition
from deepface import DeepFace
import numpy as np

# Eğitim veri setinin dosya yolunu belirle
egitim_data_yolu = "C:/Users/nurul/PycharmProjects/yuz/Face/egitim_data.npz"
egitim_data = np.load(egitim_data_yolu)# NumPy'nin load fonksiyonuyla eğitim veri setini yükle
# Eğitim veri setinden etiketler ve yüzler listelerini çek
etiketler = list(egitim_data["etiketler"])
yuzler = list(egitim_data["yuzler"])

# Webcam başlat
video_capture = cv2.VideoCapture(0)#CHATGPT

while True:# Sonsuz bir döngü başlat
    ret, frame = video_capture.read() # Video akışından bir kare al"CHATGPT"
    # Alınan karedeki yüzleri tespit et
    tespit_edilen_yuzler = face_recognition.face_locations(frame)
    # Tespit edilen yüzlerin kodlamalarını al
    tespit_edilen_yuz_encodings = face_recognition.face_encodings(frame, tespit_edilen_yuzler)
    # Tespit edilen her bir yüz ve onun kodlaması üzerinde döngü başlat
    for (top, right, bottom, left), tespit_edilen_yuz_encoding in zip(tespit_edilen_yuzler, tespit_edilen_yuz_encodings):
        isim = "Bilinmiyor"# Başlangıçta ismi "Bilinmiyor" olarak ayarla
        # Eğitim veri setindeki yüzlerle karşılaştırma yap
        uyumlar = face_recognition.compare_faces(yuzler, tespit_edilen_yuz_encoding)
        if True in uyumlar:# Eğer en az bir uyum varsa
            indeks = uyumlar.index(True)# İlk uyumlu yüzün indeksini al
            isim = etiketler[indeks] # İsim, eğitim veri setindeki etiketler listesinden alınır

        # Duygu analizi sonuçlarını al
        sonuclar = DeepFace.analyze(frame, actions=['emotion'])
        # En belirgin duyguyu bul
        en_belirgin_duygu = max(sonuclar[0]['emotion'].items(), key=lambda x: x[1])
        # Yüzün çevresine dikdörtgen çiz ve isimle birlikte en belirgin duyguyu ekle
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
        cv2.putText(frame, f"{isim} - {en_belirgin_duygu[0]}: {en_belirgin_duygu[1]}",(left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    # Web kameradan alınan kareyi ekranda göster
    cv2.imshow('Webcam - Yüz Tanıma ve Duygu Analizi', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):#"CHATGPT"
        break

# Video akışını serbest bırak
video_capture.release()

# Tüm pencereleri kapat
cv2.destroyAllWindows()

