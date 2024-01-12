def main():
    #thingToSearch = "gene=SLC6A9"
    file_path = "cds_from_genomic.fna"
    print("gene no 25:", getCategory(file_path, 25, "gene"))
    #printCategories(file_path, 25)
    #printAllCategories(file_path)

def printAllCategories(file_path):
    con = ""
    counter1 = 0
    code1 = ""
    gene = ""
    db_xref = ""
    protein = ""
    protein_id = ""
    location = ""
    gbkey = ""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(">lcl") != -1 and con != "n":
                counter1 = counter1 + 1
                print('Line Number:', lines.index(line), "Code Number:", counter1)
                code1 = line.split(" ", 1)[0]
                #print(code1)
                gene = line.split("[")[1].replace(']', '')
                #print(gene)
                db_xref = line.split("[")[2].replace(']', '')
                protein = line.split("[")[3].replace(']', '')
                protein_id = line.split("[")[4].replace(']', '')
                location = line.split("[")[5].replace(']', '')
                gbkey = line.split("[")[6].replace(']', '')
                print(code1, gene, db_xref, protein, protein_id, location, gbkey, sep="\n")
                con = ""
                while con != 'y':
                    con = input("Print more results (y/n): ")
                    if con == "n":
                        break
    file.close
    
def printCategories(file_path, num):
    counter1 = 1
    code1 = ""
    gene = ""
    db_xref = ""
    protein = ""
    protein_id = ""
    location = ""
    gbkey = ""
    cycle = 1
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(">lcl") != -1 and num == cycle:
                code1 = line.split(" ", 1)[0]
                #print(code1)
                gene = line.split("[")[1].replace(']', '')
                #print(gene)
                db_xref = line.split("[")[2].replace(']', '')
                protein = line.split("[")[3].replace(']', '')
                protein_id = line.split("[")[4].replace(']', '')
                location = line.split("[")[5].replace(']', '')
                gbkey = line.split("[")[6].replace(']', '')
                break
            
            elif line.find(">lcl") != -1 and num != cycle:
                cycle = cycle + 1
                counter1 = counter1 + 1
                
    print('Line Number:', lines.index(line) + 1, "Code Number:", counter1)
    print(code1, gene, db_xref, protein, protein_id, location, gbkey, sep="\n")
    file.close
    
def getCategory(file_path, num, var):
    cycle = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(">lcl") != -1 and cycle == num:
                code1 = line.split(" ", 1)[0]
                #print(code1)
                gene = line.split("[")[1].replace(']', '')
                #print(gene)
                db_xref = line.split("[")[2].replace(']', '')
                protein = line.split("[")[3].replace(']', '')
                protein_id = line.split("[")[4].replace(']', '')
                location = line.split("[")[5].replace(']', '')
                gbkey = line.split("[")[6].replace(']', '')
                break

            elif line.find(">lcl") != -1 and cycle != num:
                cycle = cycle + 1

            
    file.close
    if var == "code":
        return code1
    elif var == "gene":
        return gene
    elif var == "xref" or var == "db_xref":
        return db_xref
    elif var == "protein":
        return protein
    elif var == "protein_id" or var == "protein id":
        return protein_id
    elif var == "location":
        return location
    elif var == "gbkey":
        return gbkey
    
if __name__ == "__main__":
    main()