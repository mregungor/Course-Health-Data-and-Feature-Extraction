import subprocess

import librosa
import librosa.display
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

import numpy as np


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if file_path:
        plot_features(file_path)

def reset_plot():
    root.destroy()
    subprocess.run(["python","Recorder.py"])

def plot_features(audio_file):
    y, sr = librosa.load(audio_file)

    # MFCC
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    plt.figure(figsize=(12, 6))
    plt.subplot(3, 2, 1)
    librosa.display.specshow(mfccs, x_axis='time')
    plt.title('MFCC')
    plt.colorbar()

    # Mel Spectrogram
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr)
    plt.subplot(3, 2, 2)
    librosa.display.specshow(librosa.power_to_db(mel_spec, ref=np.max), y_axis='mel', x_axis='time')
    plt.title('Mel Spectrogram')
    plt.colorbar(format='%+2.0f dB')

    # Chromagram
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    plt.subplot(3, 2, 3)
    librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
    plt.title('Chromagram')
    plt.colorbar()

    # Spectral Contrast
    contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    plt.subplot(3, 2, 4)
    librosa.display.specshow(contrast, x_axis='time')
    plt.title('Spectral Contrast')
    plt.colorbar()

    # Tonnetz
    tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
    plt.subplot(3, 2, 5)
    librosa.display.specshow(tonnetz, y_axis='tonnetz', x_axis='time')
    plt.title('Tonnetz')
    plt.colorbar()

    plt.tight_layout()
    plt.show()

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("Ses Dosyası Analizi")

# Butonu oluştur ve browse_file fonksiyonunu bağla
browse_button = tk.Button(root, text="Ses Dosyası Seç", command=browse_file)
browse_button.pack(pady=20)

reset_button = tk.Button(root, text="Geri", command=reset_plot)
reset_button.pack(pady=20)

# Pencereyi çalıştır
root.mainloop()
