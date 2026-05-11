# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

import csv


class data:
    amount = 0
    date = ''
    reigion = ''
    def __init__(self, amount, date, region):
        self.amount = amount
        self.date = date
        self.region = region

datapoints = []
lines = 0
with open('daily_sales_data_formatted.csv', mode='r') as csvFile:
    pointer= csv.reader(csvFile)
    for row in pointer:
        amount = row[0]
        date = row[1]
        region = row[2]

        if lines != 0:
            datapoints.append(data(amount, date, region))
        lines += 1
datapoints = datapoints[:-1]

def plots(number):
    if number > len(datapoints):
        return len(datapoints)
    return number



# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
app = Dash()

df = pd.DataFrame({
    "Amount": [datapoints[i].amount for i in range(plots(1))],
    "Date": [datapoints[i].date for i in range(plots(1))],
    "Region": [datapoints[i].region for i in range(plots(1))]
})

fig = px.line(df, x="Amount", y="Date", color="Region", title="Fruit Amounts in Regions")


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
