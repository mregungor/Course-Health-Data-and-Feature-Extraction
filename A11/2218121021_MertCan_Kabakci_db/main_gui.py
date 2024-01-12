from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QFileDialog
from gff21 import GFFVeriAktarici
from hasta_kayit import HastaKayit

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        dosya_sec_label = QLabel("GFF Dosyasını Seçin:")
        self.dosya_yolu_line = QLineEdit()
        dosya_sec_button = QPushButton("Dosya Seç")

        table_name_label = QLabel("Tablo İsmi:")
        self.table_name_line = QLineEdit()

        dosya_adi_label = QLabel("Kaydedilecek Dosya Adı:")
        self.dosya_adi_line = QLineEdit()

        veri_aktar_button = QPushButton("Veriyi Aktar")

        # Hasta ekleme alanları
        isim_label = QLabel("İsim:")
        self.isim_line = QLineEdit()

        soyisim_label = QLabel("Soyisim:")
        self.soyisim_line = QLineEdit()

        dogum_tarihi_label = QLabel("Doğum Tarihi:")
        self.dogum_tarihi_line = QLineEdit()

        cinsiyet_label = QLabel("Cinsiyet:")
        self.cinsiyet_line = QLineEdit()

        dogum_yeri_label = QLabel("Doğum Yeri:")
        self.dogum_yeri_line = QLineEdit()

        hasta_ekle_button = QPushButton("Hasta Ekle")

        dosya_sec_button.clicked.connect(self.dosya_sec)
        veri_aktar_button.clicked.connect(self.veri_aktar)
        hasta_ekle_button.clicked.connect(self.hasta_ekle)

        v_layout = QVBoxLayout()
        v_layout.addWidget(dosya_sec_label)
        v_layout.addWidget(self.dosya_yolu_line)
        v_layout.addWidget(dosya_sec_button)
        v_layout.addWidget(table_name_label)
        v_layout.addWidget(self.table_name_line)
        v_layout.addWidget(dosya_adi_label)
        v_layout.addWidget(self.dosya_adi_line)
        v_layout.addWidget(veri_aktar_button)

        # Hasta ekleme alanlarını layout'a ekleme
        v_layout.addWidget(isim_label)
        v_layout.addWidget(self.isim_line)
        v_layout.addWidget(soyisim_label)
        v_layout.addWidget(self.soyisim_line)
        v_layout.addWidget(dogum_tarihi_label)
        v_layout.addWidget(self.dogum_tarihi_line)
        v_layout.addWidget(cinsiyet_label)
        v_layout.addWidget(self.cinsiyet_line)
        v_layout.addWidget(dogum_yeri_label)
        v_layout.addWidget(self.dogum_yeri_line)
        v_layout.addWidget(hasta_ekle_button)

        self.setLayout(v_layout)
        self.setWindowTitle("GFF Veri Aktarıcı Arayüzü")

    def dosya_sec(self):
        dosya_adi, _ = QFileDialog.getOpenFileName(self, "GFF Dosyasını Seç", "", "GFF Files (*.gff)")
        if dosya_adi:
            self.dosya_yolu_line.setText(dosya_adi)

    def veri_aktar(self):
        dosya_yolu = self.dosya_yolu_line.text()
        table_name = self.table_name_line.text()
        dosya_adi = self.dosya_adi_line.text()

        if dosya_yolu and table_name and dosya_adi:
            veri_aktarici = GFFVeriAktarici(dosya_yolu, 'localhost', 'root', 'Nukleotits.1', 'Nukleotits')
            veri_aktarici.veri_aktar(table_name)
            veri_aktarici.exon_mrna_verileri_kaydet_sql(dosya_adi, table_name)
            QMessageBox.information(self, "Başarılı", "Veri aktarımı tamamlandı.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    def hasta_ekle(self):
        isim = self.isim_line.text()
        soyisim = self.soyisim_line.text()
        dogum_tarihi = self.dogum_tarihi_line.text()
        cinsiyet = self.cinsiyet_line.text()
        dogum_yeri = self.dogum_yeri_line.text()

        hasta_kayit = HastaKayit(isim, soyisim, dogum_tarihi, cinsiyet, dogum_yeri)
        hasta_kayit.hasta_ekle()
        QMessageBox.information(self, "Başarılı", "Hasta başarıyla eklendi.")

if __name__ == "__main__":
    app = QApplication([])
    arayuz = MainGUI()
    arayuz.show
