import pandas as pd
import mysql.connector

class GFFVeriAktarici:
    def __init__(self, dosya_yolu, host, kullanici, sifre, veritabani):
        self.dosya_yolu = dosya_yolu
        self.host = host
        self.kullanici = kullanici
        self.sifre = sifre
        self.veritabani = veritabani

    def dosyayi_oku(self):
        columns = ['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
        return pd.read_csv(self.dosya_yolu, sep='\t', comment='#', names=columns)

    def veritabani_baglan(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.kullanici,
            password=self.sifre,
            database=self.veritabani
        )

    def veri_aktar(self, table_name):
        gff_data = self.dosyayi_oku()
        conn = self.veritabani_baglan()
        cursor = conn.cursor()

        try:
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    seqid TEXT,
                    source TEXT,
                    type TEXT,
                    start INT,
                    end INT,
                    score FLOAT,
                    strand TEXT,
                    phase TEXT,
                    attributes TEXT
                )
            ''')

            for index, row in gff_data.iterrows():
                if row['seqid'] == 'NC_000021.9':
                    if row['score'] == '.':
                        score_value = None
                    else:
                        if pd.notnull(row['score']):
                            score_value = float(row['score'])
                        else:
                            score_value = None
                    cursor.execute(f'''
                        INSERT INTO {table_name} (seqid, source, type, start, end, score, strand, phase, attributes)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (row['seqid'], row['source'], row['type'], row['start'], row['end'], score_value, row['strand'], row['phase'], row['attributes']))
            conn.commit()
            print("Veri aktarımı tamamlandı.")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            conn.close()

    def exon_mrna_verileri_kaydet_sql(self, dosya_adi, table_name):
        conn = self.veritabani_baglan()
        cursor = conn.cursor()

        try:
            with open(dosya_adi, 'w') as dosya:
                dosya.write("Type\tStart\tEnd\n")

                cursor.execute(f'''
                    SELECT type, start, end
                    FROM {table_name}
                    WHERE type = 'exon' OR type = 'mrna'
                ''')

                for row in cursor.fetchall():
                    dosya.write(f"{row[0]}\t{row[1]}\t{row[2]}\n")

                print(f"Exon ve mrna verileri {dosya_adi} dosyasına kaydedildi.")
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            conn.close()
