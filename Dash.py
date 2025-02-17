import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_daq as daq
from callbacks import register_callbacks

# Crear una aplicación Dash con Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Lista de opciones para el menú desplegable
dropdown_options = [
    {'label': 'Gráfico de Líneas', 'value': 'line-chart'},
    {'label': 'Gráfico de Barras', 'value': 'bar-chart'},
    {'label': 'Gráfico de Dispersión', 'value': 'scatter-plot'},
    {'label': 'Gráfico de Área', 'value': 'area-chart'},
    {'label': 'Gráfico de Pastel', 'value': 'pie-chart'},
    {'label': 'Gráfico de Caja', 'value': 'box-plot'},
    {'label': 'Histograma', 'value': 'histogram'},
    {'label': 'Mapa de Calor', 'value': 'heatmap'},
    {'label': 'Gráfico de Velas', 'value': 'candlestick'},
    {'label': 'Gráfico de Violín', 'value': 'violin'},
    {'label': 'Gráfico de Gantt', 'value': 'gantt'},
    {'label': 'Gráfico de Embudo', 'value': 'funnel'},
    {'label': 'Gráfico de Sunburst', 'value': 'sunburst'}
]

# Estilos CSS para el sidebar y la animación
# Estilos CSS para el sidebar y la animación (continuación)
styles = {
    'sidebar': {
        'position': 'fixed',
        'top': '0',
        'left': '-260px',
        'width': '250px',
        'padding': '10px',
        'background-color': '#f8f9fa',
        'height': '100vh',
        'overflow-y': 'auto',
        'transition': 'left 0.3s ease-in-out'
    },
    'sidebar_visible': {
        'left': '0px'
    }
}

# Diseño de la aplicación
app.layout = dbc.Container([
    html.H1('Dashboard Interactivo 2x2', style={'padding-left': '260px', 'padding-top': '10px'}),
    html.Button('Mostrar/Ocultar Configuración', id='toggle-button', n_clicks=0, style={'position': 'absolute', 'left': '10px', 'top': '10px', 'z-index': '1'}),
    html.Div([
        html.Div([
            html.H4("Configuración Gráfico 1"),
            dcc.Dropdown(id='dropdown-1', options=dropdown_options, value='line-chart', clearable=False),
            daq.ColorPicker(id='color-picker-1', label='Selecciona un color', value=dict(hex='#FF0000')),
            html.Hr(),
            html.H4("Configuración Gráfico 2"),
            dcc.Dropdown(id='dropdown-2', options=dropdown_options, value='scatter-plot', clearable=False),
            daq.ColorPicker(id='color-picker-2', label='Selecciona un color', value=dict(hex='#00FF00')),
            html.Hr(),
            html.H4("Configuración Gráfico 3"),
            dcc.Dropdown(id='dropdown-3', options=dropdown_options, value='area-chart', clearable=False),
            daq.ColorPicker(id='color-picker-3', label='Selecciona un color', value=dict(hex='#0000FF')),
            html.Hr(),
            html.H4("Configuración Gráfico 4"),
            dcc.Dropdown(id='dropdown-4', options=dropdown_options, value='pie-chart', clearable=False),
            daq.ColorPicker(id='color-picker-4', label='Selecciona un color', value=dict(hex='#FFA500')),
        ], id='sidebar', style=styles['sidebar']),
    ], id='sidebar-container'),
    
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col(dcc.Graph(id='graph-1', style={'width': '100%'}), width=6),
                dbc.Col(dcc.Graph(id='graph-2', style={'width': '100%'}), width=6)
            ], align="center"),
            dbc.Row([
                dbc.Col(dcc.Graph(id='graph-3', style={'width': '100%'}), width=6),
                dbc.Col(dcc.Graph(id='graph-4', style={'width': '100%'}), width=6)
            ], align="center")
        ], id='graphs-container', width=12)
    ]),

    # Slider para ajustar un parámetro (por ejemplo, multiplicar los valores de 'Trabajo')
    dcc.Slider(
        id='work-slider',
        min=1,
        max=10,
        step=1,
        value=1,
        marks={i: str(i) for i in range(1, 11)}
    )
], fluid=True, style={'padding-left': '260px'})

# Registrar los callbacks
register_callbacks(app)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
