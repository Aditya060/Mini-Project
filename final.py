import dash
import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Output, Input  # used in the section callback

df = pd.read_csv("movies.csv")  # pandas dataframe



# Page Layout
app = dash.Dash(__name__)
# Html layout
app.layout = html.Div([
    #setting up the headings for the page
    #Division for Bar-Graph
	html.Div([
    html.H1("User Data based Graphs in Python", style={
            'color': 'blue', 'fontSize': 40, 'textAlign': 'center'}),
      html.H1("Created by Aditya Thapliyal 2016593", style={
            'color': 'black', 'fontSize': 20, 'textAlign': 'left'}),
     html.H2("BAR-GRAPHS", style={
            'color': 'red', 'fontSize': 30, 'textAlign': 'center'}),


    dcc.Dropdown(id='Choice',
                 options=[{'label': x, 'value': x}
                          for x in (df.Genre.unique())],
                 value='Comedy'  # default value
                 ),
    dcc.Graph(id='python-graph', figure={}),
   ]),

    #Division for Pie Chart
    html.Div([
        
         html.H2("PIECHART", style={
            'color': 'red', 'fontSize': 30, 'textAlign': 'center'}),
        # dcc.Dropdown(id='Choice2',
        #              options=[{'label': x, 'value': x}
        #                       for x in (df.Genre.unique())],
        #              value='Romance'  # default value
        #              ),
        dcc.Graph(id='python-graph2', figure={}),
    ]),


    html.Div([

        #Division for Histogram
         html.H2("HISTOGRAM", style={
            'color': 'red', 'fontSize': 30, 'textAlign': 'center'}),
        # dcc.Dropdown(id='Choice3',
        #              options=[{'label': x, 'value': x}
        #                       for x in (df.Genre.unique())],
        #              value='Romance'  # default value
        #              ),
        dcc.Graph(id='python-graph3', figure={}),
    ])])



@app.callback(
    Output(component_id='python-graph', component_property='figure'),
    Input(component_id='Choice', component_property='value'),
    # Output(component_id='python-graph2', component_property='figure2'),
    # Input(component_id='Choice2', component_property='value')
)  # callback decorator
def interactive_graphing(value_genre):
    dff = df[df.Genre == value_genre]
    fig = px.bar(data_frame=dff, x="Audience score %", y="Worldwide Gross", opacity=0.5,hover_name='Film',
    	color='Year',   # if values in column z = 'some_group' and 'some_other_group'
    color_discrete_map={
        
    
    })
    return fig
    

@app.callback(
    Output(component_id='python-graph2', component_property='figure'),
     Input(component_id='Choice', component_property='value'),
    
)  # callback decorator
def interactive_graphing(value_genre):
    dff = df[df.Genre == value_genre]
    fig2 = px.pie(data_frame=dff, names="Film", values="Audience score %")
    return fig2


@app.callback(
    Output(component_id='python-graph3', component_property='figure'),
    Input(component_id='Choice', component_property='value'),
)  # callback decorator
def interactive_graphing(value_genre):
    dff = df[df.Genre == value_genre]
    fig3 = px.histogram(data_frame=dff,x='Audience score %')
   
    return fig3
        
    
    
   


    # fig.update_layout(bargap=0.2)
                


if __name__ == '__main__':
    app.run_server(debug=True, port=8002)







