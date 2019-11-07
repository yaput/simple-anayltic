from dash.dependencies import Input, Output
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = ['aster', 'avivo', 'healthcare']
app.layout = html.Div([
    html.Label('Bot Choice'),
    # dcc.Input(id='my-id', value='initial value', type='text'),
    dcc.Dropdown(id='my-id', options=[{'label': k, 'value': k} for k in all_options], value='aster'),
    html.Div(id='my-div'),
])


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    df = pd.read_csv(open(input_value+'_default_fallback.csv'))
    return generate_table(df)


if __name__ == '__main__':
    app.run_server(debug=True)

