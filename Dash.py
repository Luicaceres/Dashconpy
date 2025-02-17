import dash
from dash import dcc
from dash import html
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash.dependencies import Input, Output, State



 # Crear una aplicación Dash con Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Datos de ejemplo
df = pd.DataFrame({
    "Personas": ["yop", "augusto","douglar","Rolando"],
    "Trabajo": [10, 20,  15, 20]
})

# Datos de ejemplo para el gráfico de Velas
df_candlestick = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2022', periods=4),
    'Open': [10, 15, 14, 13],
    'High': [15, 18, 17, 16],
    'Low': [7, 12, 10, 11],
    'Close': [12, 16, 13, 15]
})


# Crear una figura de Plotly
#fig = px.bar(df, x="Personas", y="Trabajo", title="Gráfico de Barra")
#fig_line = px.line(df, x="Personas", y="Trabajo", title="Gráfico de Líneas")
#fig_scatter = px.scatter(df, x="Personas", y="Trabajo", title="Gráfico de Dispersión")
#fig_area = px.area(df, x="Personas", y="Trabajo", title="Gráfico de Área")
#fig_pie = px.pie(df, names="Personas", values="Trabajo", title="Gráfico de Pastel")
#fig_box = px.box(df, x="Personas", y="Trabajo", title="Gráfico de Caja")
#fig_hist = px.histogram(df, x="Trabajo", title="Histograma")
#heatmap_data = pd.DataFrame(np.random.randn(10, 10), columns=list('ABCDEFGHIJ'))
#fig_heatmap = px.imshow(heatmap_data, title="Mapa de Calor")

#figures = [
#    {'id': 'line-chart', 'figure': px.line(df, x="Personas", y="Trabajo", title="Gráfico de Líneas")},
#    {'id': 'scatter-plot', 'figure': px.scatter(df, x="Personas", y="Trabajo", title="Gráfico de Dispersión")},
#    {'id': 'area-chart', 'figure': px.area(df, x="Personas", y="Trabajo", title="Gráfico de Área")},
#    {'id': 'pie-chart', 'figure': px.pie(df, names="Personas", values="Trabajo", title="Gráfico de Pastel")},
#    {'id': 'box-plot', 'figure': px.box(df, x="Personas", y="Trabajo", title="Gráfico de Caja")},
#    {'id': 'histogram', 'figure': px.histogram(df, x="Trabajo", title="Histograma")},
#    {'id': 'heatmap', 'figure': px.imshow(pd.DataFrame(np.random.randn(10, 10), columns=list('ABCDEFGHIJ')), title="Mapa de Calor")}
#]

# Función para actualizar figuras con datos ajustados
# Función para actualizar figuras con datos ajustados y colores personalizados
def create_figure(fig_type, df, slider_value, color):
    if fig_type == 'line-chart':
        return px.line(df, x="Personas", y="Trabajo", title="Gráfico de Líneas", color_discrete_sequence=[color])
    elif fig_type == 'bar-chart':
        return px.bar(df, x="Personas", y="Trabajo", title="Gráfico de Barras", color_discrete_sequence=[color])
    elif fig_type == 'scatter-plot':
        return px.scatter(df, x="Personas", y="Trabajo", title="Gráfico de Dispersión", color_discrete_sequence=[color])
    elif fig_type == 'pie-chart':
        return px.pie(df, names="Personas", values="Trabajo", title="Gráfico de Pastel", color_discrete_sequence=px.colors.sequential.RdBu)
    elif fig_type == 'area-chart':
        return px.area(df, x="Personas", y="Trabajo", title="Gráfico de Área", color_discrete_sequence=[color])
    elif fig_type == 'box-plot':
        return px.box(df, x="Personas", y="Trabajo", title="Gráfico de Caja", color_discrete_sequence=[color])
    elif fig_type == 'histogram':
        return px.histogram(df, x="Trabajo", title="Histograma", color_discrete_sequence=[color])
    elif fig_type == 'heatmap':
        return px.imshow(pd.DataFrame(np.random.randn(10, 10) * slider_value, columns=list('ABCDEFGHIJ')), title="Mapa de Calor", color_continuous_scale=px.colors.sequential.RdBu)
    elif fig_type == 'candlestick':
        fig = go.Figure(data=[go.Candlestick(x=df_candlestick['Date'], open=df_candlestick['Open'], high=df_candlestick['High'], low=df_candlestick['Low'], close=df_candlestick['Close'])])
        fig.update_layout(title="Gráfico de Velas", yaxis_title='Precio')
        return fig
    elif fig_type == 'violin':
        return px.violin(df, y="Trabajo", x="Personas", title="Gráfico de Violín", color_discrete_sequence=[color], box=True, points="all")
    elif fig_type == 'gantt':
        df_gantt = [dict(Task="Task 1", Start='2021-01-01', Finish='2021-02-28'),
                    dict(Task="Task 2", Start='2021-03-01', Finish='2021-04-30')]
        return ff.create_gantt(df_gantt, title="Gráfico de Gantt")
    elif fig_type == 'funnel':
        return px.funnel(df, x="Trabajo", y="Personas", title="Gráfico de Embudo", color_discrete_sequence=[color])
    elif fig_type == 'sunburst':
        return px.sunburst(df, path=['Personas'], values='Trabajo', title="Gráfico de Sunburst", color_discrete_sequence=[color])

#fig_line.update_layout(height=400,
#     width=800,
#     xaxis_title="Personas", 
#    yaxis_title="Trabajo"
#    ) 


# Función para generar la cuadrícula de gráficos
#def generate_graph_grid(figures, cols=2):
#    rows = []
#    for i in range(0, len(figures), cols):
#        row = dbc.Row([
#            dbc.Col(dcc.Graph(id=fig['id'], figure=fig['figure']), width=6)
#            for fig in figures[i:i+cols]
#        ], align="center")
#        rows.append(row)
#    return rows

# Diseño de la aplicación
#app.layout = dbc.Container([
#    html.H1('Mi Dashboard con Múltiples Gráficos'),#
#
#    dbc.Row([
#        dbc.Col(dcc.Graph(id='line-chart', figure=fig_line), width=4),
#        dbc.Col(dcc.Graph(id='scatter-plot', figure=fig_scatter), width=4),
#        dbc.Col(dcc.Graph(id='area-chart', figure=fig_area), width=4)
#    ], align="center"),#
#
#    dbc.Row([
#        dbc.Col(dcc.Graph(id='pie-chart', figure=fig_pie), width=4),
#        dbc.Col(dcc.Graph(id='box-plot', figure=fig_box), width=4),
#        dbc.Col(dcc.Graph(id='histogram', figure=fig_hist), width=4)
#    ], align="center"),#
#
#    dbc.Row([
#        dbc.Col(dcc.Graph(id='heatmap', figure=fig_heatmap), width=4)
#    ], align="center")
#], fluid=True)

# Lista de opciones para el menú desplegable
# Función para actualizar figuras con datos ajustadosdropdown_options = [{'label': fig['figure'].layout.title['text'], 'value': fig['id']} for fig in figures]
dropdown_options = [
    {'label': 'Gráfico de Líneas', 'value': 'line-chart'},
    {'label': 'Gráfico de Barras', 'value': 'bar-chart'},
    {'label': 'Gráfico de Dispersión', 'value': 'scatter-plot'},
    {'label': 'Gráfico de Área', 'value': 'area-chart'},
    {'label': 'Gráfico de Pastel', 'value': 'pie-chart'},
    {'label': 'Gráfico de Caja', 'value': 'box-plot'},
    {'label': 'Histograma', 'value': 'histogram'},
    {'label': 'Mapa de Calor', 'value': 'heatmap'},
    {'label': 'Gráfico de Velas', 'value': 'candlestick-chart'},
    {'label': 'Gráfico de Violin', 'value': 'violin-plot'},
    {'label': 'Gráfico de Gantt', 'value': 'gantt-chart'},
    {'label': 'Gráfico de Embudo', 'value': 'funnel-chart'},
    {'label': 'Gráfico de Sunburst', 'value': 'sunburst-chart'}
]

# Estilos CSS para el sidebar y la animación
styles = {
    'sidebar': {
        'position': 'fixed',
        'top': '0',  # Asegura que el sidebar esté completamente visible
        'left': '-260px',  # Start off-screen
        'width': '250px',
        'padding': '10px',
        'background-color': '#f8f9fa',
        'height': '100vh',
        'overflow-y': 'auto',
        'transition': 'left 0.3s ease-in-out'
    },
    'sidebar_visible': {
        'left': '0px'  # Move on-screen
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

# Callback para mostrar/ocultar el sidebar con animación y ajustar el tamaño de los gráficos
@app.callback(
    [Output('sidebar', 'style'), Output('graphs-container', 'style')],
    [Input('toggle-button', 'n_clicks')],
    [State('sidebar', 'style'), State('graphs-container', 'style')]
)
def toggle_sidebar(n_clicks, sidebar_style, graphs_style):
    # Inicializar estilos si son None
    if sidebar_style is None:
        sidebar_style = styles['sidebar']
    if graphs_style is None:
        graphs_style = {'width': '100%', 'transition': 'width 0.3s ease-in-out'}
    
    if n_clicks % 2 == 0:
        sidebar_style.update(styles['sidebar_visible'])
        graphs_style.update({'width': 'calc(100% - 260px)', 'transition': 'width 0.3s ease-in-out', 'margin-left': '260px'})
    else:
        sidebar_style.update({'left': '-260px'})
        graphs_style.update({'width': '100%', 'transition': 'width 0.3s ease-in-out', 'margin-left': '0'})
    return sidebar_style, graphs_style

# Callback para actualizar los gráficos según la selección del menú desplegable, el slider y el color
@app.callback(
    [Output('graph-1', 'figure'), Output('graph-2', 'figure'), Output('graph-3', 'figure'), Output('graph-4', 'figure')],
    [Input('dropdown-1', 'value'), Input('dropdown-2', 'value'), Input('dropdown-3', 'value'), Input('dropdown-4', 'value'),
     Input('color-picker-1', 'value'), Input('color-picker-2', 'value'), Input('color-picker-3', 'value'), Input('color-picker-4', 'value'),
     Input('work-slider', 'value')]
)
def update_graphs(dropdown1, dropdown2, dropdown3, dropdown4, color1, color2, color3, color4, slider_value):
    adjusted_df = df.copy()
    adjusted_df['Trabajo'] = df['Trabajo'] * slider_value

    # Extraer el valor hexadecimal del color seleccionado
    color1_hex = color1['hex']
    color2_hex = color2['hex']
    color3_hex = color3['hex']
    color4_hex = color4['hex']

    figure1 = create_figure(dropdown1, adjusted_df, slider_value, color1_hex)
    figure2 = create_figure(dropdown2, adjusted_df, slider_value, color2_hex)
    figure3 = create_figure(dropdown3, adjusted_df, slider_value, color3_hex)
    figure4 = create_figure(dropdown4, adjusted_df, slider_value, color4_hex)

    return figure1, figure2, figure3, figure4

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
