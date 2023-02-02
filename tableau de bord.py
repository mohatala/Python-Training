import dash
from dash import dcc
from dash import html

app = dash.Dash()

data_part1 = {'x':[1, 2, 3, 4, 5],
                'y':[5, 4, 7, 4, 8],
                'type':'line',
                'name':'Trucks'}
data_part2 = {'x':[1, 2, 3, 4, 5],
                'y':[6, 3, 5, 3, 7],
                'type':'bar',
                'name':'Ships'}
data_part3 = {'x':[1.5, 3, 4, 5, 6],
                'y':[6, 3, 5, 3, 7],
                'type':'dotted',
                'name':'cars'}
app.layout = html.Div(children =[
    html.H1("Dash Tutorial"),
    dcc.Graph(
        id ="example",
        figure ={
            'data':[data_part1, data_part2, data_part3],
            'layout':{
                'title':'Basic Dashboard'
                }
            }
        )
    ])
if __name__ == '__main__':
    app.run_server()
