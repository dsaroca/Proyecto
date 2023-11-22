# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pJ0VLCYJ8TNsm03RhrSRYjIj-QIbp7we
"""

import plotly.graph_objects as go
import pandas as pd

# Datos
data = {
    'Tipo': ["Competencia Fisica", "Competencia Artistica", "Citas", "Competencia Gastronomica", "Convivencia"],
    'Cantidad': [32, 29, 6, 8, 1],
    'Formato': ["Tradicional", "Tradicional", "Moderno", "Moderno", "Moderno"]
}

# Crear un DataFrame a partir de los datos
df = pd.DataFrame(data)

# Definir colores para cada formato de reality
formato_colors = {
    "Tradicional": 'lightgreen',
    "Moderno": 'fuchsia'
}

# Crear una figura de barras
fig = go.Figure()

# Añadir las barras al gráfico
for formato in df['Formato'].unique():
    df_temp = df[df['Formato'] == formato]
    fig.add_trace(go.Bar(
        x=df_temp['Tipo'],
        y=df_temp['Cantidad'],
        name=formato,
        marker_color=formato_colors.get(formato, 'gray')  # Color gris si no hay coincidencia
    ))

# Personalizar el diseño del gráfico
fig.update_layout(
    title='Tipos de reality más transmitidos en Chile',
    title_font=dict(size=50, color='Pink', family='Times New Roman'),
    title_x=0.5,  # Centro horizontalmente el título
    xaxis_title='Tipo de reality',
    yaxis_title='Cantidad',
    barmode='group'  # Agrupar las barras por tipo de formato
)

# Mostrar el gráfico
fig.show()