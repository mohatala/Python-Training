import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("DATABASE.csv",sep=";")
df2 = df.groupby('MOIS')['QUANTITE'].sum().reset_index()
df3=df.groupby('VENDEUR')['QUANTITE'].sum().reset_index()
df4=df.groupby('VENDEUR')['VENDEUR'].count().reset_index(name="count")
df5=df.groupby('TRIMESTRE')['PU'].sum().reset_index()
df6=df.groupby('ANNEE')['ANNEE'].count().reset_index(name="count")
#df7=df.groupby('VENDEUR')['VENDEUR'].count().reset_index(name="count")
##print(df['%'])

# ======================== Setting the margins
layout = go.Layout(
    margin=go.layout.Margin(
        l=40,  # left margin
        r=40,  # right margin
        b=10,  # bottom margin
        t=35  # top margin
    )
)

def get_bar_chart():
    barChart = dcc.Graph(figure=go.Figure(layout=layout).add_trace(go.Bar(x=df3["VENDEUR"],
                                                                          y=df3['QUANTITE'],
                                                                          marker=dict(color='#351e15'))).update_layout(
        title='Somme des quantités / VENDEUR', plot_bgcolor='rgba(0,0,0,0)'),
        style={'width': '50%', 'height': '40vh', 'display': 'inline-block'})
    return barChart
def get_line_chart():
    lineChart = dcc.Graph(figure=go.Figure(layout=layout).add_trace(go.Scatter(x=df4['VENDEUR'],
                                                                               y=df4['count'],
                                                                               marker=dict(
                                                                                   color='#351e15'))).update_layout(
        title='ventes / vendeur', plot_bgcolor='rgba(0,0,0,0)'),
        style={'width': '50%', 'height': '40vh', 'display': 'inline-block'})
    return lineChart
def get_scatter_plot():
    scatterPlot = dcc.Graph(figure=go.Figure(layout=layout).add_trace(go.Scatter(x=df5['TRIMESTRE'],
                                                                                 y=df5['PU'],
                                                                                 marker=dict(
                                                                                     color='#351e15'),
                                                                                 mode='markers')).update_layout(
        title='Somme des pu / trimestre', plot_bgcolor='rgba(0,0,0,0)'),
        style={'width': '50%', 'height': '40vh', 'display': 'inline-block'})
    return scatterPlot
def get_line_chart2():
    lineChart = dcc.Graph(figure=go.Figure(layout=layout).add_trace(go.Scatter(x=df6['ANNEE'],
                                                                               y=df6['count'],
                                                                               marker=dict(
                                                                                   color='#351e15'))).update_layout(
        title='Nombre de ventes / année', plot_bgcolor='rgba(0,0,0,0)'),
        style={'width': '50%', 'height': '40vh', 'display': 'inline-block'})
    return lineChart
def get_pie_chart():
    pieChart = dcc.Graph(
        figure=go.Figure(layout=layout).add_trace(go.Pie(
            labels=df6['ANNEE'],
            values=df6['count'],
            marker=dict(colors=['#120303', '#300f0f', '#381b1b', '#4f2f2f', '#573f3f', '#695a5a', '#8a7d7d'],
                        line=dict(color='#ffffff', width=2)))).update_layout(title='Rendement/Vendeur',
                                                                             plot_bgcolor='rgba(0,0,0,0)',
                                                                             showlegend=False),
        style={'width': '50%', 'height': '40vh', 'display': 'inline-block'})
    return pieChart
# ======================== Dash App
app = dash.Dash(__name__)
# ======================== App Layout
app.layout = html.Div([
    html.H1('Analyse Des Ventes', style={'text-align': 'center', 'background-color': '#ede9e8'}),
    get_bar_chart(),
    get_line_chart(),
    get_scatter_plot(),
    get_line_chart2(),
    get_pie_chart(),
])
if __name__ == '__main__':
    app.run_server()

