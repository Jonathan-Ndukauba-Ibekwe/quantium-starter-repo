import csv

class data:
    amount = 0
    date = ''
    reigion = ''

    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

    def __init__(self, amount, date, region):
        self.amount = amount
        self.date = date
        self.region = region

datapoints = []


def DATA():
    datapointsReigion = []
    lines = 0
    with open('dashApp/daily_sales_data_formatted.csv', mode='r') as csvFile:
        pointer= csv.reader(csvFile)
        for row in pointer:
            amount = row[0]
            date = row[1]
            region = row[2]

            if lines != 0:
                datapointsReigion.append(data(amount, date, region))
            lines += 1
    return datapointsReigion[:-1]

def NORTH():
    north = []
    for datapoint in DATA():
        if datapoint.region == "North":
            north.append(datapoint)
    return north

def SOUTH():
    south = []
    for datapoint in DATA():
        if datapoint.region == "South":
            south.append(datapoint)
    return south

def EAST():
    east = []
    for datapoint in DATA():
        if datapoint.region == "East":
            east.append(datapoint)
    return east

def WEST():
    west = []
    for datapoint in DATA():
        if datapoint.region == "West":
            west.append(datapoint)
    return west
    