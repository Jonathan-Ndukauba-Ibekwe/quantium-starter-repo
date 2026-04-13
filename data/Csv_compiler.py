"""for every line that contains piink morsel
this is the 30(n-1) +2 to 30(n-1) +5 line of the csv file
if currentLine % 28 == 2:
    # this is the line with the piink morsel
"""

import csv
from decimal import Decimal
data0 = []
data1 = []
data2 = []
dataFormat = []


with open('daily_sales_data_0.csv', 'r') as csvfile0:
    reader = csv.reader(csvfile0)
    for line in reader:
        product = line[0]
        price = line[1][1:] # remove the $ sign
        quantity = line[2]
        date = line[3]
        reigion = line[4]
        if product == "pink morsel":
            data0.append([float(price) * int(quantity), date, reigion])

with open('daily_sales_data_1.csv', 'r') as csvfile1:
    reader = csv.reader(csvfile1)
    for line in reader:
        product = line[0]
        price = line[1][1:] # remove the $ sign
        quantity = line[2]
        date = line[3]
        reigion = line[4]
        if product == "pink morsel":
            data1.append([float(price) * int(quantity), date, reigion])

with open('daily_sales_data_2.csv', 'r') as csvfile2:
    reader = csv.reader(csvfile2)
    for line in reader:
        product = line[0]
        price = line[1][1:] # remove the $ sign
        quantity = line[2]
        date = line[3]
        reigion = line[4]
        if product == "pink morsel":
            data2.append([float(price) * int(quantity), date, reigion])


with open('daily_sales_data_formatted.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['total_sales', 'date', 'region'])
    for row0 in data0:
        writer.writerow(row0)
    for row1 in data1:
        writer.writerow(row1)
    for row2 in data2:
        writer.writerow(row2)