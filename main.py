class CSV:

    structure = {}
    keylist = []

    def __init__(self):
        self.structure = {}
        self.keylist = []

    def read_csv(self):
        file = open("/home/dalton/Documents/School_Stuff/CS421/Data.csv", "r");
        for x in file.readline().split(","):
            self.structure.update({x: []})
            self.keylist.append(x)

        for lines in file:
            array = lines.split(",")
            for i in range(len(self.keylist)):
                self.structure[self.keylist[i]].append(array[i])


def main():
    test = CSV
    test.read_csv(CSV)


if __name__ == '__main__':
    main()
