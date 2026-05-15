# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import csv
import random

# x axis; dates of sales data; format: mm/dd/yyyy
Date = []

# y axis; sales data for each region; four lines for four regions
North = []
South = []
East = []
West = []


dateRange = 'all'
dateRange = 9999 if dateRange == 'all' else int(dateRange)*4  # default value of 9999 if no input is given
# copies relevant data from csv file into lists to be plotted
with open('daily_sales_data_formatted.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    lineCount = 0
    prevDate = '0'
    for line in reader:
        if line[1] == 'date': # skips header line
            continue
        if lineCount >= dateRange: # breaks loop when all lines have been read
            break
        if line[1] != prevDate:
            Date.append(line[1])
            prevDate = line[1]
        lineCount += 1
        if line[2] == 'north':
            North.append(float(line[0]))
        elif line[2] == 'south':
            South.append(float(line[0]))
        elif line[2] == 'east':
            East.append(float(line[0]))
        elif line[2] == 'west':
            West.append(float(line[0]))
        

"""
print(len(Date))
print(len(North))
print(len(South))
print(len(East))
print(len(West)) 
"""


# Creates a DataFrame from the data to be plotted
df = pd.DataFrame({
    "Date": Date,
    "North": North,
    "South": South,
    "East": East,
    "West": West
})
fig = px.line(df, x="Date", y=["North", "South", "East", "West"], title='Daily Revenue From 2018 to 2022 on Every Region')





app = Dash()
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
