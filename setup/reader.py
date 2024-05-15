from tabula import convert_into
from os import remove

def load_data():
    convert_into("2023-PSSD-York-University.pdf", "infile.csv", output_format="csv", guess=False, pages="all")
    print("Done conversion!")
    with open("infile.csv") as filein, open("output.csv", "w") as fileout:
            for line in filein:
                if line.split(",")[0] == "2023":
                    line = line.replace("2023,Universities,","").replace("York University","").replace(",,",",")
                    fileout.write(line)
                else:
                    continue
    remove("infile.csv")

if __name__ == "__main__":
    load_data()