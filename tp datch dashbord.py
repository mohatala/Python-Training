import dash
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go


df=pd.read_csv("C:/Users/21260/Desktop/Master/Python/dataset_dash.csv")
#print(df.columns[1:])

app = dash.Dash()
app.layout = html.Div([
    html.H1("Langage"),
    dcc.Dropdown([df.columns[1], df.columns[2], df.columns[3]],df.columns[1], id='demo-dropdown'),
    html.Div(children =[
    dcc.Graph(
        id='graph1',
        className='dropgraph',
    ),
    ])
])
l=[]
for m in df.MOIS:
    l.append(m)
@app.callback(
    Output('graph1', 'figure'),
    Input('demo-dropdown', 'value')
)

def update_graph(value):
    l1=[]
    for m in df.loc[:, {value}]:
        l1.append(m)
    print(l1)
    col='skyblue'
    return {'data':[go.Line(
                            x=l,
                            y=l1,
                            marker_color=col),
                         ] ,
            'layout': go.Layout(
                        title='test',   
                    )    
           }




if __name__ == '__main__':
    app.run_server()
