class CSV:

    structure = {}
    keylist = []

    def __init__(self):
        self.structure = {}
        self.keylist = []

    def read_csv(self):
        file = open("resources/Project2DataTrimmed.csv", "r")
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

    def print_row(self):
        print("Printing a row:")
        row = input("Please enter a row between 1 and 20: ")
        try:
            for key in self.keylist:
                print(key + ": " + self.structure[key][int(row)-1])
        except:
            print("Invalid row/value entered.")


def main():
    test = CSV
    test.read_csv(CSV)
    test.print_cell(CSV)
    test.print_row(CSV)


if __name__ == '__main__':
    main()
