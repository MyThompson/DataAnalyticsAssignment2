class CSV:

    structure = {}
    keylist = []

    def __init__(self):
        self.structure = {}
        self.keylist = []

    def read_csv(self):
        file = open("SacramentocrimeJanuary2006.csv", "r")
        for x in file.readline().split(","):
            self.structure.update({x: []})
            self.keylist.append(x)

        for lines in file:
            array = lines.split(",")
            for i in range(len(self.keylist)):
                self.structure[self.keylist[i]].append(array[i])
        
    def print_cell(self):
        num = input("Please enter item number: ")
        key = input("Please enter item key: ")
        try:
            print(self.structure[key][int(num)])
        except:
            print("invalid cell")


def main():
    test = CSV
    test.read_csv(CSV)
    test.print_cell(CSV)
    


if __name__ == '__main__':
    main()
