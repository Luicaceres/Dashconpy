import dash  # Asegúrate de importar dash
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State
from utilidades import create_figure, df

def fetch_data(cursor):
    query = '''
        SELECT sum(Cantidad) as cantidad, BCONOM 
        FROM FACT_CARTERA_TDC a
        JOIN DIM_BANCOS b ON b.ID_DIM_BANCOS = a.ID_DIM_BANCOS
        JOIN DIM_STAT_CTA c ON a.ID_STAT_CTA = c.ID_COD_STAT
        JOIN DIM_STAT_TARJ d ON a.ID_DIM_STAT_TARJ = d.ID_DIM_STAT_TARJ
        JOIN DIM_TIPO_PLASTICO e ON a.ID_DIM_TIP_PLAST = e.ID_DIM_TIPO_PLASTICO
        WHERE COD_STAT = '01' AND COD_TAR = '1'
        GROUP BY BCONOM
    '''
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Consulta ejecutada correctamente.")
        print(f"Resultados: {result}")
        return result
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return []

def register_callbacks(app, cursor):
    @app.callback(
        [Output('graph-1', 'figure'), Output('graph-2', 'figure'), Output('graph-3', 'figure'), Output('graph-4', 'figure')],
        [Input('dropdown-1', 'value'), Input('dropdown-2', 'value'), Input('dropdown-3', 'value'), Input('dropdown-4', 'value'),
         Input('color-picker-1', 'value'), Input('color-picker-2', 'value'), Input('color-picker-3', 'value'), Input('color-picker-4', 'value'),
         Input('work-slider', 'value'), Input('interval-component', 'n_intervals')]
    )
    def update_graphs(dropdown1, dropdown2, dropdown3, dropdown4, color1, color2, color3, color4, slider_value, n_intervals):
        ctx = dash.callback_context

        # Fetch data from the database
        data = fetch_data(cursor)
        df_db = pd.DataFrame(data, columns=['cantidad', 'BCONOM'])  # Ajusta las columnas según tu consulta

        # Ajustar df basado en el valor del slider
        adjusted_df = df.copy()
        adjusted_df['Trabajo'] = df['Trabajo'] * slider_value

        color1_hex = color1['hex']
        color2_hex = color2['hex']
        color3_hex = color3['hex']
        color4_hex = color4['hex']

        # Crear gráficos
        figure1 = px.bar(df_db, x='BCONOM', y='cantidad', title='Datos de Oracle en Tiempo Real', color_discrete_sequence=[color1_hex])
        figure2 = create_figure(dropdown2, adjusted_df, slider_value, color2_hex)
        figure3 = create_figure(dropdown3, adjusted_df, slider_value, color3_hex)
        figure4 = create_figure(dropdown4, adjusted_df, slider_value, color4_hex)

        if ctx.triggered:
            triggered_input = ctx.triggered[0]['prop_id'].split('.')[0]
            if triggered_input == 'interval-component':
                print("Intervalo activado, actualizando datos...")
            else:
                print(f"Input activado: {triggered_input}")

        return figure1, figure2, figure3, figure4
