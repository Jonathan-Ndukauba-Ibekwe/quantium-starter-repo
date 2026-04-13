"""for every line that contains piink morsel
this is the 30(n-1) +2 to 30(n-1) +5 line of the csv file
if currentLine % 28 == 2:
    # this is the line with the piink morsel
"""

import csv
data0 = []
data1 = []
data2 = []



with open('daily_sales_data_0.csv', 'r') as csvfile0:
    reader = csv.reader(csvfile0)
    for line in reader:
        if line[0] == "pink morsel":
            data0.append(line)

print(data0)