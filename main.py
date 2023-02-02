import dash
from dash import dcc
from dash import html
from csv import reader
import collections

data_parts = collections.defaultdict(list)
with open('graph.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    next(read_obj)
    for row in csv_reader:
        language, month, value = row[0].split(';')
        data_parts[language].append({'month': month, 'value': value})

data_p = []
title_ = []
i = 0
for d in data_parts:
    months = []
    values = []
    title_.append(d)
    for data in data_parts[d]:
        months.append(data['month'])
        values.append(data['value'])
    data_p.append({'x': months, 'y': values, 'type': 'line' if i == 0 else 'bar', 'name': d})
    i += 1

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1("VOLUME HORAIRE / LANGUAGE DE PROGRAMMATION"),
    dcc.Graph(
        id="example",
        figure={'data': data_p, 'layout': {'title': ' '.join(title_)}}
    )
])

if __name__ == '__main__':
    app.run_server()
