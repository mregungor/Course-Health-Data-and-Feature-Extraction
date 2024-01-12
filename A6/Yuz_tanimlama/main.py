#OpenCv ile yüz tanıma
import cv2
import os
import csv

# Haar Cascade sınıflandırıcısını yükledik
face_cascade = cv2.CascadeClassifier(r"classifier/haarcascade_frontalface_default.xml")

# Video dosyasını okumak için VideoCapture'ı başlattık
cap = cv2.VideoCapture(0)

# Dosyaya yazma için CSV dosyasını açma
csv_file = open('etiketlenen_yuzler.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Sol_Ust_X', 'Sol_Ust_Y', 'Sag_Alt_X', 'Sag_Alt_Y'])

# Etiketlenmiş yüzleri saklamak için dizin oluşturma
output_directory = 'etiketlenen_yuzler'
os.makedirs(output_directory, exist_ok=True)

# İteratör
counter = 0
#max_photos = 30

while True:
    #video akısından bir kare aldık
    ret ,img = cap.read()

    # Görüntüyü gri tona çevir (yüz tespiti için genellikle gri ton kullanılır)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #yüzleri tespit et,scale görüntü botutu kücültmek,minneighbors komşuluk değeri
    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30))

    # Her bir tespit edilen yüzün etrafına dikdörtgen çiz
    #sol üst koşe,sağ alt kose,griye cevirme,piksel
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

        # Yüzü ayrı bir dosya olarak kaydetme
        face_image = img[y:y + h, x:x + w]
        cv2.imwrite(os.path.join(output_directory, f"etiketli_yuz_{counter}.jpg"), face_image)

        # Yüz koordinatlarını CSV dosyasına yazma
        csv_writer.writerow([x, y, x + w, y + h])

        # Sonuçları gösterme
        cv2.imshow('Yuz Etiketleme', img)

        # İteratörü arttır
        counter += 1

    # Her 30 fotoğrafta bir kontrol etme
    #if counter % max_photos == 0:
        #print(f"{max_photos} fotograf kaydedildi. Program sona eriyor.")
        #break

    # Çıkış için 'q' tuşuna basma
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Dosyayı kapatma
csv_file.close()

# Webcam ve pencereyi kapatma
cap.release()
cv2.destroyAllWindows()

