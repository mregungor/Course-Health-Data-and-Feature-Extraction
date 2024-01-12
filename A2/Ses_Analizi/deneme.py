import subprocess

import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import tkinter as tk
from tkinter import filedialog, messagebox


class SpectrogramAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Spectrogram Analyzer")

        self.file_label = tk.Label(master, text="Bir WAV dosyası seçin:", font=("Arial", 16))
        self.file_label.pack()

        self.file_entry = tk.Entry(master, font=("Arial", 14))
        self.file_entry.pack()

        self.browse_button = tk.Button(master, text="Ses dosyası seçiniz", command=self.browse_file, bg="blue", fg="white", font=("Arial", 14))
        self.browse_button.pack(pady=10)

        self.analyze_button = tk.Button(master, text="Ses grafiklerini görüntüle", command=self.analyze_spectrogram, bg="blue", fg="white", font=("Arial", 14))
        self.analyze_button.pack(pady=5 )

        self.ses_button = tk.Button(master, text="Ses sağlığı önerileri", command=self.oneri, bg="blue", fg="white", font=("Arial", 14))
        self.ses_button.pack(pady=20)

        self.quit_button = tk.Button(master, text="Geri", command=self.geri, bg="blue", fg="white", font=("Arial", 14))
        self.quit_button.pack()


        master.title("Spectrogram Analyzer")
        master.geometry("400x600")

    def geri(self):
        root.destroy()
        subprocess.run(['python','Recorder.py'])
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Wave files", "*.wav")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def analyze_spectrogram(self):
        file_path = self.file_entry.get()
        if not file_path:
            return

        # Ses dosyasını oku
        data, samplerate = sf.read(file_path)

        # FFT analizi uygula
        X = np.fft.fft(data)

        # FFT sonucunu mutlak değere dönüştür
        X = abs(X)

        # Frekans aralığını sınırlandır
        N = len(X)
        freq = np.arange(N) * samplerate / N

        # Maksimum değeri bul
        max_value = np.max(X)
        max_index = np.argmax(X)

        # Maksimum değeri yazdır
        print(f"Maksimum güç: {max_value}")

        # Spektrogramı çiz
        plt.figure()
        plt.plot(freq, X)
        plt.xlabel("Frekans (Hz)")
        plt.ylabel("Güç")
        plt.ylim(0, 500)
        plt.yticks(np.arange(0, 500, 50))

        # Maksimum değeri grafiğe işaretle
        plt.plot(freq[max_index], max_value, 'ro')

        # x eksenini 0'dan başlat
        plt.xlim(0, freq.max())

        # Spektrogramın dosya adını oluştur
        spectrogram_filename = "spectrogram.png"

        # Spektrogramu kaydet
        plt.savefig(spectrogram_filename)

        # Orijinal ses sinyalinin grafiğini çiz
        plt.figure()
        plt.plot(data, 'r')
        plt.xlabel('Zaman (sn)')
        plt.ylabel('Güç')

        # Orijinal ses sinyalinin dosya adını oluştur
        original_signal_filename = "original_signal.png"

        # Orijinal ses sinyalini kaydet
        plt.savefig(original_signal_filename)

        # Her iki grafiği de göster
        plt.show()

    def oneri(self):
        # Ses dosyasını oku
        file_path = self.file_entry.get()
        if not file_path:
            return


        # Ses sağlığı önerileri
        öneriler = [
            "Ses tellerinizi korumak için sesinizi çok fazla kullanmayın.",
            "Yüksek sesle konuştuğunuzda veya bağırdığınızda, ses tellerinizi korumak için ara verin.",
            "Ses tellerinizi güçlendirmek için ses egzersizleri yapın.",
            "Yeterince dinlenin ve bol su için.",
            "Yüksek sesle konuşmaktan veya bağırmaktan kaçının.",
            "Gürültülü ortamlardan kaçının.",
            "Sigara içmeyin veya tütün ürünleri kullanmayın.",
            "Alkol veya kafein tüketiminizi sınırlayın.",
            "Ses tellerinizi rahatlatmak için sıcak kompres uygulayın.",
        ]

        # Ses sağlığı önerilerini göster
        print("\nSes Sağlığı Önerileri:")
        for öneri in öneriler:
            print("- " + öneri)

        öneri_metni = "\nSes Sağlığı Önerileri:\n\n" + "\n".join(öneriler)
        messagebox.showinfo("Ses Sağlığı Önerileri", öneri_metni)



if __name__ == "__main__":
    root = tk.Tk()
    app = SpectrogramAnalyzerGUI(root)
    root.mainloop()
