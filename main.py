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

    def sort_by_col(self):
        print("Select a column to sort by. The opeions are as follows: ")
        print("1. Facility Zip Code, 2. Latitude, 3. Longitude, or 4. Total Air Emissions in pounds.")
        num = input("Enter choice (1-4): ")

        values = []
        key = ""

        if int(num) == 1:
            key = "Facility Zip Code"
        elif int(num) == 2:
            key = "Latitude"
        elif int(num) == 3:
            key = "Longitude"
        elif int(num) == 4:
            key = "Total Air Emissions (Pounds)"

        for x in range(len(self.structure[key])):
            number = float(self.structure[key][x])
            values.append((number, x))

        values.sort()
        print(type(values[0][1]))

        for x in values:
            print(key + ": " + str(x[0]))

def main():
    test = CSV
    test.read_csv(CSV)
    test.print_cell(CSV)
    test.print_row(CSV)
    test.sort_by_col(CSV)


if __name__ == '__main__':
    main()
