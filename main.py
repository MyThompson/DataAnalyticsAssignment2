class data:

    structure = {}
    keylist = []

    def __init__(self):
        self.structure = {}
        self.keylist = []

    def read_csv(self, location):
        file = open(location, "r")
        for x in file.readline().split(","):
            self.structure.update({x: []})
            self.keylist.append(x)
            self.keylist.append(x)

        # Ignores any value that has a broken row (because the csv for the consumer reports is broken)
        for lines in file:
            if lines == "":
                pass
            else:
                array = lines.split(",")
                if len(array) != len(self.keylist):
                    pass
                else:
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

        for key in self.keylist:
            print(key + ": ")
            for row in values:
                print(self.structure[key][row[1]])

    def getStateAmount(self):
        state = input("Enter a state code you would like to see (ex: IN): ")
        statesDict = {}
        for x in self.structure["State"]:
            try:
                statesDict[x] += 1
            except:
                statesDict.update({x: 1})

        print("Number of complaints in " + state + ": " + str(statesDict[state]))

    def read_xml(self):
        pass

    def read_xml(self):
        pass


def main():
    num = int(input("Enter 1 for part one, 2 for part 2: "))
    if num == 1:
        test = data
        value = int(input("Enter 1. for CSV, 2. for XML, 3. for JSON (options 2 and 3 don't work): "))
        if value == 1:
            test.read_csv(test, "resources/Project2DataTrimmed.csv")
        if value == 2:
            test.read_xml(test)
        if value == 3:
            test.read_json(test)
        test.print_cell(test)
        test.print_row(test)
        test.sort_by_col(test)
    if num == 2:
        test = data
        test.read_csv(test, "resources/consumer.csv")
        test.getStateAmount(test)


if __name__ == '__main__':
    main()
