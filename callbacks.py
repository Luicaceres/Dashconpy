from dash.dependencies import Input, Output, State
from utilidades import create_figure, df

def register_callbacks(app):
    @app.callback(
        [Output('sidebar', 'style'), Output('graphs-container', 'style')],
        [Input('toggle-button', 'n_clicks')],
        [State('sidebar', 'style'), State('graphs-container', 'style')]
    )
    def toggle_sidebar(n_clicks, sidebar_style, graphs_style):
        if sidebar_style is None:
            sidebar_style = {'display': 'none', 'position': 'fixed', 'top': '56px', 'left': '-260px', 'width': '250px', 'padding': '10px', 'background-color': '#f8f9fa', 'height': 'calc(100vh - 56px)', 'overflow-y': 'auto', 'transition': 'left 0.3s ease-in-out'}
        if graphs_style is None:
            graphs_style = {'width': '100%', 'margin-left': '0'}

        # Ajuste para asegurar que el sidebar y los gráficos se ajusten correctamente
        if n_clicks is None or n_clicks % 2 == 0:
            sidebar_style['display'] = 'none'
            sidebar_style['left'] = '-260px'
            graphs_style = {'width': '100%', 'margin-left': '0'}
        else:
            sidebar_style['display'] = 'block'
            sidebar_style['left'] = '0px'
            graphs_style = {'width': 'calc(100% - 260px)', 'margin-left': '260px'}

        return sidebar_style, graphs_style

    @app.callback(
        [Output('graph-1', 'figure'), Output('graph-2', 'figure'), Output('graph-3', 'figure'), Output('graph-4', 'figure')],
        [Input('dropdown-1', 'value'), Input('dropdown-2', 'value'), Input('dropdown-3', 'value'), Input('dropdown-4', 'value'),
         Input('color-picker-1', 'value'), Input('color-picker-2', 'value'), Input('color-picker-3', 'value'), Input('color-picker-4', 'value'),
         Input('work-slider', 'value')]
    )
    def update_graphs(dropdown1, dropdown2, dropdown3, dropdown4, color1, color2, color3, color4, slider_value):
        adjusted_df = df.copy()
        adjusted_df['Trabajo'] = df['Trabajo'] * slider_value

        color1_hex = color1['hex']
        color2_hex = color2['hex']
        color3_hex = color3['hex']
        color4_hex = color4['hex']

        figure1 = create_figure(dropdown1, adjusted_df, slider_value, color1_hex)
        figure2 = create_figure(dropdown2, adjusted_df, slider_value, color2_hex)
        figure3 = create_figure(dropdown3, adjusted_df, slider_value, color3_hex)
        figure4 = create_figure(dropdown4, adjusted_df, slider_value, color4_hex)

        return figure1, figure2, figure3, figure4
