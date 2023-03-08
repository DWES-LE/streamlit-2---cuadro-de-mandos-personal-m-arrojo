# 📈 Cuadro de mandos personal 📊
 
> Usa este repositorio para crear un cuadro de mandos personal con Streamlit. Documenta los siguientes apartados del README.
> Incluye en tu README la url de donde has publicado tu aplicación. Pon la `url` también en el `About` de tu repositorio.

## Objetivo
Diseño de un cuadro de mandos personal para visualización e interacción con un conjunto de datos.
He escogido realizar mi trabajo sobre los alojamientos Airbnb en Barcelona. El cuadro de mandos permite filtrar por opciones y representa los alojamientos en un mapa.

## Búsqueda y documentación de los datos
He encontrado un dataset en [Kaggle](https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities?select=barcelona_weekdays.csv) con los datos de los precios de los alojamientos de varias ciudades de Europa y he escogido Barcelona. La fuente de los datos es de [Zenodo](https://zenodo.org/record/4446043#.Y9Y9ENJBwUE).

Los datos están en formato csv y contienen los siguientes campos:
- realSum: el precio total del alojamiento para dos personas y dos noches en EUR
- room_type: el tipo de alojamiento
- room_shared: variable dummy para habitaciones compartidas
- room_private: variable dummy para habitaciones privadas
- person_capacity: el número máximo de huéspedes
- host_is_superhost: variable dummy para el estado de superhost
- multi: variable dummy si el listado pertenece a anfitriones con 2-4 ofertas
- biz: variable dummy si el listado pertenece a anfitriones con más de 4 ofertas
- cleanliness_rating: calificación de limpieza
- guest_satisfaction_overall: calificación general del listado
- bedrooms: número de habitaciones (0 para estudios)
- dist: distancia al centro de la ciudad en km
- metro_dist: distancia a la estación de metro más cercana en km
- attr_index: índice de atracción de la ubicación del listado
- attr_index_norm: índice de atracción normalizado (0-100)
- rest_index: índice de restaurantes de la ubicación del listado
- attr_index_norm: índice de restaurantes normalizado (0-100)
- lng: longitud de la ubicación del listado
- lat: latitud de la ubicación del listado

## Visualización de los datos
Prepara visualizaciones diferentes del dataframe en texto (tablas) o gráficas (histogramas, barras, etc.). Puedes usar matplotlib, seaborn, plotly, etc.

Para la visualización de los datos en Streamlit, he utilizado pandas para representar un pie chart con el rango de precios de la selección de alojamientos, plotly express para generar dos histogramas con las valoraciones de limpieza y alojamiento y folium para representar los alojamientos en un mapa.
He necesitado instalar la versión 0.3.1 de branca para que el mapa tuviera visibilidad.

## Publicación de la aplicación.
La aplicación está publicada en [Streamlit Sharing](https://share.streamlit.io/).
