#Mert Gürhan 2318121204
import tkinter as tk
from Bio.Seq import Seq
from random import choice, random
error_rate = 0.014  # %1 yanlış eşleşme
error_pairs = [("A", "T"), ("T", "A"), ("C", "G"), ("G", "C")]
def introduce_errors(sequence):
    mutated_sequence = []
    for base in sequence:
        if base in ("A", "T", "C", "G") or base == "-":
            if random() < error_rate:
                base = choice([pair[1] for pair in error_pairs])
        mutated_sequence.append(base)
    return Seq("".join(mutated_sequence))
def girisleri_ve_sonucu_temizle():
    ilk_dizi_var.set("")
    ikinci_dizi_var.set("")
    sonuc_metin.delete(1.0, tk.END)
def find_mismatches(first_seq, second_seq):
    mismatches = []
    for i, (base1, base2) in enumerate(zip(first_seq, second_seq)):
        if (base1, base2) not in [("A", "T"), ("T", "A"), ("C", "G"), ("G", "C")]:
            mismatches.append((i + 1, base1, base2))  # Konum ve yanlış eşleşmeleri ekledil
    return mismatches
pencere = tk.Tk()
pencere.title("DNA Uyuşmazlık Tespit Programı")
ilk_dizi_var = tk.StringVar()
ikinci_dizi_var = tk.StringVar()
etiket_ilk_dizi = tk.Label(pencere, text="İlk DNA Dizisi:")
etiket_ilk_dizi.pack(pady=5)
metin_kutusu_ilk_dizi = tk.Entry(pencere, textvariable=ilk_dizi_var)
metin_kutusu_ilk_dizi.pack(pady=5)
etiket_ikinci_dizi = tk.Label(pencere, text="İkinci DNA Dizisi:")
etiket_ikinci_dizi.pack(pady=5)
metin_kutusu_ikinci_dizi = tk.Entry(pencere, textvariable=ikinci_dizi_var)
metin_kutusu_ikinci_dizi.pack(pady=5)
def uyuşmazliklari_tespit_et():
    sonuc_metin.delete(1.0, tk.END)
    ilk_dizi = Seq(ilk_dizi_var.get())
    ikinci_dizi = Seq(ikinci_dizi_var.get())
    ilk_dizi = introduce_errors(ilk_dizi)
    ikinci_dizi = introduce_errors(ikinci_dizi)
    uyuşmazliklar = find_mismatches(ilk_dizi, ikinci_dizi)
    for konum, baz1, baz2 in uyuşmazliklar:
        sonuc_metin.insert(tk.END, f"Uyuşmazlık: {baz1} - {baz2}, Konum: {konum}\n")
    ilk_dizi_uzunlugu = len(ilk_dizi)
    ikinci_dizi_uzunlugu = len(ikinci_dizi)
    uyuşmaz_cift_sayisi = len(uyuşmazliklar)
    bilgi_metni = (
        f"\nİlk DNA dizisi harf sayısı: {ilk_dizi_uzunlugu}\n"
        f"Ikinci DNA dizisi harf sayısı: {ikinci_dizi_uzunlugu}\n"
        f"Uyuşmaz DNA çifti sayısı: {uyuşmaz_cift_sayisi}\n"
    )
    sonuc_metin.insert(tk.END, bilgi_metni)
dugme_tespit = tk.Button(pencere, text="Uyuşmazlıkları Tespit Et", command=uyuşmazliklari_tespit_et)
dugme_tespit.pack(pady=10)
dugme_temizle = tk.Button(pencere, text="Temizle", command=girisleri_ve_sonucu_temizle)
dugme_temizle.pack(pady=10)
sonuc_metin = tk.Text(pencere, height=15, width=50)
sonuc_metin.pack(pady=10)
pencere.mainloop()
#Mert Gürhan 2318121204
