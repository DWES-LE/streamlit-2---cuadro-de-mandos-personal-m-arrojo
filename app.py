import streamlit as st
import pandas as pd
import plotly.express as px
import folium

# Cargar datos


@st.cache_data()
def load_data():
    data = pd.read_csv("airbnb_barcelona.csv")
    return data


data = load_data()

# ,realSum,room_type,room_shared,room_private,person_capacity,host_is_superhost,multi,biz,cleanliness_rating,guest_satisfaction_overall,bedrooms,dist,metro_dist,attr_index,attr_index_norm,rest_index,rest_index_norm,lng,lat
# 0,474.3174994763423,Entire home/apt,False,False,4.0,False,0,1,10.0,91.0,1,1.111996477976483,0.6304909460189917,526.4694202447247,17.942926962147965,915.5870827687069,20.1548895790265,2.17556,41.39624

# Crea un diccionario para traducir los valores de room_type a español
room_type_dict = {"Entire home/apt": "Apartamento completo",
                  "Private room": "Habitación privada",
                  "Shared room": "Habitación compartida"}

# Filtrar por tipo de alojamiento
room_type_options = ["Todos"] + [room_type_dict[value]
                                 for value in data["room_type"].unique()]
room_type = st.sidebar.selectbox("Tipo de alojamiento", room_type_options)
if room_type != "Todos":
    data = data[data["room_type"] == room_type]

# Filtrar por capacidad
capacity = st.sidebar.slider("Capacidad (personas)", 1, 7, 1)
data = data[data["person_capacity"] >= capacity]

# Filtrar por distancia al centro
center_dist = st.sidebar.slider("Distancia al centro (km)", 0, 10, 5)
data = data[data["dist"] <= center_dist]

# Filtrar por precio
price = st.sidebar.slider("Precio por noche (€)", 0, 1000, 100)
data = data[data["realSum"] <= price]

# Filtrar por superhost
superhost = st.sidebar.checkbox("¿Anfitrión superhost?")
data = data[data["host_is_superhost"] == superhost]

# Filtrar por satisfacción del huésped
satisfaction = st.sidebar.slider("Satisfacción del huésped", 0, 100, 100)
data = data[data["guest_satisfaction_overall"] <= satisfaction]

confirma = st.sidebar.button("Confirmar")


# Pantalla principal de la aplicación
st.title("Encuentra tu alojamiento en Barcelona!")
st.write("¿Estás buscando un Airbnb en Barcelona y ya no sabes por donde mirar? Este cuadro de mandos te permite filtrar los alojamientos por aspectos como el tipo, capacidad, precio, la satisfacción del huésped y más. ¡Prueba a modificar los filtros y descubre dónde puedes alojarte en esta ciudad tan bonita!")
imagen = st.image("barcelona.jpg", use_column_width=True)

if confirma:
    imagen.empty()
    foto = ("")
    fuente = ("")

    st.sidebar.success("Filtro aplicado")
    # Mostrar mapa con los resultados
    st.header("Resultados de la búsqueda")
    st.write("Échale un vistazo al mapa para ver dónde están los alojamientos que hemos encontrado. Haz click en cada marcador para ver más información sobre el alojamiento.")
    m = folium.Map(location=[41.3879, 2.1699], zoom_start=12)

    for i, row in data.iterrows():
        folium.Marker([row["lat"], row["lng"]],
                      popup=f"Precio por noche: {row['realSum']}€\nTipo de alojamiento: {row['room_type']}\nCapacidad: {row['person_capacity']}").add_to(m)

    st.write(m)

    if len(data) > 0:
        # Mostrar resultados en una tabla
        st.subheader(f"Se han encontrado {len(data)} alojamientos:")
        st.write(data)
        # Pie chart con rangos de precios
        fig_pie = px.pie(data, values='realSum', names=pd.cut(data['realSum'], bins=[0, 50, 100, 150, 200, 250, 300, 400, 500, 600, 1000], labels=[
                        '0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-400', '400-500', '500-600', '600+']))
        st.write("Rangos de precios de los resultados:")
        st.plotly_chart(fig_pie)

        # Histograma de las calificaciones de limpieza
        fig_cleanliness = px.histogram(data, x='cleanliness_rating', nbins=20)
        st.write("Distribución de las calificaciones de limpieza de los resultados:")
        st.plotly_chart(fig_cleanliness)

        # Histograma de las calificaciones de satisfacción del huésped
        fig_satisfaction = px.histogram(data, x='guest_satisfaction_overall', nbins=20)
        st.write("Distribución de las calificaciones de satisfacción del huésped de los resultados:")
        st.plotly_chart(fig_satisfaction)

    else:
        st.subheader("No se han encontrado resultados :( Prueba a modificar los filtros.")
