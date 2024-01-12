import os
import sqlite3
import subprocess
import tkinter as tk
import wave
from array import array
from datetime import datetime
from struct import pack
from sys import byteorder
from tkinter import messagebox

import librosa
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class SesKaydiUygulamasi:
    def __init__(self, master):

        self.animation = None


        self.master = master
        self.master.title("Ses Kaydı Tutucu")


        width = 643
        height = 650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        self.isim_label = tk.Label(self.master, text="İsim:")
        self.isim_label.place(x=120, y=32, height=15, width=30)

        self.isim_entry = tk.Entry(self.master)
        self.isim_entry.place(x=170, y=30, height=20, width=100)

        self.soyisim_label = tk.Label(self.master, text="Soyisim:")
        self.soyisim_label.place(x=110, y=57, height=15, width=50)

        self.soyisim_entry = tk.Entry(self.master)
        self.soyisim_entry.place(x=170, y=55, height=20, width=100)

        self.ses_kaydi_button = tk.Button(self.master, text="Ses Kaydını Başlat", command=self.recognize_gender)
        self.ses_kaydi_button.place(x=330, y=40, height=30, width=100)

        self.database = tk.Button(self.master, text="Veri Tabanı", command=self.database)
        self.database.place(x=170, y=82, width=100,height=30)

        self.Grafik_Button = tk.Button(self.master, text="Grafikler", command=self.graph)
        self.Grafik_Button.place(x=470, y=40, width=100, height=30)

        self.ses_sagligi_button = tk.Button(self.master, text="Ses Sağlığı", command=self.ses_sagligi)
        self.ses_sagligi_button.place(x=330, y=97, width=100,height=30)  # Ses Kaydını Başlat butonuyla aynı x koordinatında

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().grid(columnspan=2)
        self.canvas.get_tk_widget().place(x=0, y=150, width=700, height=500)


        self.result_label = tk.Label(root, text="")
        self.result_label.place(x=320, y=80, height=20, width=70)

        self.probabs_label = tk.Label(root, text="")
        self.probabs_label.place(x=400, y=80, width=250, height=20)

        self.db_file = "ses_kaydi.db"
        self.create_database()

    def create_database(self):
        # Create a SQLite database and a table for recordings
        try:
            self.veritabani_baglantisi = sqlite3.connect(self.db_file)
            self.veritabani_cursor = self.veritabani_baglantisi.cursor()
            self.veritabani_cursor.execute('''
                CREATE TABLE IF NOT EXISTS recordings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    İsim TEXT,
                    Soyisim TEXT,
                    Tarih_Saat TEXT,
                    Cinsiyet TEXT,
                    Oran  TEXT,
                    Dosya_Adi TEXT,
                    Dosya_Yolu TEXT
                )
            ''')
            self.veritabani_baglantisi.commit()
        except Exception as e:
           messagebox.showerror("Database Error", f"Error creating database: {str(e)}")
    def database(self):
        root.destroy()
        subprocess.run(["python", "Database.py"])

    def insert_record(self, İsim, Soyisim, Tarih_Saat, Cinsiyet, Oran, Dosya_Adi, Dosya_Yolu):
        # Insert a new recording into the database
        try:
            self.veritabani_cursor.execute('''
                   INSERT INTO recordings (İsim, Soyisim, Tarih_Saat, Cinsiyet, Oran, Dosya_Adi, Dosya_Yolu)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
               ''', (İsim, Soyisim, Tarih_Saat, Cinsiyet, Oran, Dosya_Adi, Dosya_Yolu))
            self.veritabani_baglantisi.commit()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error inserting record: {str(e)}")

    def graph(self):
        root.destroy()
        subprocess.run(["python", "Graphs.py"])

    def ses_sagligi(self):
        root.destroy()
        subprocess.run(["python", "deneme.py"])

    def recognize_gender(self):

        global veritabani_baglantisi, veritabani_cursor
        THRESHOLD = 500
        CHUNK_SIZE = 1024
        FORMAT = pyaudio.paInt16
        RATE = 16000

        SILENCE = 30

        def plot_waveform(waveform):
            self.ax.clear()
            self.ax.plot(waveform, color='blue')
            self.ax.set_title('Sound Waveform')
            self.ax.set_xlabel('Time')
            self.ax.set_ylabel('Amplitude')
            self.canvas.draw()

        def is_silent(snd_data):
            "Returns 'True' if below the 'silent' threshold"
            return max(snd_data) < THRESHOLD

        def normalize(snd_data):
            "Average the volume out"
            MAXIMUM = 16384
            times = float(MAXIMUM) / max(abs(i) for i in snd_data)

            r = array('h')
            for i in snd_data:
                r.append(int(i * times))
            return r

        def trim(snd_data):
            "Trim the blank spots at the start and end"

            def _trim(snd_data):
                snd_started = False
                r = array('h')

                for i in snd_data:
                    if not snd_started and abs(i) > THRESHOLD:
                        snd_started = True
                        r.append(i)

                    elif snd_started:
                        r.append(i)
                return r

            # Trim to the left
            snd_data = _trim(snd_data)

            # Trim to the right
            snd_data.reverse()
            snd_data = _trim(snd_data)
            snd_data.reverse()
            return snd_data

        def add_silence(snd_data, seconds):
            "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
            r = array('h', [0 for i in range(int(seconds * RATE))])
            r.extend(snd_data)
            r.extend([0 for i in range(int(seconds * RATE))])
            return r



        def record():
            """
            Record a word or words from the microphone and
            return the data as an array of signed shorts.
            Normalizes the audio, trims silence from the
            start and end, and pads with 0.5 seconds of
            blank sound to make sure VLC et al can play
            it without getting chopped off.
            """
            p = pyaudio.PyAudio()
            stream = p.open(format=FORMAT, channels=1, rate=RATE,
                            input=True, output=True,
                            frames_per_buffer=CHUNK_SIZE)

            num_silent = 0
            snd_started = False

            r = array('h')

            while 1:
                # little endian, signed short
                snd_data = array('h', stream.read(CHUNK_SIZE))
                if byteorder == 'big':
                    snd_data.byteswap()
                r.extend(snd_data)


                silent = is_silent(snd_data)

                if silent and snd_started:
                    num_silent += 1
                elif not silent and not snd_started:
                    snd_started = True

                if snd_started and num_silent > SILENCE:
                    break

            sample_width = p.get_sample_size(FORMAT)
            stream.stop_stream()
            stream.close()
            p.terminate()

            r = normalize(r)
            r = trim(r)
            r = add_silence(r, 0.5)
            return sample_width, r

        def record_to_file(path):
            "Records from the microphone and outputs the resulting data to 'path'"
            sample_width, data = record()
            data = pack('<' + ('h' * len(data)), *data)

            wf = wave.open(path, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(sample_width)
            wf.setframerate(RATE)
            wf.writeframes(data)
            wf.close()

        def extract_feature(file_name, **kwargs):
            """
            Extract feature from audio file `file_name`
                Features supported:
                    - MFCC (mfcc)
                    - Chroma (chroma)
                    - MEL Spectrogram Frequency (mel)
                    - Contrast (contrast)
                    - Tonnetz (tonnetz)
                e.g:
                `features = extract_feature(path, mel=True, mfcc=True)`
            """
            mfcc = kwargs.get("mfcc")
            chroma = kwargs.get("chroma")
            mel = kwargs.get("mel")
            contrast = kwargs.get("contrast")
            tonnetz = kwargs.get("tonnetz")
            X, sample_rate = librosa.core.load(file_name)
            if chroma or contrast:
                stft = np.abs(librosa.stft(X))
            result = np.array([])
            if mfcc:
                mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
                result = np.hstack((result, mfccs))
            if chroma:
                chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
                result = np.hstack((result, chroma))
            if mel:
                mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T, axis=0)
                result = np.hstack((result, mel))
            if contrast:
                contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0)
                result = np.hstack((result, contrast))
            if tonnetz:
                tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T, axis=0)
                result = np.hstack((result, tonnetz))
            return result


        if __name__ == "__main__":
            # load the saved model (after training)
            # model = pickle.load(open("result/mlp_classifier.model", "rb"))
            from utils import create_model
            import argparse
            parser = argparse.ArgumentParser(description="""Gender recognition script, this will load the model you trained, 
                                            and perform inference on a sample you provide (either using your voice or a file)""")
            parser.add_argument("-f", "--file", help="The path to the file, preferred to be in WAV format")
            args = parser.parse_args()
            file = args.file
            # construct the model
            model = create_model()
            # load the saved/trained weights
            model.load_weights("results/model.h5")
            if not file or not os.path.isfile(file):
                # if file not provided, or it doesn't exist, use your voice
                print("Please talk")
                # put the file name here
                isim = self.isim_entry.get()
                soyisim = self.soyisim_entry.get()
                tarih_saat = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
                file = f"{isim}_{soyisim}_{tarih_saat}.wav"




                # record the file (start talking)
                record_to_file(file)
            # extract features and reshape it
            features = extract_feature(file, mel=True).reshape(1, -1)
            # predict the gender!

            male_prob = model.predict(features)[0][0]
            female_prob = 1 - male_prob

            gender = "Erkek" if male_prob > female_prob else "Kadın"
            olasilik = f"{male_prob * 100:.2f}%" if gender == "Erkek" else f"{female_prob * 100:.2f}%"
            isim = self.isim_entry.get()
            soyisim = self.soyisim_entry.get()
            tarih_saat = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
            Dosya_Adi = f"{isim}_{soyisim}_{tarih_saat}.wav"
            Dosya_Yolu = os.path.join('C:\\Users\\murat\\PycharmProjects\\SesFinal', Dosya_Adi)

            self.insert_record(isim, soyisim, tarih_saat, gender, olasilik, Dosya_Adi, Dosya_Yolu)
            _, snd_data = record()

            plot_waveform(snd_data)

            self.result_label.config(
            text=f"Sonuç: {gender}")

            self.probabs_label.config(
             text=f"Olasılıklar: Erkek: {male_prob * 100: .2f} % Kadın: {female_prob * 100: .2f} %")




# __main__ kısmı
if __name__ == "__main__":
    root = tk.Tk()
    uygulama = SesKaydiUygulamasi(root)
    root.mainloop()