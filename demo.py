from flask import Flask, request, render_template
import dash
from dash import dcc, html, State, Output, Input

# 创建flask应用
app = Flask(__name__)

# 创建Flask路由
@app.route('/')
def index():
    return render_template('index.html')

# 创建dash应用
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dash/')

# Dash 布局
dash_layout = html.Div(
    [
        html.H1('Hello Dash'),
        html.Div([html.P('Welcome to dash page')]),
        html.Hr(),
        html.A(
            html.Button('Back to Home'),
            href='/'  # 指向Flask页面
        ),
        html.Div(
            [
                dcc.Input(id='input_box', type='text', placeholder='enter something...'),
                html.Button("Submit", id='submit_btn'),
            ]
        ),
        html.Div(id='output'),
        dcc.Graph(
            id='sample_graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 7, 8], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 9, 6], 'type': 'bar', 'name': 'NYC'},
                ],
                'layout': {
                    'title': 'Dash visualization demo'
                }
            }
        )
    ]
)

dash_app.layout = dash_layout

# dash_app callback
@dash_app.callback(
    Output('output', 'children'),
    Input('submit_btn', 'n_clicks'),
    State('input_box', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, text_input):
    if n_clicks:
        return f'You entered {text_input}'
    return dash.no_update()

# Flask 路由
@app.route('/send_data')
def send_data():
    return "Data from Flask"

# 运行应用
if __name__ == '__main__':
    app.run(debug=True)  # 加入debug模式
