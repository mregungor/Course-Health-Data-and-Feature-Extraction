import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import webbrowser
from user_database import UserManager
class KayitUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Kişi Kayıt Uygulaması")
        self.root.geometry("600x500")  # Pencere boyutu
        self.root.configure(bg="#FFEBEB")  # Arka plan rengi

        self.ana_cerceve = tk.Frame(root, bg="#FFEBEB")
        self.ana_cerceve.pack(expand=True, fill="both")

        self.etiketler_olustur()
        self.giris_kutulari_olustur()
        self.buton_olustur()

        # UserD_database sınıfıyla veritabanına erişim
        self.user_manager = UserManager()
        self.cursor = self.user_manager.cursor

        # İkinci, üçüncü ve dördüncü sayfaların nesnelerini tanımlama
        self.ikinci_sayfa = None
        self.ucuncu_sayfa = None
        self.dorduncu_sayfa = None

    def etiketler_olustur(self):
        etiketler = ["Yaşınız:", "Doğum Tarihiniz (GG.AA.YYYY):", "Cinsiyetiniz:",
                     "Mesleğiniz:", "Boyunuz (cm):", "Kilonuz (kg):", "Medeni Durumunuz:"]

        for i, etiket_text in enumerate(etiketler):
            etiket = tk.Label(self.ana_cerceve, text=etiket_text, bg="#FFEBEB", font=("Arial", 12, "italic"))
            etiket.grid(row=i, column=0, padx=10, pady=10, sticky="w")

    def giris_kutulari_olustur(self):
        self.giris_yas = tk.Entry(self.ana_cerceve, font=("Arial", 12, "italic"))
        self.giris_yas.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.giris_dogum_tarihi = tk.Entry(self.ana_cerceve, font=("Arial", 12, "italic"))
        self.giris_dogum_tarihi.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.combo_cinsiyet = ttk.Combobox(self.ana_cerceve, values=["Erkek", "Kadın"], font=("Arial", 12, "italic"))
        self.combo_cinsiyet.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.giris_meslek = tk.Entry(self.ana_cerceve, font=("Arial", 12, "italic"))
        self.giris_meslek.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.giris_boy = tk.Entry(self.ana_cerceve, font=("Arial", 12, "italic"))
        self.giris_boy.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.giris_kilo = tk.Entry(self.ana_cerceve, font=("Arial", 12, "italic"))
        self.giris_kilo.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        self.radio_durum = tk.StringVar()
        self.radio_durum.set("Bekar")
        self.radio_bekar = tk.Radiobutton(self.ana_cerceve, text="Bekar", variable=self.radio_durum, value="Bekar", bg="#FFEBEB", font=("Arial", 12, "italic"))
        self.radio_bekar.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        self.radio_evli = tk.Radiobutton(self.ana_cerceve, text="Evli", variable=self.radio_durum, value="Evli", bg="#FFEBEB", font=("Arial", 12, "italic"))
        self.radio_evli.grid(row=6, column=1, padx=10, pady=10, sticky="e")

    def buton_olustur(self):
        self.devam_buton = tk.Button(self.ana_cerceve, text="Devam", command=self.devam_buton_tiklandi, bg="#FF69B4", font=("Arial", 14, "italic"))
        self.devam_buton.grid(row=7, column=0, columnspan=2, pady=10)

    def devam_buton_tiklandi(self):
        # Kaydetme işlemi
        kaydet_sonuc, user_id = self.kaydet()

        # Eğer kaydetme işlemi başarılıysa, ikinci forma geç
        if kaydet_sonuc:
            if self.ikinci_sayfa is None:
                self.ikinci_sayfa = self.ikinci_form(user_id, self.user_manager)

    def kaydet(self):
        yas = self.giris_yas.get()
        dogum_tarihi = self.giris_dogum_tarihi.get()
        cinsiyet = self.combo_cinsiyet.get()
        meslek = self.giris_meslek.get()
        boy = self.giris_boy.get()
        kilo = self.giris_kilo.get()
        durum = self.radio_durum.get()

        # Boş kutu kontrolü
        if not all([yas, dogum_tarihi, cinsiyet, meslek, boy, kilo]):
            messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun.")
            return False, None

        try:
            yas = int(yas)
            dogum_tarihi = datetime.strptime(dogum_tarihi, "%d.%m.%Y").date()
            boy = float(boy)
            kilo = float(kilo)

            entryDate = datetime.now().date()  # Şuanki tarihi alma
            # Verileri UserManager sınıfını kullanarak veritabanına kaydetme
            user_manager = UserManager()
            user_id = user_manager.add_user(yas, dogum_tarihi, cinsiyet, meslek, durum, entryDate)

            if user_id is not None:
                return True, user_id
            else:
                messagebox.showerror("Hata", "Kullanıcı eklenirken bir hata oluştu.")
                return False, None

        except ValueError:
            messagebox.showerror("Hata", "Geçersiz giriş!")
            return False, None

    def ikinci_form(self, user_id, user_manager):
        if self.root and self.root.winfo_exists():
            ikinci_pencere = tk.Toplevel(self.root)
            ikinci_pencere.title("Hobilerin Neler?")
            ikinci_pencere.geometry("600x500")  # Pencere boyutu
            ikinci_pencere.configure(bg="#ADD8E6")  # Arka plan rengi

            etiket = tk.Label(ikinci_pencere, text=f"Merhaba, {user_id}! Hobilerin Neler?", bg="#ADD8E6",
                              font=("Arial", 12, "italic"))
            etiket.pack(pady=20)

            # Checkboxları içerecek olan bir frame oluştur
            checkbox_frame = tk.Frame(ikinci_pencere, bg="#ADD8E6")
            checkbox_frame.pack(pady=10)

            # Checkboxları tanımla
            self.var_gitar = tk.IntVar()
            self.checkbox_gitar = tk.Checkbutton(checkbox_frame, text="Gitar Çalmak", variable=self.var_gitar,
                                                 bg="#ADD8E6", font=("Arial", 12, "italic"))
            self.checkbox_gitar.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            self.var_sarki = tk.IntVar()
            self.checkbox_sarki = tk.Checkbutton(checkbox_frame, text="Şarkı Söylemek", variable=self.var_sarki,
                                                 bg="#ADD8E6", font=("Arial", 12, "italic"))
            self.checkbox_sarki.grid(row=1, column=0, padx=10, pady=5, sticky="w")

            self.var_kitap = tk.IntVar()
            self.checkbox_kitap = tk.Checkbutton(checkbox_frame, text="Kitap Okumak", variable=self.var_kitap,
                                                 bg="#ADD8E6", font=("Arial", 12, "italic"))
            self.checkbox_kitap.grid(row=2, column=0, padx=10, pady=5, sticky="w")

            self.var_ders = tk.IntVar()
            self.checkbox_ders = tk.Checkbutton(checkbox_frame, text="Ders Çalışmak", variable=self.var_ders,
                                                bg="#ADD8E6", font=("Arial", 12, "italic"))
            self.checkbox_ders.grid(row=3, column=0, padx=10, pady=5, sticky="w")

            # Devam ve Temizle butonları
            devam_buton = tk.Button(ikinci_pencere, text="Devam", command=lambda : self.ucuncu_forma_gec(user_id), bg="#87CEFA",
                                    font=("Arial", 14, "italic"))
            devam_buton.pack(pady=10)

            temizle_buton = tk.Button(ikinci_pencere, text="Temizle", command=self.temizle, bg="#FF6347",
                                      font=("Arial", 14, "italic"))
            temizle_buton.pack(pady=10)

            return ikinci_pencere

    def temizle(self):
        # Checkboxları temizle
        self.checkbox_gitar.deselect()
        self.checkbox_sarki.deselect()
        self.checkbox_kitap.deselect()
        self.checkbox_ders.deselect()

    def get_secilen_hobiler(self):
    #Seçilen hobiyi tut
        secilen_hobiler = []
        if self.var_gitar.get():
            secilen_hobiler.append("Gitar Çalmak")
        if self.var_sarki.get():
            secilen_hobiler.append("Şarkı Söylemek")
        if self.var_kitap.get():
            secilen_hobiler.append("Kitap Okumak")
        if self.var_ders.get():
            secilen_hobiler.append("Ders Çalışmak")

        return secilen_hobiler

    def get_notlar(self):
        #"1.0" ile belirtilen başlangıç konumundan tüm metin içeriğini al
        return self.not_alani.get("1.0", tk.END)
    def ucuncu_forma_gec(self, user_id):
        # Hobileri al
        hobiler = self.get_secilen_hobiler()

        # Veritabanına kaydet
        self.user_manager.update_hobbies(user_id, hobiler)
        # Üçüncü forma geç
        if self.ucuncu_sayfa is None:
            self.ucuncu_sayfa = self.ucuncu_form(user_id)
            self.ikinci_sayfa.destroy()  # İkinci formu kapat

    def ucuncu_form(self, user_id):
        ucuncu_pencere = tk.Toplevel(self.root)
        ucuncu_pencere.title("Kendimi Nasıl Hissediyorum?")
        ucuncu_pencere.geometry("600x500")  # Pencere boyutu
        ucuncu_pencere.configure(bg="#FFEBEB")  # Arka plan rengi

        etiket = tk.Label(ucuncu_pencere, text="Bugün kendimi nasıl hissediyorum?", bg="#FFEBEB", font=("Arial", 12, "italic"))
        etiket.pack(pady=20)

        self.not_alani = tk.Text(ucuncu_pencere, height=5, width=40, font=("Arial", 12))
        self.not_alani.pack(pady=10)

        # Devam butonu
        devam_buton = tk.Button(ucuncu_pencere, text="Devam", command=lambda: self.dorduncu_forma_gec(self.not_alani, user_id), bg="#87CEFA", font=("Arial", 14, "italic"))
        devam_buton.pack(pady=10)

        return ucuncu_pencere

    def dorduncu_forma_gec(self, not_alani, user_id):
        # Dördüncü forma geç
        notlar = self.get_notlar()
        self.user_manager.add_notes(user_id, notlar) #Fonksiyon çağırma

        if self.dorduncu_sayfa is None:
            self.dorduncu_sayfa = self.dorduncu_form(not_alani)
            self.ucuncu_form(user_id).destroy()  # Üçüncü formu kapat

    def dorduncu_form(self, not_alani):
        dorduncu_pencere = tk.Toplevel(self.root)
        dorduncu_pencere.title("Bugün Ne Yapmak İstersin?")
        dorduncu_pencere.geometry("600x500")  # Pencere boyutu
        dorduncu_pencere.configure(bg="#ADD8E6")  # Arka plan rengi

        etiket = tk.Label(dorduncu_pencere, text="Bugün ne yapmak istersin?", bg="#FFEBEB", font=("Arial", 12, "italic"))
        etiket.pack(pady=20)

        secenekler = ["Film izlemek", "Konsere gitmek", "Arkadaşlarla buluşmak", "Evde dinlenmek"]
        secenek_vari = tk.StringVar()
        secenek_vari.set(secenekler[0])  # Default olarak ilk seçeneği seçili yap

        secenek_menu = ttk.Combobox(dorduncu_pencere, textvariable=secenek_vari, values=secenekler,
                                    font=("Arial", 12, "italic"))
        secenek_menu.pack(pady=10)

        secenek_kaydet_buton = tk.Button(dorduncu_pencere, text="Seçeneği Kaydet",
                                         command=lambda: self.secilen_sey_yap(secenek_vari.get()), bg="#FFEBEB",
                                         font=("Arial", 14, "italic"))
        secenek_kaydet_buton.pack(pady=10)
        return dorduncu_pencere

    def secilen_sey_yap(self, secenek):
        if secenek == "Film izlemek":
            messagebox.showinfo("Öneri", "Güzel bir seçim! Netflix'e yönlendiriliyorsunuz.")
            webbrowser.open("https://www.netflix.com/")  # Netflix'i aç
        elif secenek == "Konsere gitmek":
            messagebox.showinfo("Öneri", "Harika! Konser etkinlikleri için bilet satış sitelerine göz atabilirsiniz.")
            webbrowser.open("https://www.bubilet.com.tr/sehir-sec?redirectURL=")  # Bubilet'e yönlendiriliyorsunuz.
        elif secenek == "Arkadaşlarla buluşmak":
            messagebox.showinfo("Öneri", "Arkadaşlarını aramaya ne dersin?")
        elif secenek == "Evde dinlenmek":
            messagebox.showinfo("Öneri", "Sana dinlenmeler yakışır.")

if __name__== "__main__":
    root = tk.Tk()
    uygulama = KayitUygulamasi(root)
    root.mainloop()

