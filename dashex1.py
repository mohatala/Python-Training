import pandas as pd
import dash
from dash import dcc
from dash import html

df = pd.read_csv(r'C:\Users\21260\Desktop\Master\Python\langage.csv',index_col=0)
print(df)
app = dash.Dash()
data_part1 = {'x':[df.columns[0]],
                'y':[df.columns[1]],
                'type':'line',
                'name':'Trucks'}
data_part2 = {'x':[df.columns[0]],
                'y':[df.columns[2]],
                'type':'line',
                'name':'Trucks'}
data_part3 = {'x':[df.columns[0]],
                'y':[df.columns[3]],
                'type':'bar',
                'name':'Ships'}
app.layout = html.Div(children =[
    html.H1("Volume Horaire/Langage de programmation"),
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

