from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Align
from Bio import Entrez

Entrez.email = "azrabaykus@gmail.com"

def benzerlik_hesapla(dna1, dna2):
    aligner = Align.PairwiseAligner()
    alignments = aligner.align(dna1, dna2)
    best_alignment = alignments[0]
    similarity_score = best_alignment.score / max(len(dna1), len(dna2))

    return similarity_score

def genbank_karsilastirma(user_dna, genbank_accessions):
    print("\nGenBank veritabanındaki DNA dizileri ile karşılaştırma sonuçları:")

    for accession in genbank_accessions:
        db_dna = fetch_genbank_sequence(accession)
        benzerlik = benzerlik_hesapla(user_dna, db_dna)
        print(f"Benzerlik Oranı girilen dna ve {accession} arasında: {benzerlik:.2%}")

        if benzerlik == 1.0:
            print("Bu iki DNA dizisi tam olarak uyuşuyor.")
        elif benzerlik >= 0.5:
            print("Bu iki DNA dizisi birinci dereceden akraba olabilir.")
        elif benzerlik >= 0.25:
            rint("Bu iki DNA dizisi ikinci dereceden akraba(teyze/amca yeğen,dede/ nine torun,üvey kardeş ilişkisi) olabilir.")
        elif benzerlik >= 0.06:
            print("Bu iki DNA dizisi ikinci dereceden akraba(kuzen-kuzen ilişkisi) olabilir.")
        else:
            print("Bu iki DNA dizisi belirtilen kriterlere uymuyor.")

#chatgpt
def fetch_genbank_sequence(accession):
    with Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text") as handle:
        record = SeqIO.read(handle, "genbank")
        return str(record.seq)


def main():
    print("1: GenBank'ten DNA Karşılaştırma")
    print("2: İki Kişinin DNA'sını Karşılaştırma")

    secim = input("Lütfen seçiminizi yapın (1 veya 2): ")

    if secim == '1':
        # Kullanıcıdan DNA dizisini al
        user_dna = input("Lütfen kendi DNA'nızı girin: ")

        genbank_accessions = ["NM_001301717", "NM_001301718", "NM_001301719", "NM_001301720", "NM_001301721"]
        # GenBank'ten DNA dizilerini al
        genbank_karsilastirma(user_dna, genbank_accessions)

    elif secim == '2':
        # İki kişinin DNA'sını karşılaştırma yapılacak
        dna1 = input("Lütfen ilk kişinin DNA'sını girin: ")
        dna2 = input("Lütfen ikinci kişinin DNA'sını girin: ")

        benzerlik = benzerlik_hesapla(dna1, dna2)

        print(f"\nBenzerlik Oranı: {benzerlik:.2%}")

        if benzerlik == 1.0:
            print("Bu iki DNA dizisi tam olarak uyuşuyor.")
        elif benzerlik >= 0.5:
            print("Bu iki DNA dizisi birinci dereceden akraba olabilir.")
        elif benzerlik >= 0.25:
            print("Bu iki DNA dizisi ikinci dereceden akraba(teyze/amca yeğen,dede/ nine torun,üvey kardeş ilişkisi) olabilir.")
        elif benzerlik >= 0.06:
            print("Bu iki DNA dizisi ikinci dereceden akraba(kuzen-kuzen ilişkisi) olabilir.")
        else:
            print("Bu iki DNA dizisi belirtilen kriterlere uymuyor.")

    else:
        print("Geçersiz seçim. Lütfen 1 veya 2 girin.")

if __name__ == "__main__":
    main()


