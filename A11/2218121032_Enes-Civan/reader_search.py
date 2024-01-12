def main():
    thingToSearch = input("What are you looking for in the database? ")
    #thingToSearch = "gene=SLC6A9"
    file_path = "cds_from_genomic.fna"
    print(search_str(file_path, thingToSearch, 21, "output1", True))

def search_str(file_path, word, chrosomeNo, fileName, wholeGenes):
    con = "y"
    nextGenom = 1
    rval = 0
    geneToSave = ""
    chrosomeSearch = ""
    if wholeGenes:
        rlist = []
    if chrosomeNo < 10:
        chrosomeSearch = '0' + str(chrosomeNo)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        rval = 0
        for line in lines:
            if line.find(">lcl|NC_0000" + chrosomeSearch) != -1:
                rval = rval + 1
            if line.find(word) != -1 and con == "y":
                print(word, 'exists in file')
                print('Line Number:', lines.index(line) + 1)
                print('Line:', line)
                nextGenom = 1
                geneToSave = lines[lines.index(line)]
                while lines[lines.index(line) + nextGenom].find(">lcl|NC_0000" + chrosomeSearch) == -1:
                    print(lines[lines.index(line) + nextGenom], end="")
                    geneToSave += lines[lines.index(line) + nextGenom]
                    if lines[lines.index(line) + nextGenom].find(">lcl|NC_0000" + chrosomeSearch) != -1:
                        break
                    nextGenom += 1
                if not wholeGenes:
                    con = input("Print more results (y/n): ")
                    if con == "n":
                        if fileName != "":
                            file.close
                            fileName += ".fna"
                            with open(fileName, 'w') as file:
                                file.write(geneToSave)
                        break
                else:
                    rlist.append(rval)
                    
    file.close
    if wholeGenes:
        return rlist
    return rval

if __name__ == "__main__":
    main()