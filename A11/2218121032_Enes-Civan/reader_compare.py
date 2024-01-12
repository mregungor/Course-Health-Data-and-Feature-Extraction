#This code will let you read fna formated fasta files and compare 2 locations of your choosing
#Gene numbers are based on the reference placings from the file so in order to get the placing numbers of your search, you will have to use the functions from reader_search code

from Bio.Seq import Seq
from Bio.Align import PairwiseAligner
from Bio import SeqIO

def main():
    file_path = "cds_from_genomic.fna"
    print(f"Similarity rate: {getDiff(3, 65, file_path, True):.2f}%")
    
def getTheGene(file_path, input, getReference):
    reqGene = "Not filled yet"
    nextGenom = 1
    cycle = 1
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(">lcl") != -1:
                if input == cycle:
                    nextGenom = 1
                    if getReference:
                        reqGene = lines[lines.index(line)]
                    else:
                        reqGene = ""
                    while True:
                        if lines[lines.index(line) + nextGenom].find(">lcl") != -1:
                            file.close
                            return reqGene
                        reqGene = reqGene + lines[lines.index(line) + nextGenom]
                        nextGenom += 1
                cycle += 1
    file.close
    return reqGene

def saveGene(file_path, input):
    with open(file_path, 'w') as file:
        file.write(input)
    file.close()

def getDiff(gene1no, gene2no, file_path, saveGenes):
    if saveGenes:
        saveGene("gene1.fna", getTheGene(file_path, gene1no, True))
        saveGene("gene2.fna", getTheGene(file_path, gene2no, True))
        gene1obj = SeqIO.read("gene1.fna", "fasta")
        gene2obj = SeqIO.read("gene2.fna", "fasta")
        
    else:
        gene1obj = Seq(getTheGene(file_path, gene1no, False))
        gene2obj = Seq(getTheGene(file_path, gene2no, False))

    aligner = PairwiseAligner()
    score = aligner.score(gene1obj, gene2obj)
    alignments = aligner.align(gene1obj, gene2obj)

    print(alignments[0])
    return score / max(len(gene1obj), len(gene2obj)) * 100
    
if __name__ == "__main__":
    main()