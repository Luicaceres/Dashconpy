import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np

# Datos de ejemplo
df = pd.DataFrame({
    "Personas": ["Yop", "Augusto", "Douglar", "Rolando"],
    "Trabajo": [10, 15, 7, 5]
})

# Datos de ejemplo para el gráfico de Velas
df_candlestick = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2022', periods=4),
    'Open': [10, 15, 14, 13],
    'High': [15, 18, 17, 16],
    'Low': [7, 12, 10, 11],
    'Close': [12, 16, 13, 15]
})

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
