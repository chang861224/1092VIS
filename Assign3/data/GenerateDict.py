import json 

def getDetails(year=2000, n=5):
    csvFile = "{}-President.csv".format(str(year))
    data = dict()

    with open(csvFile, "r") as f:
        titles = f.readline().rstrip("\n").split(",")
        lines = f.readlines()
    for line in lines:
        items = line.rstrip("\n").split(",")
        city = {}
        for i in range(1, n + 6):
            city[titles[i]] = int(items[i])
        data[items[0]] = city
    return data

if __name__ == "__main__":
#    print(getDetails(2000, 5))
#    print(getDetails(2004, 2))
#    print(getDetails(2008, 2))
    print(getDetails(2012, 3))
#    print(getDetails(2016, 3))
#    print(getDetails(2020, 3))

