import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

df = pd.read_csv("neededtable.csv")

app.layout = html.Div(style={"textAlign" : "center", 'width':'80%', 'paddingLeft':'10%'}, children=[
    html.H1(
        children='Made with <3 by Vishwas Modhera',
        style={"textAlign":"center", 'weight':'bold'}
    ),
    html.Br(),
    html.H2(
        children='A Dash web-app to visualize data.',
        style={'textAlign':'center'}
    ),
    html.H5(
        children='Call structure is check-list to data table, and check-list to Graph. Graph is not daisy-chained with data table.',
        style={'textAlign':'center'}
    ),
    html.Hr(),
    dcc.Checklist(
        id='item-selector',
        options=[{'label':i, 'value':i} for i in df['Item Type'].unique()]
    ),
    html.Hr(),
    dash_table.DataTable(
        id='data-table',
        columns=[{'name': i, 'id':i, 'deletable':False, 'selectable':True} for i in df.columns],
        data=df.to_dict('records'),
        editable=True,
        filter_action='native',
        sort_action='native',
        sort_mode='multi',
        column_selectable='multi',
        selected_columns=[],
        selected_rows=[],
        #row_selectable='multi',
        row_deletable=True,
        export_format='xlsx',
        export_headers='display',
        merge_duplicate_headers=True
    ),
    html.Hr(),
    html.Div(id='table-graph')
])

@app.callback(
    Output('data-table', 'data'),
    [Input('item-selector', 'value')] 
)
def update_table(value):
    dff = df[df['Item Type'].isin(value)]
    #fig = px.line(dff.T, title='Data Visualiser')
    return dff.to_dict('records')

@app.callback(
    Output('table-graph', 'children'),
    [Input('data-table', 'derived_virtual_data'),
    Input('data-table', 'derived_virtual_selected_rows')]
)
def update_figure(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = df if rows is None else pd.DataFrame(rows)

    return [dcc.Graph(id='table-plot', figure= px.line(dff.T))]

if __name__ == "__main__":
    app.run_server(debug=True)
