import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import cv2
from PIL import Image, ImageTk
import webbrowser
import mediapipe as mp
import datetime
import numpy as np

class KameraArayuzu:
    def __init__(self, root):
        self.root = root
        self.root.title("Duygusal Günlük")
        self.foto_sayac = 0
        self.kamera = cv2.VideoCapture(0)

        self.canvas = tk.Canvas(root, bg="#FFEB3B")
        self.canvas.pack()

        self.buton_mutlu = ttk.Button(root, text=" Mutlu ☺️", command=self.buton_mutlu_callback, style='TButton')
        self.buton_mutlu.pack(side=tk.LEFT, padx=10)

        self.buton_uzgun = ttk.Button(root, text="Üzgün 😕", command=self.buton_uzgun_callback, style='TButton')
        self.buton_uzgun.pack(side=tk.LEFT, padx=10)

        self.buton_kizgin = ttk.Button(root, text="Kızgın 😡", command=self.buton_kizgin_callback, style='TButton')
        self.buton_kizgin.pack(side=tk.LEFT, padx=10)

        self.buton_saskin = ttk.Button(root, text="Şaşkın 😯", command=self.buton_saskin_callback, style='TButton')
        self.buton_saskin.pack(side=tk.LEFT, padx=10)

        self.buton_diger = ttk.Button(root, text="Diğer", command=self.buton_diger_callback, style='TButton')
        self.buton_diger.pack(side=tk.LEFT, padx=10)

        self.buton_webcam = ttk.Button(root, text="Webcamim Yok", command=self.webcam_ac, style='TButton')
        self.buton_webcam.pack(side=tk.LEFT, padx=10)

        self.style = ttk.Style()
        self.style.configure('TButton', font=('calibri', 10, 'bold'), foreground='#1565C0', background='#FFC107')  # Buton stilini özelleştirdik

        self.video_goster()

    def video_goster(self):
        ret, frame = self.kamera.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=frame)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.photo = photo
            self.root.after(10, self.video_goster)
        else:
            self.kamera.release()

    def webcam_ac(self):
        ipwebcam_adres = "http://192.168.41.129:8080"
        webbrowser.open(ipwebcam_adres)

    def not_birak(self):
        not_text = simpledialog.askstring("Günlük", f" Bugün neler olduğunu ve neler hissettiğinizi anlatmak ister misiniz?")

        if not not_text:
            return

        tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        not_line = f"{tarih}\n{not_text}\n\n"

        dosya_yolu = "C:\\Users\\kahya\\OneDrive\\Masaüstü\\gunluknotlar"
        dosya_adi = "gunluk.txt"
        with open(f"{dosya_yolu}/{dosya_adi}", "a", encoding="utf-8") as dosya:
            dosya.write(not_line)

    def buton_mutlu_callback(self):
        isim = self.isim_cinsiyet_yas_sor()
        self.acilacak_pencere("Mutlu", f"{isim}, Bugün Çok Güzelsiniz :) Her Daim Gülümsemeye Devam\n")


        self.foto_kaydet("Mutlu")
        self.not_birak()

    def buton_uzgun_callback(self):
        isim = self.isim_cinsiyet_yas_sor()
        self.acilacak_pencere("Üzgün", f"{isim}, Hobi Alanınıza Uygun En Yakın Yerlere Göz Atmak İster Misiniz?", True)
        self.foto_kaydet("Uzgun")
        self.not_birak()

    def buton_kizgin_callback(self):
        isim = self.isim_cinsiyet_yas_sor()
        self.acilacak_pencere("Kızgın", f"{isim}, Rahat bir pozisyonda oturun veya yatar pozisyonda uzanın.\n"
                                        "Burundan derin bir nefes alın. Bu esnada karın bölgesinin şişmesi gerekir.\n"
                                        "Nefesinizi yaklaşık 3-4 saniye boyunca tutun.\n"
                                        "Ağzınızdan yavaşça nefes verin. Bu esnada karın bölgeniz tekrar içeri doğru çekilmeli.\n"
                                        "Nefes verirken yavaş olun ve mümkün olduğunca tüm havayı boşaltın.\n"
                                        "Nefes alma ve verme işlemini 10-15 kez tekrarlayın.\n"
                                        "Her tekrarda nefes alma ve verme süresini artırarak ilerleyebilirsiniz.")
        self.foto_kaydet("Kizgin")
        self.not_birak()

    def buton_saskin_callback(self):
        isim = self.isim_cinsiyet_yas_sor()
        pencere = self.acilacak_pencere("Şaşkın",
                                        f"{isim}, En yakın arkadaşınızı arayıp şaşkınlığınızın nedenini anlatmak ister misiniz?")
        arama_buton = ttk.Button(pencere, text="En Yakın Arkadaşınızı Ara", command=self.en_yakin_arkadasi_ara)
        arama_buton.pack(pady=10)
        self.foto_kaydet("Saskin")
        self.not_birak()

    def buton_diger_callback(self):
        isim = self.isim_cinsiyet_yas_sor()
        duygu = self.kullanici_duygu_girisi()
        self.acilacak_pencere("Diğer", f"{isim}, Bugün {duygu} olarak hissediyordunuz. Nasıl daha iyi hissedersiniz tam kestiremiyoruz.\n")
        self.foto_kaydet("Diger")
        self.not_birak()


    def kullanici_duygu_girisi(self):
        duygu = simpledialog.askstring("Duygu Girişi", "Bugün nasıl hissediyorsunuz?")
        return duygu

    def isim_cinsiyet_yas_sor(self):
        isim = simpledialog.askstring("Bilgi", "Adınız:")
        return isim

    def acilacak_pencere(self, baslik, icerik, harita_butonu=False):
        pencere = tk.Toplevel(self.root)
        pencere.title(baslik)

        etiket = ttk.Label(pencere, text=icerik)
        etiket.pack(padx=10, pady=10)

        if harita_butonu:
            kahve_buton = ttk.Button(pencere, text="Kahvecileri Göster", command=self.kahve_salonlarini_goster)
            kahve_buton.pack(pady=10)

            bilardo_buton = ttk.Button(pencere, text="Bilardo Salonlarını Göster",command=self.bilardo_salonlarini_goster)
            bilardo_buton.pack(pady=10)

            ps_buton = ttk.Button(pencere, text="Playstationcıları Göster", command=self.ps_salonlarini_goster)
            ps_buton.pack(pady=10)

            sinema_buton = ttk.Button(pencere, text="Sinemaları Göster", command=self.sinemalari_goster)
            sinema_buton.pack(pady=10)
        return pencere

    def kahve_salonlarini_goster(self):
        adres = "https://www.google.com/maps/search/?api=1&query=Kahve"
        webbrowser.open(adres)

    def bilardo_salonlarini_goster(self):
        adres = "https://www.google.com/maps/search/?api=1&query=Bilardo+Salonu"
        webbrowser.open(adres)

    def ps_salonlarini_goster(self):
        adres = "https://www.google.com/maps/search/?api=1&query=Playstation+Salonu"
        webbrowser.open(adres)

    def sinemalari_goster(self):
        adres = "https://www.google.com/maps/search/?api=1&query=Sinema"
        webbrowser.open(adres)

    def foto_kaydet(self, duygu):
        ret, frame = self.kamera.read()
        if ret:
            dosya_adi = f"{duygu}_{self.foto_sayac}.png"
            dosya_yolu = "C:\\Users\\kahya\\OneDrive\\Masaüstü\\fotolar"
            dosya_yolu = dosya_yolu.replace("/", "\\")
            cv2.imwrite(f"{dosya_yolu}\\{dosya_adi}", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            print(f"{dosya_adi} adlı dosya {dosya_yolu} dizinine kaydedildi.")
            self.foto_sayac += 1

            parmak_sayisi = self.parmak_sayisini_algila(frame)
            parmak_sayisi = min(5, parmak_sayisi)
            print(
                f"Algılanan Parmak Sayısı: {parmak_sayisi} Yani bugün 5 üzerinden {parmak_sayisi} kadar {duygu}sunuz.")



    def parmak_sayisini_algila(self, frame):
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        parmak_sayisi = 0

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                for point in landmarks.landmark:
                    if point.y < 0.5:
                        parmak_sayisi += 1

        return parmak_sayisi


if __name__ == "__main__":
    root = tk.Tk()
    app = KameraArayuzu(root)
    root.mainloop()


