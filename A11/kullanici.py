import json
import re
import hashlib
import secrets

def kaydet(kullanicilar):
    with open("kullanicilar.json", "w") as dosya:
        json.dump(kullanicilar, dosya)

def yukle():
    try:
        with open("kullanicilar.json", "r") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {}

kullanicilar = yukle()

def kayit_ol(kullanicilar, kullanici_ad, soyad, email, sifre):
    if email not in kullanicilar:
        while True:
            sifre_tekrar = input("Şifreyi Tekrar Girin: ")
            if sifre == sifre_tekrar:
                break
            else:
                print("Girdiğiniz şifreler uyuşmuyor. Tekrar deneyin.")

        tuz = secrets.token_hex(16)

        sifre_hash = hashlib.sha256((sifre + tuz).encode()).hexdigest()

        kullanicilar[email] = {'kullanici_ad': kullanici_ad, 'soyad': soyad, 'sifre_hash': sifre_hash, 'tuz': tuz}
        kaydet(kullanicilar)
        print("Kayıt başarıyla tamamlandı.")
    else:
        print("Bu email adresi zaten kayıtlı.")

def giris_yap(kullanicilar, email, sifre):
    if email in kullanicilar:
        sifre_hash = kullanicilar[email]['sifre_hash']
        tuz = kullanicilar[email]['tuz']

        girilen_sifre_hash = hashlib.sha256((sifre + tuz).encode()).hexdigest()

        if girilen_sifre_hash == sifre_hash:
            print(f"{kullanicilar[email]['kullanici_ad']} {kullanicilar[email]['soyad']} giriş yaptı.")
        else:
            print("Email veya şifre hatalı. Giriş başarısız.")
    else:
        print("Email veya şifre hatalı. Giriş başarısız.")

while True:
    print("1. Kayıt Ol")
    print("2. Giriş Yap")
    print("3. Çıkış")

    secim = input("Lütfen bir seçenek girin (1/2/3): ")

    if secim == '1':
        kullanici_ad = input("Kullanıcı Adı: ")
        soyad = input("Soyad: ")

        while True:
            email = input("Email: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                break
            else:
                print("Geçersiz email formatı. Lütfen tekrar deneyin.")

        while True:
            sifre = input("Şifre (en az 6 karakter): ")
            if len(sifre) >= 6:
                break
            else:
                print("Şifre en az 6 karakter olmalıdır. Lütfen tekrar deneyin.")

        kayit_ol(kullanicilar, kullanici_ad, soyad, email, sifre)

    elif secim == '2':
        email = input("Email: ")
        sifre = input("Şifre: ")

        giris_yap(kullanicilar, email, sifre)

    elif secim == '3':
        print("Çıkış yapılıyor. İyi günler!")
        break

    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")
