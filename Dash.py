import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash.dependencies import Input, Output, State
from callbacks import register_callbacks

# Crear una aplicación Dash con Bootstrap y estilos personalizados
app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP, 
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",  # Importa FontAwesome Icons
    "https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css"  # Importa Bootstrap Icons
], assets_folder='assets')  # Asegúrate de que la carpeta 'assets' exista

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

# Diseño de la barra de navegación
navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("Dashboard Interactivo 2x2", className="ml-2"),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse(
            dbc.Nav([
                dbc.NavItem(dbc.NavLink(html.I(className="bi bi-gear-fill"), id="toggle-button", n_clicks=0, style={"fontSize": "1.5rem", "padding": "0", "width": "auto"})),
            ], className="ml-auto", navbar=True),
            id="navbar-collapse",
            is_open=False,  # Inicialmente cerrado
            navbar=True,
        ),
    ]),
    color="dark",
    dark=True,
    className="mb-4",
    fixed="top"  # Asegúrate de que la barra de navegación esté fija en la parte superior
)

# Callback para manejar el colapso del navbar
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [Input("toggle-button", "n_clicks")],
    [State("navbar-collapse", "is_open")]
)
def toggle_navbar_collapse(n, t, is_open):
    if n or t:
        return not is_open
    return is_open

# Diseño de la aplicación
app.layout = dbc.Container([
    navbar,
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
        ], id='sidebar', style={'display': 'none'}),
    ], id='sidebar-container'),

    dbc.Row(id='graphs-container', children=[
        dbc.Col(dcc.Graph(id='graph-1', className='graph-col'), width=6, xs=12, sm=12, md=6, lg=6, xl=6),
        dbc.Col(dcc.Graph(id='graph-2', className='graph-col'), width=6, xs=12, sm=12, md=6, lg=6, xl=6),
        dbc.Col(dcc.Graph(id='graph-3', className='graph-col'), width=6, xs=12, sm=12, md=6, lg=6, xl=6),
        dbc.Col(dcc.Graph(id='graph-4', className='graph-col'), width=6, xs=12, sm=12, md=6, lg=6, xl=6),
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
], fluid=True, style={'marginTop': '60px'})  # Asegúrate de que los componentes se desplazan hacia abajo

# Registrar los callbacks
register_callbacks(app)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
