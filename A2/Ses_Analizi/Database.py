import sqlite3
import subprocess
import tkinter as tk
from tkinter import ttk

class DatabaseViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite Database Viewer")

        # Veritabanına bağlan
        self.connection = sqlite3.connect("ses_kaydi.db")
        self.cursor = self.connection.cursor()

        # Arayüz öğelerini oluştur
        self.create_widgets()

    def create_widgets(self):
        # Listbox widget'ını oluştur
        self.listbox = tk.Listbox(self.root, width=100, height=10)
        self.listbox.grid(row=0, column=0, padx=10, pady=10)

        # Verileri Listbox'a ekleyen butonu oluştur
        self.show_data_button = tk.Button(self.root, text="Verileri Göster", command=self.show_data)
        self.show_data_button.grid(row=1, column=0, pady=5)

        self.Geri = tk.Button( text="Geri", command=self.geri)
        self.Geri.place(x=0, y=0, width=60, height=20)

    def geri(self):
        root.destroy()
        subprocess.run(["python","Recorder.py"])
    def show_data(self):
        # Veritabanından verileri al
        self.cursor.execute("SELECT * FROM recordings")
        data = self.cursor.fetchall()

        # Listbox'ı temizle
        self.listbox.delete(0, tk.END)

        # Verileri Listbox'a ekle
        for row in data:
            self.listbox.insert(tk.END, row)

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseViewer(root)
    root.mainloop()
