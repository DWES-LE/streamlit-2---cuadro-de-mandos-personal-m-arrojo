import streamlit as st
import pandas as pd
import altair as alt
import random

# Cargar datos desde CSV
df = pd.read_csv("provincias.csv")

# Título del cuadro de mandos
st.title("Cuadro de mandos de provincias españolas")

# Obtener dos provincias al azar
provincias = df['Provincia'].tolist()
provincia_1, provincia_2 = random.sample(provincias, 2)

# Crear una lista con las características para comparar
caracteristicas = ['Población', 'Área (km²)', 'Ingreso per cápita (EUR)', 'Tasa de desempleo (%)', 'Índice de calidad de vida']

# Crear el selector de provincias y de características
provincia_1 = st.sidebar.selectbox("Selecciona la primera provincia:", provincias, index=provincias.index(provincia_1))
provincia_2 = st.sidebar.selectbox("Selecciona la segunda provincia:", provincias, index=provincias.index(provincia_2))
caracteristica = st.sidebar.selectbox("Selecciona la característica a comparar:", caracteristicas)

# Obtener los datos de cada provincia seleccionada
data_1 = df.loc[df['Provincia'] == provincia_1]
data_2 = df.loc[df['Provincia'] == provincia_2]

# Obtener los valores de la característica seleccionada para cada provincia
valor_1 = data_1[caracteristica].values[0]
valor_2 = data_2[caracteristica].values[0]

# Crear la visualización comparativa
chart_data = pd.DataFrame({
    'Provincia': [provincia_1, provincia_2],
    caracteristica: [valor_1, valor_2]
})

st.write("Comparación de las provincias seleccionadas:")
st.write(chart_data)

chart = alt.Chart(chart_data).mark_bar().encode(
    x='Provincia:N',
    y=caracteristica + ':Q'
).properties(
    width=600,
    height=400
)

st.altair_chart(chart)
