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

## Prepara tu aplicación.
La aplicación se llamará `app.py`. Añade un `requirements.txt` con las dependencias de tu aplicación. Ve actualizándolo a medida que vayas añadiendo librerías.

## Carga y análisis de conjunto de dato con pandas
Carga el conjunto de datos en un dataframe de pandas y realiza un análisis exploratorio de los datos.

## Visualización de los datos
Prepara visualizaciones diferentes del dataframe en texto (tablas) o gráficas (histogramas, barras, etc.). Puedes usar matplotlib, seaborn, plotly, etc.

## Diseña la interacción que van a tener tus datos
Qué inputs y outputs tendrán tus datos. 

## Prepara la aplicación (cuadro de mandos) con Streamlit
Prepara y prueba la aplicación.

## Publica la aplicación.
Publica la aplicación en Streamlit Cloud, en Heroku o en el servicio que prefieras https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app
